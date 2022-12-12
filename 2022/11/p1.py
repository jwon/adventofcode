from collections import defaultdict
import sys

monkey_items = {}
monkey_operations = {}
monkey_tests = {}
monkey_tests_true = {}
monkey_tests_false = {}

with open(sys.argv[1], 'r') as f:
    current_monkey = None
    for raw_line in f:
        line = raw_line.strip()
        if line.startswith('Monkey'):
            current_monkey = int(line.split(' ')[1].strip(':'))
        elif line.startswith('Starting items'):
            monkey_items[current_monkey] = [int(item) for item in line.split(': ')[1].split(', ')]
        elif line.startswith('Operation'):
            important_part = line.split(' old ')[1]
            number = important_part.split(' ')[1]
            if '*' in important_part:
                if number == 'old':
                    monkey_operations[current_monkey] = lambda x: x * x
                else:
                    monkey_operations[current_monkey] = lambda x, number=number: x * int(number)
            elif '+' in important_part:
                if number == 'old':
                    monkey_operations[current_monkey] = lambda x: x + x
                else:
                    monkey_operations[current_monkey] = lambda x, number=number: x + int(number)
        elif line.startswith('Test'):
            number = int(line.split('divisible by ')[1])
            monkey_tests[current_monkey] = lambda x, number=number: x % number == 0
        elif line.startswith('If true'):
            monkey_tests_true[current_monkey] = int(line.split('throw to monkey ')[1])
        elif line.startswith('If false'):
            monkey_tests_false[current_monkey] = int(line.split('throw to monkey ')[1])

monkey_inspections = defaultdict(int)
for round in range(20):
    print(f'Round {round+1}')
    for monkey_idx in range(len(monkey_items)):
        for item in monkey_items[monkey_idx]:
            monkey_inspections[monkey_idx] += 1
            new_worry_level = monkey_operations[monkey_idx](item)
            bored_worry_level = int(new_worry_level / 3)
            if monkey_tests[monkey_idx](bored_worry_level):
                new_monkey_idx = monkey_tests_true[monkey_idx]
            else:
                new_monkey_idx = monkey_tests_false[monkey_idx]
            monkey_items[new_monkey_idx].append(bored_worry_level)
        monkey_items[monkey_idx] = []

    print(f'End of Round {round+1}')
    for monkey_idx, items in monkey_items.items():
        print(f'Monkey {monkey_idx}: {items}')

print('INSPECTIONS:')
for monkey_idx, count in monkey_inspections.items():
    print(f'Monkey {monkey_idx}: {count}')

monkey_business = sorted(monkey_inspections.values())
print(monkey_business[-1]*monkey_business[-2])
