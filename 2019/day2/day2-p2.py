from itertools import permutations


def run_program(instructions, noun, verb):
    instructions = instructions.copy()
    instructions[1] = noun
    instructions[2] = verb

    for i in range(0, len(instructions), 4):
        opcode = instructions[i]
        if opcode == 99:
            return instructions[0]
        param1 = instructions[i + 1]
        param2 = instructions[i + 2]
        param3 = instructions[i + 3]
        # print(f'{opcode} {param1} {param2} {param3}')
        if opcode == 1:
            instructions[param3] = instructions[param1] + instructions[param2]
        elif opcode == 2:
            instructions[param3] = instructions[param1] * instructions[param2]
        else:
            print(f'Invalid opcode: {opcode}')
            exit(1)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        for line in f:
            instructions = [int(i) for i in line.strip().split(',')]

    TARGET = 19690720

    search_space = len(instructions)
    for noun, verb in permutations(range(search_space), 2):
        print(f'Trying noun={noun} verb={verb} ...')
        output = run_program(instructions, noun, verb)
        print(f'GOT: {output} TARGET: {TARGET}')
        if output == TARGET:
            solution = 100 * noun + verb
            print(f'FOUND IT: {solution}')
            exit()
