import abcFinance


num_firms = 3
num_banks = 1
num_days = 20

# people
starting_money = 1000
population = 50

# firm
starting_inv = 200

# bank
cash_reserves = 10000


simulation = abcFinance.Simulation(name='economy', processes=1)


firms = simulation.build_agents(Firm, "firm", number=num_firms, starting_inv=starting_inv,
                                         num_banks=num_banks)
banks = simulation.build_agents(Bank, "bank", cash_reserves=cash_reserves, number=num_banks)
people = simulation.build_agents(People, "people", population=population)


all_agents = firms + banks + people

for r in range(num_days):
    simulation.time = r

    all_agents.print_possessions()
    all_agents.print_balance_sheet()







simulation.graph()
simulation.finalize()