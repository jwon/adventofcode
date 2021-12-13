caves = {}
with open('input.txt') as f:
    for line in f:
        cave, connected_to = line.strip().split('-')
        if cave in caves:
            caves[cave].add(connected_to)
        else:
            caves[cave] = {connected_to}
        if connected_to in caves:
            caves[connected_to].add(cave)
        else:
            caves[connected_to] = {cave}

def traverse(current_cave, path=None, cannot_visit_again=None, second_visit_available=True):
    cannot_visit_again = set() if cannot_visit_again is None else set(cannot_visit_again)
    path = [] if path is None else list(path)
    path.append(current_cave)
    if current_cave == 'end':
        print(",".join(path))
        return 1
    if current_cave.islower():
        cannot_visit_again.add(current_cave)

    total_paths = 0
    for cave in caves[current_cave]:
        if cave not in cannot_visit_again:
            total_paths += traverse(cave, path=path, cannot_visit_again=cannot_visit_again, second_visit_available=second_visit_available)
        else:
            if second_visit_available and cave.islower() and cave != 'start':
                total_paths += traverse(cave, path=path, cannot_visit_again=cannot_visit_again, second_visit_available=False)
    return total_paths

print(traverse('start'))
