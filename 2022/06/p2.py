with open('input.txt', 'r') as f:
    for line in f:
        for i in range(len(line)):
            if len(set(line[i:i+14])) == 14:
                print(i+14)
                break
