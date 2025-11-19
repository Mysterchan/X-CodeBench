N, D = map(int, input().split())

T = []
L = []

for _ in range(N):
    t, l = map(int, input().split())
    T.append(t)
    L.append(l)

for k in range(1, D + 1):
    max_weight = 0
    for i in range(N):
        weight = T[i] * (L[i] + k)
        if weight > max_weight:
            max_weight = weight

    print(max_weight)