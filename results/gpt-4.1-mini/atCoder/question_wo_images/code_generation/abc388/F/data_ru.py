import sys
import collections

def main():
    input = sys.stdin.readline
    N, M, A, B = map(int, input().split())
    bad_intervals = [tuple(map(int, input().split())) for _ in range(M)]

    # Добавим фиктивные интервалы в начале и конце для удобства
    # Интервалы плохих квадратов: (L_i, R_i), отсортированы и непересекаются
    # Хорошие интервалы - промежутки между плохими
    good_intervals = []

    prev_end = 0
    for L, R in bad_intervals:
        if prev_end + 1 <= L - 1:
            good_intervals.append((prev_end + 1, L - 1))
        prev_end = R
    if prev_end + 1 <= N:
        good_intervals.append((prev_end + 1, N))

    # Начальная пози - 1, она не плохая (по условию)
    # Проверим, что 1 не в плохом интервале
    # По условию 1 < L_i, значит 1 не плохой

    # Если 1 == N, то ответ Yes
    if N == 1:
        print("Yes")
        return

    # Если 1 не в хорошем интервале, то нет решения
    # Но по условию 1 не плохой, значит 1 в хорошем интервале
    # Найдем индекс хорошего интервала, в котором находится 1
    # good_intervals отсортированы по возрастанию

    # Найдем индекс интервала, содержащего 1
    start_idx = -1
    for i, (l, r) in enumerate(good_intervals):
        if l <= 1 <= r:
            start_idx = i
            break
    if start_idx == -1:
        print("No")
        return

    # BFS по хорошим интервалам
    # Состояние: (interval_index, position_in_interval)
    # position_in_interval - позиция внутри интервала (относительно l)
    # Но позиция внутри интервала может быть очень большая (до 10^12)
    # Поэтому будем хранить только максим достижимую позицию внутри интервала
    # и использовать очередь для переходов между интервалами

    # Идея:
    # Для каждого интервала будем хранить максимальную достижимую позицию внутри него
    # Изначально для стартового интервала max_reach = 1
    # Для остальных - 0 (не достижимо)
    # При переходе из позиции x в интервал i, можно перейти на позиции x+i, где A <= i <= B,
    # если позиция не плохая (т.е. в хорошем интервале)
    # Переходы могут пересекать границы интервалов

    # Для оптимизации:
    # Мы будем обрабатывать интервалы по очереди, расширяя max_reach внутри интервала
    # и пытаясь перейти в соседние интервалы, если прыжок выходит за границы текущего интервала

    # max_reach[i] - максимальная позиция, достижимая в i-м хорошем интервале
    max_reach = [0] * len(good_intervals)
    l0, r0 = good_intervals[start_idx]
    max_reach[start_idx] = 1  # стартовая позиция

    queue = collections.deque()
    queue.append(start_idx)

    while queue:
        i = queue.popleft()
        l, r = good_intervals[i]
        cur_max = max_reach[i]

        # Расширяем достижимую позицию внутри интервала
        # Можно прыгать от cur_max + A до cur_max + B, но не выходя за r
        # Новая достижимая позиция внутри интервала:
        new_max = min(r, cur_max + B)
        if new_max > cur_max:
            max_reach[i] = new_max
            cur_max = new_max

        # Если достигли N, ответ Yes
        if cur_max == N:
            print("Yes")
            return

        # Попытаемся перейти в соседние интервалы
        # Прыжок i: A <= jump <= B
        # Для позиции x в [l, cur_max], можно прыгнуть на x + jump
        # Если x + jump > r, то прыжок выходит за текущий интервал
        # Нужно найти в каком интервале находится x + jump

        # Рассмотрим все прыжки от A до B
        # Для каждого прыжка, вычислим миним и максим позиции, куда можно прыгнуть из текущего интервала
        # min_jump_pos = l + A
        # max_jump_pos = cur_max + B

        # Но перебор всех позиций невозможен, поэтому рассмотрим диапазон достижимых позиций:
        # Достижимые позиции в текущем интервале: [l, cur_max]
        # Прыжки: [A, B]
        # Значит достижимые позиции после прыжка: [l + A, cur_max + B]

        # Теперь нужно найти, какие интервалы пересекаются с [l + A, cur_max + B]
        # и обновить max_reach для них

        # Используем бинарный поиск для поиска интервалов, пересекающих этот диапазон

        from bisect import bisect_left, bisect_right

        jump_min = l + A
        jump_max = cur_max + B
        if jump_min > N:
            continue
        if jump_max > N:
            jump_max = N

        # Найдем индексы интервалов, которые пересекаются с [jump_min, jump_max]
        # good_intervals отсортированы по l

        # Интервал пересекается с [jump_min, jump_max], если:
        # interval.r >= jump_min and interval.l <= jump_max

        # Найдем left_idx - первый интервал с r >= jump_min
        # Найдем right_idx - последний интервал с l <= jump_max

        # Для поиска по r, создадим массив r_list
        # Для поиска по l, используем bisect_right

        # Создадим r_list один раз
        # Чтобы не создавать каждый раз, вынесем вне цикла

        # Сделаем это один раз перед циклом
        break

    # Вынесем подготовку вне цикла
if __name__ == "__main__":
    import sys
    import bisect

    N, M, A, B = map(int, sys.stdin.readline().split())
    bad_intervals = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]

    good_intervals = []
    prev_end = 0
    for L, R in bad_intervals:
        if prev_end + 1 <= L - 1:
            good_intervals.append((prev_end + 1, L - 1))
        prev_end = R
    if prev_end + 1 <= N:
        good_intervals.append((prev_end + 1, N))

    # Найдем индекс интервала, содержащего 1
    start_idx = -1
    for i, (l, r) in enumerate(good_intervals):
        if l <= 1 <= r:
            start_idx = i
            break
    if start_idx == -1:
        print("No")
        sys.exit()

    max_reach = [0] * len(good_intervals)
    max_reach[start_idx] = 1

    from collections import deque
    queue = deque()
    queue.append(start_idx)

    l_list = [interval[0] for interval in good_intervals]
    r_list = [interval[1] for interval in good_intervals]

    while queue:
        i = queue.popleft()
        l, r = good_intervals[i]
        cur_max = max_reach[i]

        # Расширяем max_reach внутри интервала
        new_max = min(r, cur_max + B)
        if new_max > cur_max:
            max_reach[i] = new_max
            cur_max = new_max

        if cur_max == N:
            print("Yes")
            sys.exit()

        # Рассчитаем диапазон достижимых позиций после прыжка
        jump_min = l + A
        jump_max = cur_max + B
        if jump_min > N:
            continue
        if jump_max > N:
            jump_max = N

        # Найдем индексы интервалов, пересекающих [jump_min, jump_max]
        # Интервал пересекается, если r >= jump_min и l <= jump_max

        # left_idx: первый интервал с r >= jump_min
        left_idx = bisect.bisect_left(r_list, jump_min)
        # right_idx: последний интервал с l <= jump_max
        right_idx = bisect.bisect_right(l_list, jump_max) - 1

        if left_idx > right_idx:
            continue

        # Для каждого такого интервала обновим max_reach
        for j in range(left_idx, right_idx + 1):
            lj, rj = good_intervals[j]
            # Новая достижимая позиция в интервале j:
            # max_reach[j] = max(max_reach[j], min(rj, jump_max))
            # Но нужно учесть, что прыжок может быть не из начала lj, а из позиции x в [l, cur_max]
            # Чтобы быть точнее, миним достижимая позиция в j - lj
            # Максимальная достижимая позиция - min(rj, jump_max)
            # Мы можем достичь позиции max(lj, jump_min) до min(rj, jump_max)
            # Но для упрощения обновим max_reach[j] до min(rj, jump_max)

            new_pos = min(rj, jump_max)
            if new_pos > max_reach[j]:
                max_reach[j] = new_pos
                queue.append(j)

    print("No")