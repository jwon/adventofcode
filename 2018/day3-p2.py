def parse_fields(line):
    result = {}
    fields = line.split()
    result['id'] = int(fields[0].split('#')[1])
    edges = fields[2].split(':')[0].split(',')
    result['left_edge'] = int(edges[0])
    result['top_edge'] = int(edges[1])
    size = fields[3].split('x')
    result['width'] = int(size[0])
    result['height'] = int(size[1])

    return result


fabric = [[[] for x in range(1000)] for y in range(1000)]

potential_ids = []
with open('inputs/3.txt', 'r') as f:
    for line in f:
        claim = parse_fields(line)
        # print(claim)
        potential_ids.append(claim['id'])
        for i in range(claim['width']):
            for j in range(claim['height']):
                fabric[claim['left_edge'] + i][claim['top_edge'] + j].append(claim['id'])

for i in range(len(fabric)):
    for j in range(len(fabric[i])):
        if len(fabric[i][j]) > 1:
            for claim_id in fabric[i][j]:
                if claim_id in potential_ids:
                    potential_ids.remove(claim_id)

print(f'ANSWER: {potential_ids}')
