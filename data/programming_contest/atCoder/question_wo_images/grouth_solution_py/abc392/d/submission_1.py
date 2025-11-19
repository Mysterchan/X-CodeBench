N = int(input())
K = [0] * N
dice = [{} for _ in range(N)]
for i in range(N):
    A = list(map(int, input().split()))
    K[i] = A[0]
    for j in range(A[0]):
        if A[j+1] not in dice[i]:
            dice[i][A[j+1]] = 0
        dice[i][A[j+1]] += 1

pmax = 0
for i in range(N-1):
    for j in range(i+1,N):
        p = 0
        if len(dice[i]) <= len(dice[j]):
            for key, m1 in dice[i].items():
                if key in dice[j]:
                    p += m1*dice[j][key]
        else:
            for key, m1 in dice[j].items():
                if key in dice[i]:
                    p += m1*dice[i][key]
        pmax = max(pmax, p/(K[i]*K[j]))

print(pmax)