import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    count = 0
    for __ in range(n):
        dx, dy, x, y = map(int, input().split())
        # Проверяем, попадёт ли шар в лузу.
        # Шар движется под углом 45°, со скоростью 10^100, направления dx, dy = ±1.
        # При отражениях координаты "зеркально" отражаются относительно границ.
        # Можно свести задачу к проверке, попадёт ли шар в один из углов (0,0), (0,s), (s,0), (s,s).
        # Для этого рассмотрим движение по координате x и y отдельно.
        # При движении под углом 45° и отражениях, положение по x и y через время t:
        # pos_x(t) = x + dx * v * t (с отражениями)
        # Аналогично для y.
        # Отражения можно учесть через "отражённую" координату:
        # pos_x(t) = (x + dx * t) mod (2*s)
        # Если pos_x(t) > s, то pos_x(t) = 2*s - pos_x(t)
        # Аналогично для y.
        # Шар попадёт в лузу, если существует t, при котором pos_x(t) и pos_y(t) одновременно равны 0 или s.
        # При движении под углом 45° и скорости v, t можно выразить через координаты.
        # Рассмотрим уравнение для попадания в лузу:
        # pos_x(t) = corner_x, pos_y(t) = corner_y, где corner_x, corner_y ∈ {0, s}
        # Из-за симметрии и движения под углом 45°, условие сводится к проверке:
        # (x + dx * t) mod (2*s) == corner_x или 2*s - ((x + dx * t) mod (2*s)) == corner_x
        # Аналогично для y.
        # Для углов (0,0), (0,s), (s,0), (s,s) проверим, существует ли t ≥ 0, при котором
        # pos_x(t) == corner_x и pos_y(t) == corner_y одновременно.
        # Из-за движения под углом 45°, t = (pos_x(t) - x) / dx = (pos_y(t) - y) / dy
        # Значит, для некоторого corner_x, corner_y:
        # (corner_x - x) / dx == (corner_y - y) / dy == t ≥ 0
        # Проверим для всех 4 углов, если хотя бы для одного t ≥ 0 целое и совпадает, значит шар попадёт в лузу.

        def can_pocket(x, y, dx, dy, s):
            corners = [(0,0), (0,s), (s,0), (s,s)]
            for cx, cy in corners:
                # Рассмотрим движение с отражениями.
                # Функция для вычисления "отражённой" координаты:
                def reflect(pos):
                    pos_mod = pos % (2*s)
                    return pos_mod if pos_mod <= s else 2*s - pos_mod

                # Нам нужно найти t ≥ 0, такое что:
                # reflect(x + dx * t) == cx и reflect(y + dy * t) == cy
                # Переберём все возможные варианты t, при которых reflect(x + dx * t) == cx
                # и проверим, совпадает ли t с условием для y.

                # Для reflect(x + dx * t) == cx:
                # pos = x + dx * t
                # pos mod 2s == cx или 2s - (pos mod 2s) == cx
                # Рассмотрим два случая:
                # 1) pos mod 2s == cx => pos = m*2s + cx, m >= 0
                # 2) 2s - (pos mod 2s) == cx => pos mod 2s = 2s - cx => pos = m*2s + (2s - cx)

                # Решим для t:
                # t = (pos - x) / dx

                # Переберём m так, чтобы t ≥ 0 и целое.

                # Максимальное m ограничим, чтобы не было бесконечного цикла.
                # t должен быть целым и ≥ 0.

                # dx и dy равны ±1, значит t = pos - x или t = x - pos

                # Переберём m от 0 до 2 (достаточно, т.к. t должен быть минимальным положительным)
                for m in range(3):
                    for pos_x_candidate in [m*2*s + cx, m*2*s + (2*s - cx)]:
                        t_x = (pos_x_candidate - x) * dx
                        if t_x < 0:
                            continue
                        if t_x != int(t_x):
                            continue
                        # Аналогично для y:
                        for pos_y_candidate in [m*2*s + cy, m*2*s + (2*s - cy)]:
                            t_y = (pos_y_candidate - y) * dy
                            if t_y < 0:
                                continue
                            if t_y != int(t_y):
                                continue
                            if t_x == t_y:
                                return True
            return False

        if can_pocket(x, y, dx, dy, s):
            count += 1
    print(count)