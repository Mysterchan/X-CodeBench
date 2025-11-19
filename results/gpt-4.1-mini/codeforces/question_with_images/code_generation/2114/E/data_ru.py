import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    g = [[] for __ in range(n)]
    for __ in range(n-1):
        v,u = map(int, input().split())
        v -= 1
        u -= 1
        g[v].append(u)
        g[u].append(v)

    # threat[i] - максимальная знакопеременная сумма для вершины i
    threat = [0]*n

    # parent[i] - родитель вершины i в дереве с корнем 0
    parent = [-1]*n

    # dfs для построения parent и обхода
    stack = [0]
    order = []
    while stack:
        v = stack.pop()
        order.append(v)
        for w in g[v]:
            if w == parent[v]:
                continue
            if parent[w] == -1 and w != 0:
                parent[w] = v
                stack.append(w)

    # threat для корня = a[0]
    threat[0] = a[0]

    # Для остальных:
    # threat[v] = max(a[v], a[v] - threat[parent[v]])
    # Объяснение:
    # Пусть для вершины v путь вертикальный - это либо только v (сумма a[v]),
    # либо путь v->parent[v]->... с чередованием знаков.
    # threat[parent[v]] - максимальная знакопеременная сумма для parent[v].
    # Тогда для v можно взять либо только a[v], либо a[v] - threat[parent[v]] (чередование знаков).
    # Максимум из этих двух и есть threat[v].

    for v in order[1:]:
        p = parent[v]
        threat[v] = max(a[v], a[v] - threat[p])

    print(*threat)