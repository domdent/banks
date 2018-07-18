import abcFinance
import abce
import random

class Firm(abcFinance.Agent):
    """
    Firm
    """

    def init(self, starting_inv, num_banks, starting_money):
        """

        """
        self.create("goods", starting_inv)
        firm_id_deposit = ("firm" + str(self.id) + "_deposit")
        self.accounts.make_stock_accounts([firm_id_deposit, "goods"])
        self.accounts.book(debit=[(firm_id_deposit, 1000), ("goods", 1000)], credit=[("equity", 2000)])
        self.housebank = "bank" + str(random.randint(0, num_banks - 1))


    def open_bank_acc(self):
        balance = self.accounts["firm" + str(self.id) + "_deposit"].get_balance()[1]
        self.send_envelope(self.housebank, "deposit", balance)


    def sell_goods(self):
        """


        """
        for offer in self.get_offers("goods"):
            if self["goods"] > 2:
                self.accept(offer)
                self.book(debit=[((self.id + "_deposit"), 100)], credit=[("goods", 100)])

    def print_possessions(self):
        """
        prints possessions and logs money of a person agent
        """
        self.log("deposits", self.accounts["firm" + str(self.id) + "_deposit"].get_balance()[1])
        self.log("goods", self["goods"])
