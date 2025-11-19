from itertools import permutations

A = list(map(int, input().split()))

for perm in permutations(A):
    if perm[0] * perm[1] == perm[2]:
        print("Yes")
        exit()

print("No")