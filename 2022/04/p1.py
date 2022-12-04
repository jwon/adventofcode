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
        if first_set.intersection(second_set) == first_set or second_set.intersection(first_set) == second_set:
            result += 1

    print(result)
