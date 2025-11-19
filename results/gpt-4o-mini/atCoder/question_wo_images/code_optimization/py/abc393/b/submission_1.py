S = input().strip()
ans = 0
n = len(S)

# Precompute the positions of A, B, and C
A_positions = []
B_positions = []
C_positions = []

for index, char in enumerate(S):
    if char == 'A':
        A_positions.append(index)
    elif char == 'B':
        B_positions.append(index)
    elif char == 'C':
        C_positions.append(index)

# Now we will count valid (i, j, k) triples
for j in B_positions:
    # For each B, find A's before it and C's after it
    for i in A_positions:
        if i < j:
            # Calculate the required k position
            k = 2 * j - i
            if k < n and S[k] == 'C':
                ans += 1

print(ans)