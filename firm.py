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
        self.firm_id_deposit = ("firm" + str(self.id) + "_deposit")
        self.accounts.make_stock_accounts([self.firm_id_deposit, "goods"])
        self.accounts.book(debit=[(self.firm_id_deposit, 1000), ("goods", 1000)], credit=[("equity", 2000)])
        self.housebank = "bank" + str(random.randint(0, num_banks - 1))


    def open_bank_acc(self):
        balance = self.accounts["firm" + str(self.id) + "_deposit"].get_balance()[1]
        self.send_envelope(self.housebank, "deposit", balance)


    def sell_goods(self):
        """


        """
        for offer in self.get_offers("goods"):
            if self["goods"] > 2:
                sender_id = offer.sender
                self.accept(offer)
                self.book(debit=[(self.firm_id_deposit, 100)], credit=[("goods", 100)])
                messages = self.get_messages("account")
                msg_sender = ""
                account = ""
                for msg in messages:
                    msg_sender = msg.sender
                    account = msg.content
                    if len(msg_sender) > 1 and type(msg_sender) == tuple:
                        msg_sender = msg_sender[0] + str(msg_sender[1])
                    if sender_id == msg_sender:
                        self.send_envelope(account, "withdraw", sender_id)
                        self.send_envelope(account, "amount", 100)
                        self.send_envelope(self.housebank, "deposit", 100)
                    else:
                        print("WARNING: Message sender and buy offer sender DO NOT MATCH!")

    def print_possessions(self):
        """
        prints possessions and logs money of a person agent
        """
        self.log("deposits", self.accounts["firm" + str(self.id) + "_deposit"].get_balance()[1])
        self.log("goods", self["goods"])
