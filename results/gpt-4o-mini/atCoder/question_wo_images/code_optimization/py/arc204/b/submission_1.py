n, k = map(int, input().split())
P = list(map(lambda x: int(x) - 1, input().split()))
vis = [False] * (n * k)
ans = 0

for i in range(n * k):
    if not vis[i]:
        cycle = []
        j = i
        while not vis[j]:
            vis[j] = True
            cycle.append(j % n)
            j = P[j]
        
        ans += len(cycle) - 1

print(ans)