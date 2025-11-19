N = int(input())

A = list(map(int, input().split()))

i = j = d = 0

B = [N] * N
jBgn = 1

for i in range(0, N):
    for j in range(jBgn, N):

        if A[j] >= 2 * A[i]:
            B[i] = j
            break

mBi = 0
for i in range(0, N):
    mBi = max(mBi, B[i] - i)
    if i + max(mBi, i) >= N:
        break

print(i)