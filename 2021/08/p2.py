from itertools import product

with open('input.txt') as f:
    total = 0
    for line in f:
        letters_to_digit = {}
        digit_to_letters = {}
        six_segments = set()
        five_segments = set()
        tokens = line.strip().split(' ')
        for token in tokens:
            key = frozenset(token)
            if token == '|':
                continue
            elif len(key) == 2:
                letters_to_digit[key] = '1'
                digit_to_letters['1'] = key
            elif len(key) == 4:
                letters_to_digit[key] = '4'
                digit_to_letters['4'] = key
            elif len(key) == 3:
                letters_to_digit[key] = '7'
                digit_to_letters['7'] = key
            elif len(key) == 7:
                letters_to_digit[key] = '8'
                digit_to_letters['8'] = key
            elif len(token) == 6: # 0, 6, or 9
                six_segments.add(key)
            elif len(token) == 5: # 2, 3, or 5
                five_segments.add(key)

        # identify 3, 9, 5, 6
        while len(letters_to_digit) < 8:
            for five_segment, six_segment in product(five_segments, six_segments):
                if five_segment.issubset(six_segment):
                    # Can be (3 and 9) or (5 and 6)
                    if digit_to_letters['1'].issubset(five_segment):
                        # Must be 3 and 9
                        letters_to_digit[five_segment] = '3'
                        digit_to_letters['3'] = five_segment
                        letters_to_digit[six_segment] = '9'
                        digit_to_letters['9'] = six_segment
                        break
                    elif '3' in digit_to_letters: # don't identify 5 and 6 until 3 and 9 are found
                        letters_to_digit[five_segment] = '5'
                        digit_to_letters['5'] = five_segment
                        letters_to_digit[six_segment] = '6'
                        digit_to_letters['6'] = six_segment
                        break
            five_segments = [i for i in five_segments if i not in letters_to_digit]
            six_segments = [i for i in six_segments if i not in letters_to_digit]

        # if len(letters_to_digit) == 8:
        #     for digit in sorted(digit_to_letters):
        #         print(f'{digit}: {sorted(digit_to_letters[digit])}')
        
        # decode output value
        output_value = ''
        for token in tokens[11:]:
            key = frozenset(token)
            if key in letters_to_digit:
                digit = letters_to_digit[key]
            elif len(key) == 5:
                digit = '2'
            elif len(key) == 6:
                digit = '0'
            output_value += digit
        print(output_value)
        total += int(output_value)
    print(f'TOTAL: {total}')
