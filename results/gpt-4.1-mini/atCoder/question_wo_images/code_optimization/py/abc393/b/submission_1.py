S = input()
n = len(S)
ans = 0
for i in range(n):
    if S[i] == 'B':
        max_d = min(i, n - i - 1)
        for d in range(1, max_d + 1):
            if S[i - d] == 'A' and S[i + d] == 'C':
                ans += 1
print(ans)