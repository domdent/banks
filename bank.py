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

    def credit_depositors(self):
        """

        """
        for msg in self.get_messages("deposit"):
            self.book()


    def print_possessions(self):
        """

        """
        self.log("cash", self["cash"])



