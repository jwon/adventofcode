all_numbers = []
with open('input.txt') as f:
    for line in f:
        all_numbers.append(line.strip())


def filter_numbers(numbers, is_oxygen, index=0):
    print(f'len(numbers): {len(numbers)}')
    if len(numbers) == 1:
        return numbers[0]
    zero_nums = []
    one_nums = []
    for number in numbers:
        if number[index] == '0':
            zero_nums.append(number)
        else:
            one_nums.append(number)
    print(f'len(zero_nums): {len(zero_nums)} len(one_nums): {len(one_nums)}')

    if len(one_nums) >= len(zero_nums):
        if is_oxygen:
            return filter_numbers(one_nums, is_oxygen=is_oxygen, index=index+1)
        else:
            return filter_numbers(zero_nums, is_oxygen=is_oxygen, index=index+1)
    else: # len(zero_nums) > len(one_nums)
        if is_oxygen:
            return filter_numbers(zero_nums, is_oxygen=is_oxygen, index=index+1)
        else:
            return filter_numbers(one_nums, is_oxygen=is_oxygen, index=index+1)

oxygen_generator_rating = filter_numbers(all_numbers, True)
co2_scrubber_rating = filter_numbers(all_numbers, False)
print(oxygen_generator_rating)
print(co2_scrubber_rating)

life_support_rating = int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)
print(life_support_rating)
