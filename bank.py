import abcFinance

class Bank(abcFinance.Agent):
    """
    Bank
    """

    def init(self, cash_reserves):
        """

        """
        self.name = "bank"
        self.book(debit=[("cash", cash_reserves)])
        self.create("cash", cash_reserves)

    def credit_deposits(self):
        """

        """
        self.book(credit=[(sender_ID + "_deposit", amount)])


    def print_possessions(self):
        """

        """
        self.log("cash", self["money"])
        self.log("money", self["money"])



