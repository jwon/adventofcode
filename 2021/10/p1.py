CHUNK_MAP = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

SCORE_MAP = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

total_error_score = 0
with open('input.txt') as f:
    for line in f:
        stack = []
        for char in line.strip():
            if char in CHUNK_MAP:
                stack.append(char)
            elif CHUNK_MAP[stack.pop()] == char:
                continue
            else:    
                print(f'FOUND CORRUPTION: {char} worth {SCORE_MAP[char]} points')
                total_error_score += SCORE_MAP[char] 

print(total_error_score)
