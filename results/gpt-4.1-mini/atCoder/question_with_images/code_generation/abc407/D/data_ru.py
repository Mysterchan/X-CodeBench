import sys
sys.setrecursionlimit(10**7)

H, W = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

N = H * W

# Преобразуем координаты (i,j) в индекс 0..N-1
def idx(i, j):
    return i * W + j

# Все значения в одном списке для удобства
vals = [A[i][j] for i in range(H) for j in range(W)]

# Предварительно вычислим XOR всех значений
total_xor = 0
for v in vals:
    total_xor ^= v

# Используем битмаску для представления занятости клеток
# 0 - свободна, 1 - занята домино

# Кэш для мемоизации: mask -> максим возможный XOR
# mask - битовая маска занятых клеток
from functools import lru_cache

@lru_cache(None)
def dfs(mask):
    # Найдем первую свободную клетку
    # Если все заняты, возвращаем 0 (XOR пустого множества)
    if mask == (1 << N) - 1:
        return 0

    # Найдем первый свободный индекс
    for i in range(N):
        if (mask & (1 << i)) == 0:
            break

    res = 0
    # Попробуем не закрывать эту клетку (оставить в XOR)
    # Тогда добавим ее значение к результату
    res = vals[i] ^ dfs(mask | (1 << i))

    # Попробуем поставить домино с соседями (если возможно)
    r, c = divmod(i, W)

    # Горизонтальное домино (i,j) и (i,j+1)
    if c + 1 < W:
        j = idx(r, c + 1)
        if (mask & (1 << j)) == 0:
            # Закрываем обе клетки, они не участвуют в XOR
            res = max(res, dfs(mask | (1 << i) | (1 << j)))

    # Вертикальное домино (i,j) и (i+1,j)
    if r + 1 < H:
        j = idx(r + 1, c)
        if (mask & (1 << j)) == 0:
            res = max(res, dfs(mask | (1 << i) | (1 << j)))

    return res

print(dfs(0))