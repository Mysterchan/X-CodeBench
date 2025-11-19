def mkxy(N):
    x, y = zip(*(tuple(map(int, input().split())) for _ in range(N)))
    return x, y

def sqd(sx, sy, gx, gy):
    return (sx - gx) ** 2 + (sy - gy) ** 2

def is_possible(target):
    target *= target
    count = [0] * N
    for u in range(N):
        for v in range(N):
            if dist[u][v] <= target:
                count[u] += 1
    return all(count[u] >= 1 for u in range(N))

def bin_search(left, right):
    for _ in range(90):
        mid = (left + right) / 2
        if is_possible(mid):
            right = mid
        else:
            left = mid
    return right

N = int(input())
TX, TY = mkxy(N)
BX, BY = mkxy(N)
dist = [[sqd(TX[u], TY[u], BX[v], BY[v]) for v in range(N)] for u in range(N)]
ans = bin_search(0, 1 << 61)
print(ans**0.5)  # Output the square root of the answer as time