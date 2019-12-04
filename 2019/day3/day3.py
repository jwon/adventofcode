def find_intersection_distance(lines):
    wire_paths = []
    for line in lines:
        wire_path = [(0, 0)]
        for direction_steps in line.strip().split(','):
            direction = direction_steps[0]
            steps = int(direction_steps[1:])
            # print(f'direction: {direction} steps: {steps}')
            for _ in range(steps):
                previous_x, previous_y = wire_path[-1]
                if direction == 'R':
                    next_step = (previous_x+1, previous_y)
                elif direction == 'L':
                    next_step = (previous_x-1, previous_y)
                elif direction == 'U':
                    next_step = (previous_x, previous_y-1)
                elif direction == 'D':
                    next_step = (previous_x, previous_y+1)
                else:
                    raise Exception(f'Unknown direction: {direction}')

                wire_path.append(next_step)
        wire_paths.append(wire_path)
        # print(wire_paths)

    # Create a set for each wire
    # Exclude central port (0,0)
    first_wire_path = set(wire_paths[0][1:])
    second_wire_path = set(wire_paths[1][1:])

    # find intersections
    intersections = first_wire_path.intersection(second_wire_path)

    # find shortest intersection
    shortest_distance = None
    for intersection in intersections:
        distance = abs(intersection[0]) + abs(intersection[1])
        if shortest_distance is None:
            shortest_distance = distance
        elif distance < shortest_distance:
            shortest_distance = distance

    return shortest_distance


if __name__ == '__main__':
    print(find_intersection_distance(['R8,U5,L5,D3', 'U7,R6,D4,L4']))
    print(find_intersection_distance(['R75,D30,R83,U83,L12,D49,R71,U7,L72',
                                      'U62,R66,U55,R34,D71,R55,D58,R83']))
    print(find_intersection_distance(['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
                                      'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7']))
    with open('input.txt', 'r') as f:
        print(find_intersection_distance(f))
