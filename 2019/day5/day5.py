from itertools import permutations


def run_program(instructions, input_var):
    instructions = instructions.copy()

    instruction_pointer = 0
    while instruction_pointer < len(instructions):
        param0 = str(instructions[instruction_pointer])
        opcode = int(param0[-2:])
        if opcode == 99:
            return instructions[0]
        # print(f'{opcode} {param1} {param2} {param3}')
        if opcode == 1:
            param1 = instructions[instruction_pointer + 1]
            param2 = instructions[instruction_pointer + 2]
            param3 = instructions[instruction_pointer + 3]
            instructions[param3] = instructions[param1] + instructions[param2]
            instruction_pointer += 4
        elif opcode == 2:
            param1 = instructions[instruction_pointer + 1]
            param2 = instructions[instruction_pointer + 2]
            param3 = instructions[instruction_pointer + 3]
            instructions[param3] = instructions[param1] * instructions[param2]
            instruction_pointer += 4
        elif opcode == 3:
            param1 = instructions[instruction_pointer + 1]
            instructions[param1] = input_var
            instruction_pointer += 2
        elif opcode == 4:
            param1 = instructions[instruction_pointer + 1]
            print(f'Pointer: {instruction_pointer} Value: {instructions[param1]}')
            instruction_pointer += 2
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
