CHUNK_MAP = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

SCORE_MAP = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

error_scores = []
with open('input.txt') as f:
    for line in f:
        corrupted = False
        stack = []
        for char in line.strip():
            if char in CHUNK_MAP:
                stack.append(char)
            elif CHUNK_MAP[stack.pop()] == char:
                continue
            else:    
                corrupted = True
                break
        if not corrupted and len(stack) != 0:
            score = 0
            for i in range(1, len(stack)+1):
                score = score * 5 + SCORE_MAP[stack[i*-1]]
            error_scores.append(score)
                
print(sorted(error_scores)[len(error_scores) // 2])
