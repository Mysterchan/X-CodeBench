import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
if M != N:
    print("No")
    exit()

deg = [0] * N
parent = [-1] * N

def find(x):
    while parent[x] >= 0:
        if parent[parent[x]] >= 0:
            parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    if parent[x] > parent[y]:
        x, y = y, x
    parent[x] += parent[y]
    parent[y] = x
    return True

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    deg[a] += 1
    deg[b] += 1
    union(a, b)

root = find(0)
for i in range(1, N):
    if find(i) != root:
        print("No")
        exit()

for d in deg:
    if d != 2:
        print("No")
        exit()

print("Yes")