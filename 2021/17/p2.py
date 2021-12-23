with open('input.txt') as f:
    [first_half, second_half] = [i.split('..') for i in f.readlines()[0].strip().split(',')]
    x_min = int(first_half[0].split('x=')[1])
    x_max = int(first_half[1])
    y_min = int(second_half[0].split('y=')[1])
    y_max = int(second_half[1])

print(f'x_min: {x_min} x_max: {x_max} y_min: {y_min} y_max: {y_max}')

correct_initial_velocities = set()
for potential_x_velocity in range(x_max+1):
    for potential_y_velocity in range(y_min, abs(y_min)):
        potential_velocity = (potential_x_velocity, potential_y_velocity)
        if potential_velocity in correct_initial_velocities:
            continue
        x, y = 0, 0
        x_vel, y_vel = potential_velocity
        # print(f'Starting at {(x, y)} with velocity {potential_velocity}')
        while x < x_max and y > y_min:
            x += x_vel
            y += y_vel
            if x_vel > 0:
                x_vel -= 1
            elif x_vel < 0:
                x_vel += 1
            y_vel -= 1
            # print(f'Pos: {(x, y)} Vel: {(x_vel, y_vel)}')
            if x_min <= x <= x_max and y_min <= y <= y_max:
                print(f'TARGET REACHED! initial velocity: {potential_velocity}')
                correct_initial_velocities.add(potential_velocity)
                break

print(len(correct_initial_velocities))
