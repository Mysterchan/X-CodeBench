from itertools import permutations

A = list(map(int, input().split()))
for B in permutations(A):
    if B[0] * B[1] == B[2]:
        print("Yes")
        break
else:
    print("No")