floor = 0
with open("input.txt", "r") as f:
    for line in f:
        for index, element in enumerate(line.strip(), start=1):
            # print(element)
            if element == "(":
                floor += 1
            elif element == ")":
                floor -= 1
            else:
                raise Exception(f"Unrecognized element: {element}")

            if floor == -1:
                print(f"The position is {index}")
                break

print(f"The floor is {floor}")
