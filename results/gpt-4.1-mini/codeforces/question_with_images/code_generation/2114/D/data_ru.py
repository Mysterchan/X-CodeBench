import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    xs = []
    ys = []
    for __ in range(n):
        x, y = map(int, input().split())
        xs.append(x)
        ys.append(y)

    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)

    # Без перемещения стоимость:
    base_cost = (max_x - min_x + 1) * (max_y - min_y + 1)

    # Если n == 1, ответ 1
    if n == 1:
        print(1)
        continue

    # Для оптимизации перемещения:
    # Рассмотрим варианты перемещения одного монстра к границам:
    # Перемещение может уменьшить ширину или высоту прямоугольника.
    # Возможные варианты:
    # 1) Переместить монстра, который задает min_x, чтобы увеличить min_x (сдвинуть границу вправо)
    # 2) Переместить монстра, который задает max_x, чтобы уменьшить max_x (сдвинуть границу влево)
    # 3) Аналогично для min_y и max_y

    # Для этого нужно знать, какие монстры задают границы.
    # Найдем индексы монстров с min_x, max_x, min_y, max_y
    # Но может быть несколько монстров с min_x и т.д., возьмем всех.

    min_x_monsters = [i for i, x in enumerate(xs) if x == min_x]
    max_x_monsters = [i for i, x in enumerate(xs) if x == max_x]
    min_y_monsters = [i for i, y in enumerate(ys) if y == min_y]
    max_y_monsters = [i for i, y in enumerate(ys) if y == max_y]

    # Чтобы быстро проверить, можно ли сдвинуть границу,
    # нужно знать вторые минимальные и максимальные значения по x и y.

    # Найдем вторые минимальные и максимальные значения по x и y
    xs_sorted = sorted(xs)
    ys_sorted = sorted(ys)

    # Второй минимальный x (если есть)
    second_min_x = xs_sorted[1] if n > 1 else min_x
    # Второй максимальный x
    second_max_x = xs_sorted[-2] if n > 1 else max_x
    # Второй минимальный y
    second_min_y = ys_sorted[1] if n > 1 else min_y
    # Второй максимальный y
    second_max_y = ys_sorted[-2] if n > 1 else max_y

    # Функция для вычисления площади прямоугольника по границам
    def area(x1, x2, y1, y2):
        return (x2 - x1 + 1) * (y2 - y1 + 1)

    ans = base_cost

    # Рассмотрим варианты сдвига границ, перемещая один монстра:

    # 1) Сдвинуть min_x вправо (увеличить min_x)
    # Можно сдвинуть min_x до второго_min_x, если переместим монстра(ы) с min_x
    # Тогда новая ширина = max_x - second_min_x + 1
    # Высота не меняется
    if n > 1:
        new_min_x = second_min_x
        new_area = area(new_min_x, max_x, min_y, max_y)
        if new_area < ans:
            ans = new_area

    # 2) Сдвинуть max_x влево (уменьшить max_x)
    # Переместить монстра(ы) с max_x
    new_max_x = second_max_x
    new_area = area(min_x, new_max_x, min_y, max_y)
    if new_area < ans:
        ans = new_area

    # 3) Сдвинуть min_y вверх (увеличить min_y)
    new_min_y = second_min_y
    new_area = area(min_x, max_x, new_min_y, max_y)
    if new_area < ans:
        ans = new_area

    # 4) Сдвинуть max_y вниз (уменьшить max_y)
    new_max_y = second_max_y
    new_area = area(min_x, max_x, min_y, new_max_y)
    if new_area < ans:
        ans = new_area

    # 5) Сдвинуть одновременно по двум осям:
    # Переместить монстра с min_x и min_y (если это один монстр, то можно)
    # Но можно переместить только одного монстра, поэтому сдвигать одновременно по двум осям
    # можно только если один монстр задает обе границы.

    # Проверим пересечения множеств монстров, задающих границы:
    # Если есть монстр, который задает min_x и min_y
    intersect_min_x_min_y = set(min_x_monsters) & set(min_y_monsters)
    if intersect_min_x_min_y:
        new_area = area(second_min_x, max_x, second_min_y, max_y)
        if new_area < ans:
            ans = new_area

    # min_x и max_y
    intersect_min_x_max_y = set(min_x_monsters) & set(max_y_monsters)
    if intersect_min_x_max_y:
        new_area = area(second_min_x, max_x, min_y, second_max_y)
        if new_area < ans:
            ans = new_area

    # max_x и min_y
    intersect_max_x_min_y = set(max_x_monsters) & set(min_y_monsters)
    if intersect_max_x_min_y:
        new_area = area(min_x, second_max_x, second_min_y, max_y)
        if new_area < ans:
            ans = new_area

    # max_x и max_y
    intersect_max_x_max_y = set(max_x_monsters) & set(max_y_monsters)
    if intersect_max_x_max_y:
        new_area = area(min_x, second_max_x, min_y, second_max_y)
        if new_area < ans:
            ans = new_area

    print(ans)