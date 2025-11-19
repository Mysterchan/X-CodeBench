A = list(map(int, input().split()))

from itertools import permutations

found = False
for perm in permutations(A):
    if perm[0] * perm[1] == perm[2]:
        found = True
        break

print("Yes" if found else "No")