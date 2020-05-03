answer = 0
with open("input.txt", "r") as f:
    for line in f:
        for element in line.strip():
            # print(element)
            if element == "(":
                answer += 1
            elif element == ")":
                answer -= 1
            else:
                raise Exception(f"Unrecognized element: {element}")

print(f"The answer is {answer}")
