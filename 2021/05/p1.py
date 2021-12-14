from collections import Counter


points = []
with open('input.txt') as f:
    for line in f:
        start, end = line.strip().split(' -> ')
        x1, y1 = (int(i) for i in start.split(','))
        x2, y2 = (int(i) for i in end.split(','))
        if x1 == x2:
            step = 1 if y1 < y2 else -1
            points.extend([(x1, i) for i in range(y1, y2+step, step)])
        elif y1 == y2:
            step = 1 if x1 < x2 else -1
            points.extend([(i, y1) for i in range(x1, x2+step, step)])
    print(f'len(points): {len(points)}')
    c = Counter(points)
    print(sum(1 for _, count in c.most_common() if count >= 2))
