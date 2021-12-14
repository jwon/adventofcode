easy_digits_count = 0
with open('input.txt') as f:
    for line in f:
        tokens = line.strip().split(' ')
        easy_digits_count += sum(1 for token in tokens[11:] if len(token) in [2, 4, 3, 7])

print(easy_digits_count)
