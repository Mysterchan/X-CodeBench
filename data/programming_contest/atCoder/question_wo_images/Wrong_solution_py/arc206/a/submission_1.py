N = int(input())
A = list(map(int, input().split()))

cnt = 1
seen = {A[0] : 1}
for i in range(1, N):
    if A[i] == A[i-1]:
        seen[A[i]] += 1
        continue
    seen.setdefault(A[i], 0)
    cnt += i - seen[A[i]]
    seen[A[i]] += 1
print(cnt)