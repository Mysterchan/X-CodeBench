N, K = map(int, input().split())

visit = [[0] * N for _ in range(N)]

for _ in range(K-1):
    i, j = 0, 0
    while (i, j) != (N-1, N-1):
        visit[i][j] += 1
        if i == N-1:
            j += 1
        elif j == N-1:
            i += 1
        else:
            if visit[i+1][j] < visit[i][j+1]:
                i += 1
            elif visit[i+1][j] > visit[i][j+1]:
                j += 1
            else:
                i += 1
    visit[N-1][N-1] += 1

i, j = 0, 0
ans = []

while (i, j) != (N-1, N-1):
    visit[i][j] += 1
    if i == N-1:
        j += 1
        ans.append('R')
    elif j == N-1:
        i += 1
        ans.append('D')
    else:
        if visit[i+1][j] < visit[i][j+1]:
            i += 1
            ans.append('D')
        elif visit[i+1][j] > visit[i][j+1]:
            j += 1
            ans.append('R')
        else:
            i += 1
            ans.append('D')

print(''.join(ans))