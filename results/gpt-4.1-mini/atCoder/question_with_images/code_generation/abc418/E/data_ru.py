import sys
from math import gcd

input = sys.stdin.readline

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

# Считаем количество пар с одинаковым направлением (направление - нормализованный вектор)
# Для каждой пары точек вычисляем вектор (dx, dy), нормализуем его (делим на gcd, приводим к единому знаку)
# Затем считаем количество пар с одинаковым направлением.
# Количество трапеций = сумма по всем направлениям C(count, 2),
# так как каждая пара пар с одинаковым направлением образует пару параллельных сторон,
# а значит - трапецию.

from collections import defaultdict

dir_count = defaultdict(int)

for i in range(N):
    x1, y1 = points[i]
    for j in range(i + 1, N):
        x2, y2 = points[j]
        dx = x2 - x1
        dy = y2 - y1
        g = gcd(dx, dy)
        dx //= g
        dy //= g
        # Приводим направление к единому виду: dx > 0 или если dx == 0, то dy > 0
        if dx < 0:
            dx = -dx
            dy = -dy
        elif dx == 0 and dy < 0:
            dy = -dy
        dir_count[(dx, dy)] += 1

# Подсчёт количества трапеций
# Для каждой группы с count пар, количество способов выбрать 2 пары = count * (count - 1) // 2
# Суммируем по всем направлениям
res = 0
for c in dir_count.values():
    if c >= 2:
        res += c * (c - 1) // 2

print(res)