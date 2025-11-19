S = input()
n = len(S)

# Precompute positions of A, B, C
pos_A = set()
pos_B = []
pos_C = set()

for i in range(n):
    if S[i] == 'A':
        pos_A.add(i)
    elif S[i] == 'B':
        pos_B.append(i)
    elif S[i] == 'C':
        pos_C.add(i)

ans = 0
for j in pos_B:
    # For each B at position j, check all valid distances
    max_dist = min(j, n - 1 - j)
    for d in range(1, max_dist + 1):
        if (j - d) in pos_A and (j + d) in pos_C:
            ans += 1

print(ans)