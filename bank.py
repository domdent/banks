import abcFinance
import abce

class Bank(abcFinance.Agent):
    """
    Bank
    """

    def init(self, cash_reserves):
        """

        """
        self.name = "bank" + str(self.id)
        self.accounts.make_stock_accounts(["cash", "Equity", "customer_assets"])
        self.book(debit=[("cash", cash_reserves)], credit=[("Equity", cash_reserves)])
        self.create("cash", cash_reserves)

    def credit_depositors(self):
        """

        """
        messages = self.get_messages("deposit")
        for msg in messages:
            sender = msg.sender
            amount = msg.content
            if len(sender) > 1 and type(sender) == tuple:
                sender = sender[0] + str(sender[1])
            print(sender)
            self.accounts.make_liability_accounts([(sender + "_deposit")])
            self.book(debit=[("customer_assets", amount)], credit=[(sender + "_deposit", amount)])


    def print_possessions(self):
        """

        """
        self.log("cash", self["cash"])



