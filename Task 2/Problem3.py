pattern = input().strip()

complement = {
    'A' : 'T',
    'T' : 'A',
    'C' : 'G',
    'G' : 'C'
}

reverse_complement = ""

for nucleotide in reversed(pattern):
    reverse_complement += complement[nucleotide]

print(reverse_complement)
