import abcFinance
import random

class Firm(abcFinance.Agent):
    """
    Firm
    """

    def init(self, starting_inv, num_banks):
        """

        """
        self.create("produce", starting_inv)
        self.make_stock_account(["Deposit", "Goods", "Equity"])
        self.book(debit=[("Deposit", 1000), ("Goods", 1000)],
                  credit=[("Equity", 2000)])
        self.housebank = random.randint(0, num_banks - 1)

    def open_bank_acc(self):



    def sell_goods(self):
        """


        """
        for offer in self.get_offers("produce"):
            if self["produce"] > 2:
                self.accept(offer)
                self.book(debit=[("Deposit", 100)], credit=[("Goods", 100)])
