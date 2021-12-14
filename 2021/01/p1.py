current_depth = None
increased_count = 0
with open('input.txt') as f:
    for line in f:
        depth = int(line.strip())
        if current_depth is not None:
            if depth > current_depth:
                increased_count += 1
        current_depth = depth

print(increased_count)
