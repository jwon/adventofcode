gamma_rate = ''
epsilon_rate = ''

with open('input.txt') as f:
    total_lines = 0
    ones_seen = None
    for line in f:
        binary_string = line.strip()
        if ones_seen is None:
            ones_seen = [0] * len(binary_string)
        total_lines += 1
        for i in range(len(ones_seen)):
            if binary_string[i] == '1':
                ones_seen[i] += 1

    common_threshold = total_lines / 2
    print(ones_seen)
    for count in ones_seen:
        if count > common_threshold:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    print(gamma_rate)
    print(epsilon_rate)
    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
    print(power_consumption)
