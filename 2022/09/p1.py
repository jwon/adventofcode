from collections import namedtuple


Position = namedtuple('Position', ['x', 'y'])
head = Position(0, 0)
prev_head = None
tail = Position(0, 0)
visited = {tail}
with open('input.txt', 'r') as f:
    for motion in f:
        direction, count = motion.strip().split(' ')
        for i in range(int(count)):
            # move head
            prev_head = head
            if direction == 'R':
                head = Position(head.x+1, head.y)
            elif direction == 'U':
                head = Position(head.x, head.y-1)
            elif direction == 'L':
                head = Position(head.x-1, head.y)
            elif direction == 'D':
                head = Position(head.x, head.y+1)
            else:
                print(f'cannot move head. direction unknown: {direction}')

            # move tail if necessary
            if abs(tail.x - head.x) > 1 and abs(tail.y - head.y) > 1:  # diagonal
                tail = prev_head
            elif abs(tail.x - head.x) > 1 or abs(tail.y - head.y) > 1:  # adjacent
                tail = prev_head
            visited.add(tail)

            # print(f'head: {head}')
            # print(f'prev_head: {prev_head}')
            # print(f'tail: {tail}')
            # print(f'visited: {visited}')


print(len(visited))
