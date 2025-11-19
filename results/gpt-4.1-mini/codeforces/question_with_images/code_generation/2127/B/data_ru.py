import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    s = input().strip()

    # Найдем ближайшую стену слева от x (индексация с 1)
    left_wall = 0
    for i in range(x - 1, 0, -1):
        if s[i - 1] == '#':
            left_wall = i
            break

    # Найдем ближайшую стену справа от x
    right_wall = n + 1
    for i in range(x + 1, n + 1):
        if s[i - 1] == '#':
            right_wall = i
            break

    # Расстояния до ближайших стен (если стены нет, считаем как выход за границу)
    dist_left = x - left_wall
    dist_right = right_wall - x

    # Ответ - минимальное из двух расстояний
    print(min(dist_left, dist_right))