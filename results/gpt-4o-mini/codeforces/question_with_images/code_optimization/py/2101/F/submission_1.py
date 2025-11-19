MOD = 998244353
TWO_THIRDS = 2 * pow(3, MOD - 2, MOD) % MOD
POW3 = [1] * 3001
POW2 = [1] * 3001

for i in range(1, 3001):
    POW3[i] = POW3[i - 1] * 3 % MOD
    POW2[i] = POW2[i - 1] * 2 % MOD

def dfs(node, parent, depth, edges, depths):
    depths[depth].append(node)
    for neighbor in edges[node]:
        if neighbor != parent:
            dfs(neighbor, node, depth + 1, edges, depths)

def calculate_coolness(n, edges):
    ans = 0
    for center in range(n):
        depths = [[] for _ in range(n)]
        dfs(center, -1, 0, edges, depths)

        acc = [0] * (n + 1)
        poly = [0] * (n + 1)
        radii = [0] * n

        i = 0
        for d in range(n):
            cnt = len(depths[d])
            if cnt == 0:
                continue
            poly[i] += 1
            poly[i + cnt] -= 1
            for j in range(cnt):
                radii[i] = 2 * d + (center >= n)
                acc[i + 1] = (TWO_THIRDS * acc[i] + radii[i]) % MOD
                i += 1
            poly[i] -= 1
            poly[i + cnt] += 1

        rem = [0] * (n - 1)
        for i in range(n, 1, -1):
            rem[i - 2] = poly[i]
            poly[i - 1] += 2 * poly[i]
            poly[i - 2] -= poly[i]

        for i in range(n - 1):
            if i:
                ans += rem[i] * acc[i] * POW3[i - 1]
            ans += rem[i] * (POW3[i] - POW2[i]) * radii[i]
            ans += rem[i] * 2 * radii[i] * POW3[i]

    return ans % MOD

import sys
input = sys.stdin.read
data = input().splitlines()
index = 0
t = int(data[index])
index += 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    edges = [[] for _ in range(n)]
    for __ in range(n - 1):
        u, v = map(int, data[index].split())
        edges[u - 1].append(v - 1)
        edges[v - 1].append(u - 1)
        index += 1
    results.append(calculate_coolness(n, edges))

print('\n'.join(map(str, results)))