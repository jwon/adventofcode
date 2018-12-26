from collections import Counter

with open('inputs/2.txt', 'r') as f:
    num_two_ids = 0
    num_three_ids = 0
    for line in f:
        frequencies = Counter(line.strip())
        values = frequencies.values()
        if 2 in values:
            num_two_ids += 1
        if 3 in values:
            num_three_ids += 1

    print(num_two_ids * num_three_ids)
