n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

buk = list()
for i in range(n + 2):
    buk.append(list())

for i in range(n):
    buk[B[i]].append(A[i])

dlt = sum(B)
ans = 0

for i in range(n + 1):
    if len(buk[i]):
        dp = [1] * len(buk[i])
        for j in range(len(buk[i])):
            for k in range(j):
                if buk[i][j] > buk[i][k]:
                    dp[j] = max(dp[j], dp[k] + 1)
        ans += i * max(dp)

print(dlt - ans)