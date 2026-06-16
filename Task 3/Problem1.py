def mismatch(a, b):
    return sum(x != y for x, y in zip(a,b))

def approximate_pattern_matching(pattern, text, d):
    k = len(pattern)
    positions = []
    
    for i in range(len(text) -k +1):
        window = text[i:i+k]
        
        if mismatch(pattern, window) <= d:
            positions.append(i)
    return positions

pattern = input().strip()
text = input().strip()
d = int(input().strip())

result = approximate_pattern_matching(pattern, text, d)

print(*result)
