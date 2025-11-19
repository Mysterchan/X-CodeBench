import sys
import bisect

input = sys.stdin.readline

N, W = map(int, input().split())
blocks = [None] * N
cols = [[] for _ in range(W + 1)]  # 1-based indexing for columns

for i in range(N):
    x, y = map(int, input().split())
    blocks[i] = (x, y)
    cols[x].append((y, i))

# Для каждого столбца отсортируем блоки по y
for x in range(1, W + 1):
    cols[x].sort()

# Для каждого столбца вычислим высоты слоёв (слои - это уровни заполнения)
# Слой 0 - нижний ряд, слой 1 - следующий сверху и т.д.
# Для каждого блока определим его слой (индекс в столбце)
layer = [0] * N
for x in range(1, W + 1):
    for idx, (_, i) in enumerate(cols[x]):
        layer[i] = idx

# Для каждого столбца определим высоту (максимальный слой + 1)
height = [0] * (W + 1)
for x in range(1, W + 1):
    height[x] = len(cols[x])

# Определим для каждого слоя (0-based) миним y среди всех столбцов
# Если в каком-то столбце слой отсутствует, то слой не полный
max_layer = max(height)
min_y_per_layer = []
for l in range(max_layer):
    ys = []
    full = True
    for x in range(1, W + 1):
        if l >= height[x]:
            full = False
            break
        ys.append(cols[x][l][0])
    if not full:
        break
    min_y_per_layer.append(min(ys))
L = len(min_y_per_layer)  # количество полных слоёв

# min_y_per_layer[l] - минимальный y в слое l (0-based)
# Слой l удаляется в момент времени l+1 (т.к. удаление происходит в момент t, начиная с 1)

Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# Для каждого блока i:
# - слой: layer[i]
# - y: blocks[i][1]
# Блок исчезает, если слой < L и y <= min_y_per_layer[layer[i]]
# Время исчезновения: layer[i] + 1
# Иначе блок живёт вечно

# Предобработка для быстрого ответа
# Для каждого блока вычислим время исчезновения или None
disappear_time = [None] * N
for i in range(N):
    l = layer[i]
    y = blocks[i][1]
    if l < L and y <= min_y_per_layer[l]:
        disappear_time[i] = l + 1  # исчезает в момент t = l+1
    else:
        disappear_time[i] = None  # не исчезает

# Ответ на запрос:
# В момент T_j + 0.5 блок существует, если либо disappear_time[i] == None
# либо T_j + 0.5 < disappear_time[i], т.е. T_j < disappear_time[i]
# иначе блок исчез уже в момент disappear_time[i] <= T_j + 0.5

out = []
for T, A in queries:
    i = A - 1
    dt = disappear_time[i]
    if dt is None or T < dt:
        out.append("Yes")
    else:
        out.append("No")

print("\n".join(out))