if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        for line in f:
            program = [int(i) for i in line.strip().split(',')]

    program[1] = 12
    program[2] = 2

    for i in range(0, len(program), 4):
        opcode = program[i]
        if opcode == 99:
            print(program)
            print(f'Position 0: {program[0]}')
            exit()
        pos1 = program[i + 1]
        pos2 = program[i + 2]
        pos3 = program[i + 3]
        print(f'{opcode} {pos1} {pos2} {pos3}')
        if opcode == 1:
            program[pos3] = program[pos1] + program[pos2]
        elif opcode == 2:
            program[pos3] = program[pos1] * program[pos2]
        else:
            print(f'Invalid opcode: {opcode}')
            exit(1)
