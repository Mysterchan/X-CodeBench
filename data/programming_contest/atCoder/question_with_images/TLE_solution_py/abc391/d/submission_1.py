N, W = list(map(int, input().split()))

Wi = []
p = [-1] * (N + 1)
for i in range(W + 1):
    Wi.append([[0, 0]])
for i in range(N):
    xy = list(map(int, input().split()))
    Wi[xy[0]].append([xy[1], i + 1])
for i in range(1, W + 1):
    Wi[i].sort()

base = [1] * (W + 1)
f1 = True
count = 0
while f1 == True:
    count += 1
    f1 = False
    f = True

    for i in range(1, W + 1):
        if base[0] < len(Wi[i]):
            if Wi[i][base[0]][0] != base[i]:
                f = False
                break
        else:
            f = False
    if f == True:
        for i in range(1, W + 1):
            p[Wi[i][base[0]][1]] = count
        for i in range(W + 1):
            base[i] += 1
        f1 = True

    for i in range(1, W + 1):
        if base[0] < len(Wi[i]):
            if Wi[i][base[0]][0] > base[i]:
                base[i] += 1
                f1 = True

Q = int(input())
for i in range(Q):
    T, A = map(int, input().split())
    if p[A] == -1:
        print('Yes')
    elif p[A] > T:
        print('Yes')
    else:
        print('No')