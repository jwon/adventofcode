result = 0
with open('input.txt', 'r') as f:
    group = []
    for line in f:
        group.append(set(line.strip()))
        if len(group) >= 3:
            # print(group)
            for item in group[0].intersection(group[1]).intersection(group[2]):
                # print(item)
                offset = 38 if item.isupper() else 96
                result += ord(item)-offset
            group = []
print(result)
