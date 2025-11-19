from copy import deepcopy

n, q = map(int,input().split())
s = list()
for _ in range(n):
    s.append(list(input()))
s_score = list()
for _ in range(n - 1):
    s_score.append([0] * (n - 1))

for row in range(n - 1):
    for col in range(n - 1):
        if s[row][col] == s[row][col + 1] == s[row + 1][col] == s[row + 1][col + 1] == ".":
            s_score[row][col] += 1

s_score_imos = deepcopy(s_score)
for i in range(len(s_score_imos)):
    for j in range(1, len(s_score_imos[i])):
        s_score_imos[i][j] += s_score_imos[i][j - 1]

for _ in range(q):
    u, d, l, r = map(int,input().split())
    u -= 1
    d -= 1
    l -= 1
    r -= 2
    ans = 0
    for row in range(u, d):
        if l == 0:
            ans += s_score_imos[row][r]
        else:
            ans += s_score_imos[row][r] - s_score_imos[row][l - 1]
    print(ans)