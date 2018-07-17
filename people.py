import abcFinance
import random

class People(abcFinance.Agent):
    """
    People
    """

    def init(self, population, starting_money, num_firms, num_banks):
        self.name = "people"
        self.population = population
        self.create("deposits", starting_money)
        self.make_stock_account(["goods"])
        self.num_firms = num_firms
        self.num_banks = num_banks
        # split deposits across banks
        self.split_amount = float(self["deposits"]) / num_banks
        for i in range(self.num_banks):
            self.make_stock_account(["bank" + str(i) + "_deposit", self.split_amount])

    def open_bank_acc(self):
        # for each bank send "deposit" so they can add it to their credit
        # look into using autobook
        for i in range(self.num_banks):
            bank_ID = "bank" + str(i)
            amount = self.accounts[bank_ID + "_deposit"].get_balance()[1]
            self.send(bank_ID, "deposit", amount)


    def buy_goods(self):
        """
        buy from a random firm
        """
        firm_number = random.randint(0, self.num_firms)
        self.buy(('firm', firm_number), good='produce', quantity=2, price=50)
        self.book(debit=[("goods", 100)], credit=[("deposits", 100)])

    def print_possessions(self):
        """
        prints possessions and logs money of a person agent
        """
        self.log("deposits", self.get_balance(self.id + "_deposit")[1])
        self.log("goods", self["goods"])
        for i in range(self.num_banks):
            self.log([str(self.id) + "_deposit"])
