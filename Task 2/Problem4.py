pattern = input().strip()
genome = input().strip()

result = []

for i in range(len(genome) - len(pattern) + 1):
    if genome[i:i + len(pattern)] == pattern:
        result.append(str(i))

print(" ".join(result))
