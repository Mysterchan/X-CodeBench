N, M = list(map(int, input().split()))
P = list(map(int, input().split()))
Q = []
for i in range(N):
    k = 1
    while True:
        if k * k * P[i] <= M:
            Q.append((2 * k - 1) * P[i])

        else:
            break
        k += 1
Q.sort()
s = 0
for i in range(len(Q)):
    s += Q[i]
    if s > M:
        print(i)
        exit()
print(len(Q))