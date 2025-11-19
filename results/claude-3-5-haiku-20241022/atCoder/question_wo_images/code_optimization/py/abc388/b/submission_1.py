N, D = map(int, input().split())

snakes = []
for _ in range(N):
    t, l = map(int, input().split())
    snakes.append((t, l))

for k in range(1, D + 1):
    max_weight = 0
    for t, l in snakes:
        weight = t * (l + k)
        if weight > max_weight:
            max_weight = weight
    print(max_weight)