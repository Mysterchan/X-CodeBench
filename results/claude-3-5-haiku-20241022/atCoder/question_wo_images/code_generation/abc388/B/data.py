N, D = map(int, input().split())
snakes = []
for _ in range(N):
    T, L = map(int, input().split())
    snakes.append((T, L))

for k in range(1, D + 1):
    max_weight = 0
    for T, L in snakes:
        weight = T * (L + k)
        max_weight = max(max_weight, weight)
    print(max_weight)