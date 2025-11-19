import sys
input = sys.stdin.readline

N, L = map(int, input().split())
d = list(map(int, input().split()))

# Префиксные суммы расстояний по часовой стрелке от точки 1
pos = [0] * (N + 1)
for i in range(1, N):
    pos[i + 1] = (pos[i] + d[i - 1]) % L

# pos[i] - позиция точки i на окружности (0 <= pos[i] < L)

# Для равностороннего треугольника на окружности длины L
# расстояния между точками должны быть L/3 и 2L/3 по часовой стрелке.
# Точки a,b,c должны удовлетворять:
# dist(a,b) = L/3, dist(b,c) = L/3, dist(c,a) = L/3 (по часовой стрелке)
# или в другой последовательности, но с одинаковыми расстояниями.

# Проверим, что L делится на 3, иначе равносторонних треугольников быть не может.
if L % 3 != 0:
    print(0)
    sys.exit(0)

step = L // 3

# Для каждой точки pos[i], ищем точки pos[i] + step и pos[i] + 2*step (mod L)
# Если они существуют, то (i, j, k) образуют равносторонний треугольник.

# Создадим словарь: позиция -> индекс точки
pos_to_index = dict()
for i in range(1, N + 1):
    pos_to_index[pos[i]] = i

count = 0
for i in range(1, N + 1):
    p1 = pos[i]
    p2 = (p1 + step) % L
    p3 = (p1 + 2 * step) % L
    if p2 in pos_to_index and p3 in pos_to_index:
        a, b, c = i, pos_to_index[p2], pos_to_index[p3]
        # Проверяем порядок a < b < c
        triple = sorted([a, b, c])
        if triple[0] == a:
            # Чтобы не считать одинаковые тройки несколько раз,
            # считаем только если a - минимальный индекс в тройке
            count += 1

print(count)