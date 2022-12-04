result = 0
with open('input.txt', 'r') as f:
    for line in f:
        rucksack = line.strip()
        separator_idx = int(len(rucksack)/2)
        first_compartment = set(rucksack[:separator_idx])
        second_compartment = set(rucksack[separator_idx:])

        for item in first_compartment.intersection(second_compartment):
            offset = 38 if item.isupper() else 96
            result += ord(item)-offset

print(result)
