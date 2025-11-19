import sys
import math

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    px, py, qx, qy = map(int, input().split())
    a = list(map(int, input().split()))

    dist = math.sqrt((qx - px) ** 2 + (qy - py) ** 2)
    s = sum(a)
    max_a = max(a)

    # Проверяем, можно ли достичь точку q после всех операций
    # Условие достижимости:
    # 1) Расстояние между p и q не больше суммы всех шагов (иначе не дотянуть)
    # 2) Расстояние между p и q не меньше разницы между максимальным шагом и суммой остальных (иначе нельзя "сжать" путь)
    # Формально: max_a <= s - max_a + dist  <=> dist >= max_a - (s - max_a) = 2*max_a - s
    # И dist <= s
    # Если dist < 2*max_a - s, то ответ No
    # Если dist > s, то ответ No
    # Иначе Yes

    if dist > s:
        print("No")
    else:
        # Проверяем нижнюю границу
        if dist < abs(s - 2 * max_a):
            print("No")
        else:
            print("Yes")