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

result = 0
for directory, size in dir_sizes.items():
    if size <= 100000:
        result += size
        # print(f'{directory}: {size}')
print(result)
