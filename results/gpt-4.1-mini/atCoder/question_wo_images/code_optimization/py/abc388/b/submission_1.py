N, D = map(int, input().split())

T = []
L = []

for _ in range(N):
    t, l = map(int, input().split())
    T.append(t)
    L.append(l)

max_weight = 0
max_t = 0
max_l = 0

# Find the snake with the maximum thickness
# Because weight = thickness * (length + k)
# For each k, max weight = max over i of T[i]*(L[i]+k)
# = max over i of T[i]*L[i] + T[i]*k
# So for each k, max weight = max_i (T[i]*L[i]) + k * max_i T[i] only if the snake with max T[i] is the same as the one with max T[i]*L[i]
# But since different snakes may dominate at different k, we can precompute the weight function for each snake and pick max for each k.

# Since N and D are small, precompute weights for all snakes and all k, then pick max for each k.

weights = [ [T[i]*(L[i]+k) for k in range(1, D+1)] for i in range(N)]

for k in range(D):
    max_weight = 0
    for i in range(N):
        if weights[i][k] > max_weight:
            max_weight = weights[i][k]
    print(max_weight)