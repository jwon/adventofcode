with open('input.txt', 'r') as f:
    for line in f:
        for i in range(len(line)):
            if len(set(line[i:i+4])) == 4:
                print(i+4)
                break
