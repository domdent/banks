import abcFinance
immort random

class People(abcFinance.Agent):
    """
    People
    """

    def init(self, population, starting_money, num_firms):
        self.name = "people"
        self.population = population
        self.create("money", starting_money)
        self.make_stock_account(["Deposit", "Goods"])
        self.num_firms = num_firms

    def buy_goods(self):
        """
        buy from a random firm
        """
        firm_number = random.randint(0, self.num_firms)
        self.buy(('firm', firm_number), good='produce', quantity=2, price=50)
        self.book(debit=[("Goods", 100)], credit=[("Deposit", 100)])

