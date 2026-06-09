text = input().strip()
k = int(input())

frequency = {}

for i in range(len(text) - k + 1):
    pattern = text[i:i+k]
    frequency[pattern] = frequency.get(pattern, 0) + 1

max_count = max(frequency.values())

result = []

for pattern, count in frequency.items():
        if count == max_count:
            result.append(pattern)

print(*result)
