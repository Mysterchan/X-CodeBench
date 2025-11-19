N,M = map(int,input().split())

S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(M)]

if len(T) == 1:
    for i in range(N):
        for j in range(N):
            if S[i][j] == T[0][0]:
                print(i+1,j+1)
else:
    for i in range(N-M+1):
        for k in range(N-M+1):
            if S[i][k:k+M] == T[0]:
                for j in range(1,M):
                    if S[i+j][k:k+M] != T[j]:
                        break
                else:
                    print(i+1,j+1)