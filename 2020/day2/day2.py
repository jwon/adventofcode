from collections import Counter


with open('input.txt') as f:
    valid_passwords_count = 0
    for line in f:
        policy, password = line.strip().split(': ')
        occurences, letter = policy.split(' ')
        lower_limit, upper_limit = (int(x) for x in occurences.split('-'))
        counts = Counter(password)
        letter_count = counts[letter]
        print(f'Password: {password} Letter: {letter} count: {letter_count} lower_limit: {lower_limit} upper_limit: {upper_limit}')
        if lower_limit <= counts[letter] <= upper_limit:
            print('Password is VALID')
            valid_passwords_count += 1
        else:
            print('Password is INVALID')

print(f'Valid Passwords count: {valid_passwords_count}')
