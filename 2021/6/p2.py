fishes = {i: 0 for i in range(8+1)}
with open('input.txt') as f:
    for line in f:
        for fish in line.strip().split(','):
            fishes[int(fish)] += 1

print(fishes)
print(sum(fishes.values()))

for day in range(256):
    next = {i: 0 for i in range(8+1)}
    for state in range(8+1):
        if state == 0:
            next[8] += fishes[state]
            next[6] += fishes[state]
        else:
            next[state-1] += fishes[state]
    fishes = next
    print(f'Day #{day}: {sum(fishes.values())}')

