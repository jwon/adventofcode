from pprint import pprint


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

pprint(caves)

def traverse(current_cave, path=None, cannot_visit_again=None):
    cannot_visit_again = set() if cannot_visit_again is None else set(cannot_visit_again)
    path = [] if path is None else list(path)
    path.append(current_cave)
    if current_cave.islower():
        cannot_visit_again.add(current_cave)
    if current_cave == 'end':
        print(f'FOUND PATH: {path}')
        return 1
    potential_caves = caves[current_cave] - cannot_visit_again
    if potential_caves != set():
        return sum(traverse(cave, path=path, cannot_visit_again=cannot_visit_again) for cave in potential_caves)
    else:
        return 0

print(traverse('start'))
