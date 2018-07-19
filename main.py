import abcFinance
import abce
from bank import Bank
from firm import Firm
from people import People

num_firms = 4
num_banks = 2
num_days = 200
# people
starting_deposit_p = 1000
population = 50
# firm
starting_inv = 200
starting_deposit_f = 1000
# bank
cash_reserves = 10000

simulation = abce.Simulation(name='economy', processes=1)

firms = simulation.build_agents(Firm, "firm", number=num_firms, starting_inv=starting_inv,
                                         num_banks=num_banks, starting_money=starting_deposit_f)
banks = simulation.build_agents(Bank, "bank", cash_reserves=cash_reserves, number=num_banks)
people = simulation.build_agents(People, "people", number=1, population=population, starting_money=starting_deposit_p,
                                 num_banks=num_banks, num_firms=num_firms)

all_agents = firms + banks + people

# set up the bank accounts
(people + firms).open_bank_acc()
banks.credit_depositors()


for r in range(num_days):
    simulation.time = r

    people.create_income()
    banks.credit_income()

    people.buy_goods()
    firms.sell_goods()
    # bank needs to transfer funds on their side??
    banks.move_deposits()

    people.consume_goods()

    for agent in [people, firms, banks]:
        print(agent)
        agent.print_possessions()
        agent.print_balance_sheet()
        print("END")

    all_agents.book_end_of_period()


print("DONE")

simulation.graph()
simulation.finalize()