import abcFinance
import abce
import random


class People(abcFinance.Agent):
    """
    People
    """

    def init(self, population, starting_money, num_firms, num_banks):
        self.name = "people"
        self.population = population
        self.create("deposits", starting_money)
        self.accounts.make_stock_accounts(["goods"])
        self.accounts.make_flow_accounts(["consumption_expenses", "labour_value"])
        self.num_firms = num_firms
        self.num_banks = num_banks
        # split deposits across banks
        split_amount = float(self["deposits"]) / num_banks
        for i in range(self.num_banks):
            bank_id = "bank" + str(i) + "_deposit"
            self.accounts.make_stock_accounts([bank_id])
            self.accounts.book(debit=[(bank_id, split_amount)], credit=[("equity", split_amount)])

    def open_bank_acc(self):
        # for each bank send "deposit" so they can add it to their credit
        # look into using autobook
        for i in range(self.num_banks):
            print(i)
            bank_ID = "bank" + str(i)
            amount = self.accounts[bank_ID + "_deposit"].get_balance()[1]
            self.send_envelope(bank_ID, "deposit", amount)


    def buy_goods(self):
        """
        buy from a random firm
        """
        firm_number = random.randint(0, self.num_firms - 1)
        self.buy(('firm', firm_number), good='goods', quantity=2, price=50)
        bank_acc = "bank" + str(random.randint(0, self.num_banks - 1))
        self.book(debit=[("goods", 100)], credit=[(bank_acc + "_deposit", 100)])
        self.send_envelope(('firm', firm_number), "account", bank_acc)

    def print_possessions(self):
        """
        prints possessions and logs money of a person agent
        """
        total_deposits = 0
        for i in range(self.num_banks - 1):
            total_deposits += self.accounts["bank" + str(i) + "_deposit"].get_balance()[1]
        self.log("deposits", total_deposits)
        self.log("goods", self["goods"])

    def create_income(self):
        self.create("deposits", 100 * self.population)
        for i in range(self.num_banks):
            bank_acc = "bank" + str(i)
            self.book(debit=[(bank_acc + "_deposit", (100 * self.population)/self.num_banks)],
                      credit=[("labour_value", (100 * self.population)/self.num_banks)])
        for i in range(self.num_banks):
            bank_acc = "bank" + str(i)
            self.send_envelope(bank_acc, "wage", (100 * self.population)/self.num_banks)


    def consume_goods(self):
        self.destroy("goods", 1)
        self.book(debit=[("consumption_expenses", 50)], credit=[("goods", 50)])


