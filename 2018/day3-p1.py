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


fabric = [[0 for x in range(1000)] for y in range(1000)]

with open('inputs/3.txt', 'r') as f:
    for line in f:
        claim = parse_fields(line)
        # print(claim)
        for i in range(claim['width']):
            for j in range(claim['height']):
                fabric[claim['left_edge'] + i][claim['top_edge'] + j] += 1

count = 0
for i in range(len(fabric)):
    for j in range(len(fabric[i])):
        if fabric[i][j] > 1:
            count += 1

print(count)
