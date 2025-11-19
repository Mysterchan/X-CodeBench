import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)

# Условие алкана:
# - граф - дерево
# - каждая вершина имеет степень 1 или 4
# - есть хотя бы одна вершина степени 4

# Нужно найти максимальный подграф, являющийся алканом.
# Подграф - набор вершин и рёбер между ними, образующих дерево,
# где степени вершин 1 или 4, и есть хотя бы одна степень 4.

# Идея решения:
# Мы ищем максимальное поддерево, где все вершины имеют степень 1 или 4,
# и есть хотя бы одна вершина степени 4.
# Поддерево - связный набор вершин.

# Степень в подграфе - количество соседей из выбранных вершин.

# Задача сводится к выбору поддерева с ограничением на степени.

# Подход:
# Используем динамическое программирование на дереве.
# Для каждой вершины считаем варианты:
# - включить вершину в подграф или нет.
# - если включаем, то сколько соседей включаем, чтобы степень была 1 или 4.
# - степень вершины в подграфе - количество включенных соседей.

# Но степень вершины зависит от включения соседей, а соседи зависят от неё.
# Чтобы избежать циклов, будем считать DP снизу вверх.

# Для каждой вершины v:
# dp[v][deg][has4] = максимальный размер поддерева в поддереве с корнем v,
# где v включена, степень v = deg (deg=1 или 4),
# has4 = 0/1 - есть ли в поддереве вершина степени 4.

# Также нужно рассмотреть вариант, что v не включена:
# dp[v][0][0] = 0 (пустое поддерево)

# Но степень 0 для включенной вершины невозможна, значит dp[v][deg][has4] для deg in {1,4}
# и dp[v][0][0] для не включенной вершины.

# Для листа:
# - если не включаем: dp[v][0][0] = 0
# - если включаем: степень должна быть 1 (т.к. лист), dp[v][1][0] = 1 (включили вершину, степень 1, но нет вершины с deg=4)

# Для внутренней вершины:
# Нужно выбрать, какие дети включать, чтобы степень v была 1 или 4.

# Степень v = количество включенных детей.

# Для каждого ребенка u у нас dp[u] с вариантами включения и степенями.

# Мы должны выбрать подмножество детей, чтобы количество включенных детей = deg (1 или 4),
# и максимизировать сумму dp[u][*][*].

# При этом has4 = (есть ли в поддереве вершина с deg=4) = max по детям и по v (если deg=4, то has4=1).

# Для каждого ребенка u мы можем выбрать:
# - не включать u: dp[u][0][0]
# - включить u с deg=1 или deg=4, has4=0 или 1

# Для упрощения:
# Для каждого ребенка u возьмем максимум по dp[u][deg][has4] для deg in {0,1,4} (0 - не включать u)
# Но нам важно знать, сколько детей включено, чтобы степень v была 1 или 4.

# Значит для каждого ребенка u у нас есть варианты:
# - не включать u: (size, has4) = dp[u][0][0]
# - включить u с deg=1, has4=0 или 1
# - включить u с deg=4, has4=0 или 1

# Для каждого ребенка u соберем список вариантов (size, has4, included=0/1)

# Далее нам нужно выбрать подмножество детей с количеством включенных = deg (1 или 4),
# максимизирующее сумму size, и has4 = OR по has4 детей.

# Для эффективности:
# - Для каждого ребенка возьмем максимум по включению (deg=1 или 4) и не включению (deg=0)
# - Но чтобы точно знать has4, нужно хранить два варианта: has4=0 и has4=1

# Для каждого ребенка u сделаем два значения:
# - best0 = максимальный размер поддерева без has4 (has4=0)
# - best1 = максимальный размер поддерева с has4=1

# Для не включения u: size=0, has4=0

# Для включения u:
# - переберем deg=1 и deg=4, возьмем максимум по has4=0 и has4=1

# Таким образом для каждого ребенка u получим два варианта:
# - (size0, has4=0, included=0 или 1)
# - (size1, has4=1, included=0 или 1)

# Далее нам нужно выбрать подмножество детей с количеством включенных = deg (1 или 4),
# максимизирующее сумму size, и has4 = OR по has4 детей.

# Для этого сделаем DP по детям:
# dp_child[count][has4] = максимальный размер поддерева, выбрав count детей,
# с has4 = 0 или 1.

# Инициализация:
# dp_child[0][0] = 0
# dp_child[0][1] = -inf

# Для каждого ребенка u:
# обновляем dp_child:
# - не включать u: dp_child[count][has4] = max(dp_child[count][has4], dp_child[count][has4])
# - включить u с has4=0: dp_child[count+1][has4 OR 0] = max(...)
# - включить u с has4=1: dp_child[count+1][has4 OR 1] = max(...)

# После обработки всех детей, для deg in {1,4} берем dp_child[deg][has4] и
# dp[v][deg][has4] = dp_child[deg][has4] + 1 (за вершину v)

# Также dp[v][0][0] = 0 (не включаем v)

# В конце ответ - максимум по всем вершинам v и deg in {1,4} dp[v][deg][1]
# (т.к. должен быть хотя бы один deg=4 в подграфе)

# Если такого нет, выводим -1

INF = -10**15

# dp[v] = dict: ключ (deg, has4) -> max size
# deg in {0,1,4}, has4 in {0,1}
# deg=0 означает v не включена, size=0

def merge_dp(dp1, dp2):
    # dp1, dp2: dict (deg, has4) -> size
    # Возвращаем объединение (максимум по ключам)
    res = {}
    for k in dp1:
        res[k] = dp1[k]
    for k in dp2:
        if k in res:
            if dp2[k] > res[k]:
                res[k] = dp2[k]
        else:
            res[k] = dp2[k]
    return res

def max2(a,b):
    return a if a>b else b

def solve():
    from collections import defaultdict

    sys.setrecursionlimit(10**7)

    # Для каждого v будем считать dp[v] = dict (deg, has4) -> max size
    # deg in {0,1,4}, has4 in {0,1}
    # deg=0 - v не включена, size=0

    # Для листа:
    # dp[v][0,0] = 0
    # dp[v][1,0] = 1 (включили v, степень 1)
    # dp[v][4,0] = -inf (нельзя, т.к. нет детей)

    # Для внутреннего узла:
    # Собираем варианты детей, делаем knapsack по количеству включенных детей = deg (1 или 4)

    dp = [defaultdict(lambda: INF) for _ in range(N+1)]
    visited = [False]*(N+1)

    def dfs(v, p):
        visited[v] = True
        children = []
        for u in edges[v]:
            if u == p:
                continue
            dfs(u,v)
            children.append(u)

        # Если лист
        if not children:
            dp[v][(0,0)] = 0
            dp[v][(1,0)] = 1
            dp[v][(4,0)] = INF
            return

        # Для каждого ребенка u возьмем максимум по deg in {0,1,4} и has4 in {0,1}
        # Для u сформируем два варианта:
        # best0 = max size с has4=0
        # best1 = max size с has4=1
        # и включен ли ребенок (0 - не включен, 1 - включен)

        child_options = []
        for u in children:
            best0 = INF
            best1 = INF
            # перебираем dp[u]
            for (deg, h4), val in dp[u].items():
                if val == INF:
                    continue
                if deg == 0:
                    # не включаем u
                    if val > best0:
                        best0 = val
                else:
                    # включаем u
                    if h4 == 0:
                        if val > best0:
                            best0 = val
                    else:
                        if val > best1:
                            best1 = val
            # Если не включаем u: size=best0 (has4=0)
            # Если включаем u: size=max(best0, best1) с has4=?
            # Но нам нужно разделить has4=0 и has4=1 для включения
            # Переберем dp[u] заново, чтобы точно разделить
            inc0 = INF
            inc1 = INF
            for (deg, h4), val in dp[u].items():
                if val == INF or deg == 0:
                    continue
                if h4 == 0:
                    if val > inc0:
                        inc0 = val
                else:
                    if val > inc1:
                        inc1 = val
            # Если не включаем u: (size=best0, has4=0, included=0)
            # Если включаем u: два варианта (inc0, has4=0, included=1), (inc1, has4=1, included=1)
            # inc0 or inc1 могут быть INF, если нет таких вариантов
            child_options.append([
                (best0, 0, 0),  # не включаем u
                (inc0, 0, 1),   # включаем u, has4=0
                (inc1, 1, 1)    # включаем u, has4=1
            ])

        # Теперь делаем knapsack по детям:
        # dp_child[count][has4] = max size
        # count - количество включенных детей
        # has4 - 0 или 1
        # Инициализация:
        dp_child = [[INF]*2 for _ in range(len(children)+1)]
        dp_child[0][0] = 0

        for opts in child_options:
            ndp = [[INF]*2 for _ in range(len(children)+1)]
            for count in range(len(children)+1):
                for h4 in range(2):
                    if dp_child[count][h4] == INF:
                        continue
                    # не включаем u
                    size, nh4, inc = opts[0]
                    if size != INF:
                        val = dp_child[count][h4] + size
                        if val > ndp[count][h4]:
                            ndp[count][h4] = val
                    # включаем u с has4=0
                    size, nh4, inc = opts[1]
                    if size != INF and count+1 <= len(children):
                        val = dp_child[count][h4] + size
                        nh4_new = h4 | nh4
                        if val > ndp[count+1][nh4_new]:
                            ndp[count+1][nh4_new] = val
                    # включаем u с has4=1
                    size, nh4, inc = opts[2]
                    if size != INF and count+1 <= len(children):
                        val = dp_child[count][h4] + size
                        nh4_new = h4 | nh4
                        if val > ndp[count+1][nh4_new]:
                            ndp[count+1][nh4_new] = val
            dp_child = ndp

        # Теперь для v:
        # dp[v][0,0] = 0 (не включаем v)
        dp[v][(0,0)] = 0
        # dp[v][1,has4] = dp_child[1][has4] + 1
        # dp[v][4,has4] = dp_child[4][has4] + 1
        for deg in [1,4]:
            for h4 in [0,1]:
                val = dp_child[deg][h4]
                if val == INF:
                    continue
                # Если deg=4, то вершина v имеет степень 4, значит has4=1
                has4_new = h4
                if deg == 4:
                    has4_new = 1
                total = val + 1
                key = (deg, has4_new)
                if total > dp[v][key]:
                    dp[v][key] = total

    dfs(1,-1)

    ans = -1
    for v in range(1,N+1):
        for deg in [1,4]:
            if (deg,1) in dp[v]:
                val = dp[v][(deg,1)]
                if val > ans:
                    ans = val
    print(ans)
solve()