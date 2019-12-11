from collections import Counter


PUZZLE_INPUT = '284639-748759'


def is_valid_password(password):
    password_string = str(password)
    digits = [int(x) for x in password_string]
    if len(digits) != 6:
        return False
    for i in range(len(digits)-1):
        current_digit = digits[i]
        next_digit = digits[i+1]
        if current_digit > next_digit:
            return False

    counter = Counter(password_string)
    for digit, count in counter.items():
        if count == 2 and digit+digit in password_string:
            return True
    return False


def print_is_valid_password(password):
    print(f'{password}: {is_valid_password(password)}')


if __name__ == '__main__':
    # Tests
    print_is_valid_password(111111)
    print_is_valid_password(223450)
    print_is_valid_password(223456)
    print_is_valid_password(123789)
    print_is_valid_password(112233)
    print_is_valid_password(123444)
    print_is_valid_password(111122)
    print_is_valid_password(112222)
    start, end = (int(i) for i in PUZZLE_INPUT.split('-'))

    valid_password_count = 0
    for i in range(start, end+1):
        if is_valid_password(i):
            valid_password_count += 1

    print(valid_password_count)
