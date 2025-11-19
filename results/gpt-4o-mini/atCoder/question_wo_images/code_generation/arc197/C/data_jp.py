import sys
import bisect

input = sys.stdin.read
data = input().splitlines()

Q = int(data[0])
queries = [tuple(map(int, line.split())) for line in data[1:Q + 1]]

S = []
deleted_multiples = set()

for A, B in queries:
    # Remove multiples of A from S
    if A not in deleted_multiples:
        deleted_multiples.add(A)
        # Generate new elements to add to S
        new_elements = []
        for i in range(1, 10**6):  # Generate a reasonable number of elements
            candidate = i
            if candidate % A != 0:
                new_elements.append(candidate)
            if len(new_elements) >= B + 10:  # Generate enough elements
                break
        S.extend(new_elements)
        S = sorted(set(S))  # Keep S unique and sorted

    # Output the B-th smallest element
    print(S[B - 1])