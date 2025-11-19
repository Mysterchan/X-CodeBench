import sys
from bisect import bisect_left

input = sys.stdin.read
data = input().split()

Q = int(data[0])
queries = [(int(data[i * 2 + 1]), int(data[i * 2 + 2])) for i in range(Q)]

# Use a set to keep track of removed multiples efficiently
removed_multiples = set()
max_b = max(b for _, b in queries)

# The resulting sequence without multiples, at worst we need the first max_b numbers
result_sequence = []

# Pre-fill the result_sequence with numbers 1 to a reasonable limit
for i in range(1, 300000):  # 300000 should provide us enough values for B_i
    if i not in removed_multiples:
        result_sequence.append(i)

# Process queries
output = []
for a, b in queries:
    if a in removed_multiples:
        output.append(result_sequence[b - 1])
        continue
    
    # Remove multiples of a from sequence
    multiple = a
    while multiple < len(result_sequence) + 1:
        if multiple in removed_multiples:
            multiple += a
            continue
        removed_multiples.add(multiple)
        multiple += a
    
    # Sort removed_multiples assuming they won't get extremely large, 
    # now we find the b-th smallest.
    output.append(result_sequence[b - 1])
    
# Print all results
print('\n'.join(map(str, output)))