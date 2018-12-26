from itertools import permutations

with open('inputs/2.txt', 'r') as f:
    for id1, id2 in permutations(f, 2):
        print(f'id1: {id1.strip()} id2: {id2.strip()}')
        id_length = len(id1.strip())
        candidate = False
        common_letters = ''
        for i in range(id_length):
            if id1[i] != id2[i]:
                # print(f'compare: {id1[i]} != {id2[i]}')
                if candidate:  # if second time seeing letters that differ
                    # print('Second time seeing differing letters. Moving to next permutation')
                    break
                else:  # if first time seeing letters that differ
                    # print(f'First time seeing differing letters')
                    candidate = True
            else:
                common_letters += id1[i]

        if candidate and len(common_letters) == id_length - 1:
            print(f'Common letters: {common_letters}')
            break
