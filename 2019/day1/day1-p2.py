import math


def calculate_fuel_requirement(module_mass):
    fuel_requirement = math.floor(module_mass / 3) - 2
    if fuel_requirement <= 0:
        return 0
    else:
        return fuel_requirement + calculate_fuel_requirement(fuel_requirement)


if __name__ == '__main__':
    total = 0
    with open('input.txt', 'r') as f:
        for line in f:
            module_mass = int(line)
            print(f'Total thus far: {total}')
            fuel_requirement = calculate_fuel_requirement(int(line))
            print(f'Module {module_mass} fuel requirement: {fuel_requirement}')
            total += fuel_requirement
    print(total)
