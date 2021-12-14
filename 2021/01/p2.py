depths = []
with open('input.txt') as f:
    for line in f:
        depths.append(int(line.strip()))

increased_count = 0
for i in range(len(depths) - 3):
    prev_window = depths[i] + depths[i+1] + depths[i+2]
    next_window = depths[i+1] + depths[i+2] + depths[i+3]
    if next_window > prev_window:
        increased_count += 1

print(increased_count)
