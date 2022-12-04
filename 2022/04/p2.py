assignments = []
with open('input.txt', 'r') as f:
    for line in f:
        assignments.append([
                [int(x) for x in assignment.split('-')]
                for assignment in line.strip().split(',')
        ])

    result = 0
    for [first, second] in assignments:
        first_set = set(range(first[0], first[1]+1))
        second_set = set(range(second[0], second[1]+1))
        if len(first_set.intersection(second_set)) > 0 or len(second_set.intersection(first_set)) > 0:
            result += 1

    print(result)
