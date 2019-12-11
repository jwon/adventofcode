PUZZLE_INPUT = '284639-748759'


def is_valid_password(password):
    digits = [int(x) for x in str(password)]
    adjacent_found = False
    last_unique_digit_seen = None
    disqualified = False
    found_match = True
    for i in range(len(digits)):
        current_digit = digits[i]
        if last_unique_digit_seen is None:
            last_unique_digit_seen = current_digit
            continue

        if current_digit == last_unique_digit_seen:
            if disqualified:
                continue

            if adjacent_found:
                disqualified = True
            else:
                adjacent_found = True
        elif current_digit < last_unique_digit_seen:
            return False
        else:  # current_digit > last_unique_digit_seen
            if adjacent_found:
                found_match = True

            last_unique_digit_seen = current_digit
            adjacent_found = False
            if disqualified:
                disqualified = False

    return found_match or not disqualified


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
