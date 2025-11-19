import sys
input = sys.stdin.readline

def dfs(x,result,visited):
    if x == Y:
        print(*result)
        return True

    for nx in graph[x]:
        if nx not in visited:
            visited.add(nx)
            result.append(nx)
            if dfs(nx,result,visited): return True
            visited.remove(nx)
            result.pop()

    return False

for _ in range(int(input())):
    N,M,X,Y = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1,N+1):
        graph[i].sort()

    dfs(X,[X],{X})