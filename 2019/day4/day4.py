PUZZLE_INPUT = '284639-748759'


def is_valid_password(password):
    digits = [int(x) for x in str(password)]
    adjacent_found = False
    for i in range(len(digits)-1):
        if digits[i] == digits[i+1]:
            adjacent_found = True

        if digits[i+1] < digits[i]:
            return False

    return adjacent_found


if __name__ == '__main__':
    # Tests
    print(is_valid_password(111111))
    print(is_valid_password(223450))
    print(is_valid_password(123789))
    start, end = (int(i) for i in PUZZLE_INPUT.split('-'))

    valid_password_count = 0
    for i in range(start, end+1):
        if is_valid_password(i):
            valid_password_count += 1

    print(valid_password_count)
