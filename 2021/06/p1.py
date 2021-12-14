with open('input.txt') as f:
    for line in f:
        fishes = [int(fish) for fish in line.strip().split(',')]

print(fishes)
print(len(fishes))

def run_day(fishes):
    result = []
    for fish in fishes:
        if fish == 0:
            result.extend([6, 8])
        else:
            result.append(fish-1)

    return result

for day in range(80):
    fishes = run_day(fishes)
    print(f'Day #{day}: {len(fishes)}')

