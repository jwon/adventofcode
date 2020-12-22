with open('input.txt') as f:
    valid_passwords_count = 0
    for line in f:
        policy, password = line.strip().split(': ')
        indexes, letter = policy.split(' ')
        characters = [password[int(x)-1] for x in indexes.split('-')]
        if sum(character == letter for character in characters) == 1:
            print(f'Password {password} is VALID')
            valid_passwords_count += 1
        else:
            print(f'Password {password} is INVALID')

print(f'Valid Passwords count: {valid_passwords_count}')
