N, M = map(int, input().split())
S = list(input().strip())
T = list(input().strip())

# Convert T to a list of characters and sort indices by digit value
replacements = sorted(range(M), key=lambda x: T[x], reverse=True)

# Pointer for the position in S to replace
j = 0

# Traverse the sorted replacements
for idx in replacements:
    # If j is within bounds and we can make a replacement
    if j < N and T[idx] > S[j]:
        S[j] = T[idx]
        j += 1  # Move to the next position in S if replacement was made

# Output the resulting string as an integer
print(''.join(S))