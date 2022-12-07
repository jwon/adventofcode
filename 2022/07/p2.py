from collections import defaultdict


dir_sizes = defaultdict(int)
current_path = []
with open('input.txt', 'r') as f:
    for line in f:
        # print(line.strip())
        if line.startswith('$ cd '):
            arg = line.strip().split('$ cd ')[1]
            if arg == '..':
                current_path.pop()
            else:
                current_path.append(arg)
            # print(current_path)
        elif line.startswith('$ ls') or line.startswith('dir'):
            continue
        else:
            size = int(line.split(' ')[0])
            for idx in range(len(current_path)):
                dir_sizes[tuple(current_path[:idx+1])] += size
            # print(dir_sizes)

TOTAL_DISK_SPACE = 70_000_000
NEED_SPACE = 30_000_000
unused_space = TOTAL_DISK_SPACE - dir_sizes[('/',)]
need_to_free = NEED_SPACE - unused_space
# print(need_to_free)

for size in sorted(dir_sizes.values()):
    if size > need_to_free:
        print(size)
        break
