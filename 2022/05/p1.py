from collections import deque

stacks = None
with open('input.txt', 'r') as f:
    for line in f:
        if line.startswith('move'):
            [_, how_many, _, from_crate_idx, _, to_crate_idx] = line.split(' ')
            # print(f'{how_many} {from_crate_idx} {to_crate_idx}')
            for i in range(int(how_many)):
                stacks[int(to_crate_idx)-1].appendleft(stacks[int(from_crate_idx)-1].popleft())
            # print(stacks)
        elif line == '\n' or '[' not in line:
            pass
        else:
            if stacks is None:
                stacks = [deque() for _ in range(int(len(line)/4))]
                # print(stacks)
            for idx, crate_idx in enumerate(range(1, len(line), 4), 1):
                crate_value = line[crate_idx]
                # print(f'{idx}: {crate_value}')
                if crate_value != ' ':
                    stacks[idx-1].append(crate_value)
    print(''.join(stack.popleft() for stack in stacks))
