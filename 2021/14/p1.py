from collections import Counter


polymer_template = []
rules = {}
with open('input.txt') as f:
    for line in f:
        if not polymer_template:
            polymer_template = line.strip()
        elif ' -> ' in line:
            pattern, insert = line.strip().split(' -> ')
            rules[tuple(pattern)] = insert

print(polymer_template)
# print(rules)
            
for step in range(10):
    new_template = []
    for i in range(len(polymer_template)-1):
        pair = (polymer_template[i], polymer_template[i+1])
        if pair in rules:
            new_template.extend([pair[0], rules[pair]])
    new_template.append(polymer_template[-1])

    counts = Counter(new_template).most_common()
    answer = counts[0][1] - counts[-1][1]
    
    print(f'After step {step+1}: {answer}')
    polymer_template = new_template
