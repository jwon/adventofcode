with open('input.txt') as f:
    crab_positions = sorted([int (i) for line in f for i in line.strip().split(',')])

least_fuel_cost = None
for pos in range(crab_positions[0], crab_positions[-1]):
    current_fuel_cost = 0
    for crab in crab_positions:
        current_fuel_cost += sum(i+1 for i in range(abs(crab - pos)))
    if least_fuel_cost is None or current_fuel_cost < least_fuel_cost:
        least_fuel_cost = current_fuel_cost

print(least_fuel_cost)
