import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# Общая сумма всех значений
total_sum = 0
for row in A:
    total_sum += sum(row)

# Построим двудольный граф для задачи максимального паросочетания с максимальным весом
# Разобьем клетки на две части по цвету шахматной доски:
# (i+j) % 2 == 0 -> левая часть
# (i+j) % 2 == 1 -> правая часть
# Ребра между смежными клетками с весом = A[u] + A[v]

# Нумеруем клетки в левой и правой части
left_id = {}
right_id = {}
left_count = 0
right_count = 0

for i in range(H):
    for j in range(W):
        if (i + j) % 2 == 0:
            left_id[(i, j)] = left_count
            left_count += 1
        else:
            right_id[(i, j)] = right_count
            right_count += 1

# Список рёбер: для каждой вершины из левой части список (правая вершина, вес)
edges = [[] for _ in range(left_count)]

# Функция для добавления ребра, если обе клетки существуют
def add_edge(i1, j1, i2, j2):
    if 0 <= i2 < H and 0 <= j2 < W:
        if (i1 + j1) % 2 == 0:
            u = left_id[(i1, j1)]
            v = right_id[(i2, j2)]
            w = A[i1][j1] + A[i2][j2]
            edges[u].append((v, w))
        else:
            u = left_id[(i2, j2)]
            v = right_id[(i1, j1)]
            w = A[i1][j1] + A[i2][j2]
            edges[u].append((v, w))

# Добавляем ребра для горизонтальных и вертикальных соседей
for i in range(H):
    for j in range(W):
        # вправо
        if j + 1 < W:
            add_edge(i, j, i, j + 1)
        # вниз
        if i + 1 < H:
            add_edge(i, j, i + 1, j)

# Теперь задача сводится к поиску максимального паросочетания с максимальным суммарным весом в двудольном графе
# Используем алгоритм Куна с потенциалами (Hungarian algorithm) для максимального паросочетания с весами

INF = 10**18

def hungarian():
    n, m = left_count, right_count
    # cost[u][v] = -weight, т.к. алгоритм минимизации, а нам нужно максимизировать
    cost = [[-INF]*m for _ in range(n)]
    for u in range(n):
        for v, w in edges[u]:
            cost[u][v] = -w

    u_label = [0]*n
    v_label = [0]*m
    for u in range(n):
        u_label[u] = max(cost[u])

    match_v = [-1]*m

    for u0 in range(n):
        # Поиск увеличивающей цепи
        INF2 = 10**18
        min_slack = [INF2]*m
        min_slack_u = [-1]*m
        prev = [-1]*m
        used_u = [False]*n
        used_v = [False]*m
        queue = []
        queue.append(u0)
        used_u[u0] = True
        prev_v = -1
        while True:
            while queue and prev_v == -1:
                u = queue.pop(0)
                for v in range(m):
                    if not used_v[v]:
                        delta = u_label[u] + v_label[v] - cost[u][v]
                        if delta < min_slack[v]:
                            min_slack[v] = delta
                            min_slack_u[v] = u
                        if min_slack[v] == 0:
                            used_v[v] = True
                            if match_v[v] == -1:
                                prev_v = v
                                break
                            else:
                                queue.append(match_v[v])
                                used_u[match_v[v]] = True
                if prev_v != -1:
                    break
            if prev_v != -1:
                break
            delta = INF2
            for v in range(m):
                if not used_v[v] and min_slack[v] < delta:
                    delta = min_slack[v]
            for i in range(n):
                if used_u[i]:
                    u_label[i] -= delta
            for j in range(m):
                if used_v[j]:
                    v_label[j] += delta
                else:
                    min_slack[j] -= delta
            for v in range(m):
                if not used_v[v] and min_slack[v] == 0:
                    used_v[v] = True
                    if match_v[v] == -1:
                        prev_v = v
                        break
                    else:
                        queue.append(match_v[v])
                        used_u[match_v[v]] = True
            if prev_v != -1:
                break

        # Восстановление увеличивающей цепи
        while True:
            u = min_slack_u[prev_v]
            next_v = match_v[prev_v]
            match_v[prev_v] = u
            prev_v = next_v
            if u == u0:
                break

    # Считаем сумму весов максимального паросочетания
    res = 0
    for v in range(m):
        u = match_v[v]
        if u != -1 and cost[u][v] != -INF:
            res += -cost[u][v]
    return res

max_matching_sum = hungarian()

# Ответ: total_sum - max_matching_sum
print(total_sum - max_matching_sum)