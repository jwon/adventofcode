from collections import Counter


pair_counts = None
rules = {}
with open('input.txt') as f:
    for line in f:
        if not pair_counts:
            chars = list(line.strip())
            letter_counts = Counter(chars)
            pair_counts = Counter([(chars[i], chars[i+1]) for i in range(len(chars)-1)])
        elif ' -> ' in line:
            pattern, insert = line.strip().split(' -> ')
            rules[tuple(pattern)] = insert

print(pair_counts)
# print(rules)
            
for step in range(40):
    new_counts = Counter()
    for pair, count in pair_counts.most_common():
        to_add = []
        if pair in rules:
            letter_to_add = rules[pair]
            to_add.append((pair[0], letter_to_add))
            to_add.append((letter_to_add, pair[1]))
            letter_counts[letter_to_add] += count
        else:
            to_add.append(pair)
        for pair in to_add:
            new_counts[pair] += count

    counts = letter_counts.most_common()
    answer = counts[0][1] - counts[-1][1]
    
    print(f'After step {step+1}: {answer}')
    pair_counts = new_counts
