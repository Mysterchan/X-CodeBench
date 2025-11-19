N, D = map(int, input().split())
snakes = [tuple(map(int, input().split())) for _ in range(N)]

for k in range(1, D + 1):
    max_weight = 0
    for T, L in snakes:
        weight = T * (L + k)
        if weight > max_weight:
            max_weight = weight
    print(max_weight)