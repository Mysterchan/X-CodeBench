import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for __ in range(n)]

    # Предварительно вычислим максимум в каждой строке и столбце
    max_row = [max(row) for row in a]
    max_col = [max(a[i][j] for i in range(n)) for j in range(m)]

    # Для каждой строки и столбца вычислим максимум после уменьшения на 1
    # Но нужно учитывать, что уменьшение происходит для всех элементов в строке и столбце,
    # а максимальное значение в матрице после операции - максимум среди:
    # - элементов в выбранной строке и столбце уменьшенных на 1
    # - элементов вне выбранной строки и столбца без изменений

    # Чтобы быстро вычислять максимум вне выбранной строки и столбца,
    # используем префиксные и суффиксные максимумы для строк и столбцов.

    # Но проще: максимальное значение после операции будет максимум из:
    # - max_row[r] - 1 (т.к. вся строка r уменьшена на 1)
    # - max_col[c] - 1 (т.к. весь столбец c уменьшен на 1)
    # - максимум среди всех элементов, не в строке r и не в столбце c (без изменений)

    # Чтобы быстро находить максимум вне строки r и столбца c,
    # можно найти глобальный максимум и проверить, не находится ли он в строке r или столбце c.
    # Но это сложно, т.к. может быть несколько максимумов.

    # Оптимальный подход:
    # Для каждого элемента a[i][j], после операции (r,c):
    # - если i == r or j == c: a[i][j] - 1
    # - else: a[i][j]
    #
    # Максимум после операции = max(
    #   max_row[r] - 1,
    #   max_col[c] - 1,
    #   max element outside row r and column c
    # )
    #
    # Чтобы быстро находить max element outside row r and column c,
    # можно для каждой строки и столбца хранить максимум и второй максимум.
    # Тогда при исключении строки r и столбца c можно быстро найти максимум вне них.

    # Построим массивы максимумов и вторых максимумов для строк и столбцов
    # для быстрого вычисления максимума вне выбранной строки или столбца.

    # Для строк:
    max1_row = [(-1, -1)] * n  # (max_value, index)
    max2_row = [(-1, -1)] * n  # (second_max_value, index)
    for i in range(n):
        mx1 = -1
        mx2 = -1
        idx1 = -1
        idx2 = -1
        for j in range(m):
            val = a[i][j]
            if val > mx1:
                mx2, idx2 = mx1, idx1
                mx1, idx1 = val, j
            elif val > mx2:
                mx2, idx2 = val, j
        max1_row[i] = (mx1, idx1)
        max2_row[i] = (mx2, idx2)

    # Для столбцов:
    max1_col = [(-1, -1)] * m  # (max_value, index)
    max2_col = [(-1, -1)] * m  # (second_max_value, index)
    for j in range(m):
        mx1 = -1
        mx2 = -1
        idx1 = -1
        idx2 = -1
        for i in range(n):
            val = a[i][j]
            if val > mx1:
                mx2, idx2 = mx1, idx1
                mx1, idx1 = val, i
            elif val > mx2:
                mx2, idx2 = val, i
        max1_col[j] = (mx1, idx1)
        max2_col[j] = (mx2, idx2)

    # Теперь для каждого выбора (r, c) вычислим максимум вне строки r и столбца c:
    # Максимум вне строки r - это максимум среди всех строк, кроме r.
    # Аналогично для столбца c.
    # Но нам нужно максимум среди элементов, которые не в строке r и не в столбце c.
    #
    # Рассмотрим максимум вне строки r:
    # max_row_except_r = max(max_row[i] for i != r)
    # Аналогично для столбца.
    #
    # Но это O(n*m) если делать напрямую.
    #
    # Оптимизация:
    # Можно найти глобальный максимум и второй максимум по строкам и столбцам.
    # Тогда для исключения строки r:
    # - если max_row[r] == global_max_row, то максимум вне r = global_second_max_row
    # - иначе максимум вне r = global_max_row
    #
    # Аналогично для столбцов.

    # Найдем глобальный и второй глобальный максимум по строкам
    global_max_row = -1
    global_max_row_idx = -1
    global_second_max_row = -1
    for i in range(n):
        if max_row[i] > global_max_row:
            global_second_max_row = global_max_row
            global_max_row = max_row[i]
            global_max_row_idx = i
        elif max_row[i] > global_second_max_row:
            global_second_max_row = max_row[i]

    # Аналогично для столбцов
    global_max_col = -1
    global_max_col_idx = -1
    global_second_max_col = -1
    for j in range(m):
        if max_col[j] > global_max_col:
            global_second_max_col = global_max_col
            global_max_col = max_col[j]
            global_max_col_idx = j
        elif max_col[j] > global_second_max_col:
            global_second_max_col = max_col[j]

    # Теперь для каждого (r, c) максимум вне строки r и столбца c:
    # max_outside = max(
    #   max_row_except_r,
    #   max_col_except_c
    # )
    #
    # max_row_except_r = global_second_max_row if r == global_max_row_idx else global_max_row
    # max_col_except_c = global_second_max_col if c == global_max_col_idx else global_max_col

    # Но это максимум по строкам и максимум по столбцам, а нам нужен максимум среди элементов,
    # которые не в строке r и не в столбце c одновременно.
    #
    # Рассмотрим, что максимум вне строки r и столбца c - это максимум среди элементов,
    # которые не в строке r и не в столбце c.
    #
    # Чтобы найти такой максимум, можно:
    # - Для каждого элемента a[i][j], если i != r и j != c, то он не уменьшается.
    #
    # Но перебор всех элементов для каждого (r,c) невозможен.
    #
    # Альтернативный подход:
    # Максимум после операции = max(
    #   max_row[r] - 1,
    #   max_col[c] - 1,
    #   max_element_outside_row_r_and_col_c
    # )
    #
    # max_element_outside_row_r_and_col_c - это максимум среди элементов, не в строке r и не в столбце c.
    #
    # Если мы заранее для каждого элемента знаем, что он не в строке r и не в столбце c,
    # то можем найти максимум среди таких элементов.
    #
    # Но это сложно.
    #
    # Попробуем другой подход:
    #
    # Рассмотрим максимум среди всех элементов, кроме тех, что в строке r или столбце c.
    #
    # Для этого можно для каждого элемента a[i][j] создать массив значений,
    # и для каждой строки и столбца хранить максимум и второй максимум.
    #
    # Но это сложно.
    #
    # Попробуем перебрать все (r,c) и вычислить максимум после операции:
    # max_after = max(
    #   max_row[r] - 1,
    #   max_col[c] - 1,
    #   max_element_outside_row_r_and_col_c
    # )
    #
    # max_element_outside_row_r_and_col_c = max(
    #   max_row_except_r,
    #   max_col_except_c
    # )
    #
    # Но это не гарантирует, что элемент не в строке r и не в столбце c одновременно.
    #
    # Однако, если мы возьмем максимум среди всех элементов, кроме строки r и столбца c,
    # то это будет максимум среди элементов, которые не уменьшились.
    #
    # Чтобы быстро находить максимум вне строки r и столбца c, можно:
    # - Для каждой строки i, кроме r, взять max_row[i]
    # - Для каждого столбца j, кроме c, взять max_col[j]
    #
    # Максимум вне строки r и столбца c будет максимумом среди max_row[i] для i != r и max_col[j] для j != c,
    # но это не гарантирует, что элемент не в строке r или столбце c одновременно.
    #
    # Пример:
    # Если максимальный элемент вне строки r - это элемент в столбце c, он уменьшится.
    #
    # Значит, нужно искать максимум среди элементов, не в строке r и не в столбце c.
    #
    # Для этого можно:
    # - Для каждого элемента a[i][j], добавить его в структуру по координатам.
    # - Для каждого (r,c) искать максимум среди элементов, где i != r и j != c.
    #
    # Но это слишком дорого.
    #
    # Оптимизация:
    # Можно для каждого элемента a[i][j] считать, что он уменьшится, если i == r или j == c.
    # Значит, если элемент не в строке r и не в столбце c, он не изменится.
    #
    # Максимум после операции = max(
    #   max_row[r] - 1,
    #   max_col[c] - 1,
    #   max_element_not_in_row_r_and_not_in_col_c
    # )
    #
    # Чтобы быстро находить max_element_not_in_row_r_and_not_in_col_c,
    # можно для каждого элемента a[i][j] добавить его в структуру.
    #
    # Но перебор всех (r,c) невозможен.
    #
    # Итог:
    # Переберем все (r,c) и вычислим максимум после операции.
    # Но n*m может быть до 10^5, перебор всех (r,c) невозможен.
    #
    # Значит, нужно перебрать либо все строки, либо все столбцы.
    #
    # Попробуем перебрать все строки r:
    # Для каждой строки r, вычислим максимум вне строки r (max_row_except_r)
    # Для каждого столбца c, вычислим максимум вне столбца c (max_col_except_c)
    #
    # Максимум вне строки r и столбца c будет максимумом среди элементов,
    # не в строке r и не в столбце c.
    #
    # Но это сложно.
    #
    # Попробуем другой подход:
    #
    # Рассмотрим максимум среди всех элементов, кроме тех, что в строке r или столбце c.
    #
    # Для этого можно:
    # - Для каждой строки i, кроме r, взять max_row[i]
    # - Для каждого столбца j, кроме c, взять max_col[j]
    #
    # Максимум вне строки r и столбца c будет максимумом среди max_row_except_r и max_col_except_c,
    # но это не гарантирует, что элемент не в строке r или столбце c одновременно.
    #
    # Однако, если мы возьмем максимум среди max_row_except_r и max_col_except_c,
    # то это будет верхняя оценка максимума вне строки r и столбца c.
    #
    # Значит, максимум после операции будет не меньше max(
    #   max_row[r] - 1,
    #   max_col[c] - 1,
    #   max(max_row_except_r, max_col_except_c)
    # )
    #
    # Попробуем использовать эту оценку.
    #
    # Для каждого (r,c) вычислим:
    # max_after = max(
    #   max_row[r] - 1,
    #   max_col[c] - 1,
    #   max(max_row_except_r, max_col_except_c)
    # )
    #
    # max_row_except_r = global_second_max_row if r == global_max_row_idx else global_max_row
    # max_col_except_c = global_second_max_col if c == global_max_col_idx else global_max_col

    # Переберем все (r,c) и найдем минимальный max_after
    # Но перебор всех (r,c) невозможен (до 10^5 элементов).
    #
    # Попробуем перебрать все r и для каждого r найти лучший c.
    #
    # Для фиксированного r:
    # max_row_except_r = global_second_max_row if r == global_max_row_idx else global_max_row
    #
    # Для каждого c:
    # max_col_except_c = global_second_max_col if c == global_max_col_idx else global_max_col
    #
    # max_after = max(
    #   max_row[r] - 1,
    #   max_col[c] - 1,
    #   max(max_row_except_r, max_col_except_c)
    # )
    #
    # Чтобы найти минимальный max_after для фиксированного r,
    # нужно перебрать все c и выбрать минимальный max_after.
    #
    # Аналогично можно перебрать все c и для каждого c перебрать r.
    #
    # Но это O(n*m), что может быть до 10^5, что возможно.

    # Реализуем перебор всех (r,c) и вычислим минимальный max_after.

    ans = 10**9
    for r in range(n):
        max_row_except_r = global_second_max_row if r == global_max_row_idx else global_max_row
        row_val = max_row[r] - 1
        for c in range(m):
            max_col_except_c = global_second_max_col if c == global_max_col_idx else global_max_col
            col_val = max_col[c] - 1
            max_outside = max(max_row_except_r, max_col_except_c)
            cur_max = max(row_val, col_val, max_outside)
            if cur_max < ans:
                ans = cur_max

    print(ans)