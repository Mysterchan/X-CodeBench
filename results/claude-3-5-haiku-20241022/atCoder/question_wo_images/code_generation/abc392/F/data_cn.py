N = int(input())
P = list(map(int, input().split()))

A = []
for i in range(1, N + 1):
    A.insert(P[i-1] - 1, i)

print(' '.join(map(str, A)))