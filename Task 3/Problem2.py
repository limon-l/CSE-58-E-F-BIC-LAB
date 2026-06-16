def hamming_distance(a, b):
    return sum(x != y for x, y in zip(a, b))


def frequent_words_with_mismatches(text, k, d):
    n = len(text)
    freq = {}

    for i in range(n - k + 1):
        pattern = text[i:i+k]
        freq[pattern] = 0

    for pattern in freq:
        for i in range(n - k + 1):
            if hamming_distance(pattern, text[i:i+k]) <= d:
                freq[pattern] += 1

    max_count = max(freq.values())
    return sorted([p for p, c in freq.items() if c == max_count])


text = input().strip()
k, d = map(int, input().split())

print(" ".join(frequent_words_with_mismatches(text, k, d)))
