with open('input.txt') as f:
    [first_half, second_half] = [i.split('..') for i in f.readlines()[0].strip().split(',')]
    x_min = int(first_half[0].split('x=')[1])
    x_max = int(first_half[1])
    y_min = int(second_half[0].split('y=')[1])
    y_max = int(second_half[1])

print(f'x_min: {x_min} x_max: {x_max} y_min: {y_min} y_max: {y_max}')

print(sum(i for i in range(abs(y_min))))
