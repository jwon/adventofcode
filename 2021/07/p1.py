with open('input.txt') as f:
    crab_positions = [int (i) for line in f for i in line.strip().split(',')]

least_fuel_cost = None
for pos in crab_positions:
    current_fuel_cost = 0
    for crab in crab_positions:
        current_fuel_cost += abs(crab - pos) 
    if least_fuel_cost is None or current_fuel_cost < least_fuel_cost:
        least_fuel_cost = current_fuel_cost

print(least_fuel_cost)
