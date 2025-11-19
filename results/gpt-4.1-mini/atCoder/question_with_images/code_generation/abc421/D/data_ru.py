import sys
import math
input = sys.stdin.readline

# Перевод символа в дельту координат (r,c)
delta = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

def main():
    R_t, C_t, R_a, C_a = map(int, input().split())
    N, M, L = map(int, input().split())

    S_chars = []
    S_counts = []
    for _ in range(M):
        ch, cnt = input().split()
        cnt = int(cnt)
        S_chars.append(ch)
        S_counts.append(cnt)

    T_chars = []
    T_counts = []
    for _ in range(L):
        ch, cnt = input().split()
        cnt = int(cnt)
        T_chars.append(ch)
        T_counts.append(cnt)

    # Распакуем S и T в списки ходов по блокам (символ, длина)
    # Но не будем разворачивать полностью, т.к. N очень велик

    # Для удобства создадим списки с дельтами и длинами
    S = [(delta[ch], cnt) for ch, cnt in zip(S_chars, S_counts)]
    T = [(delta[ch], cnt) for ch, cnt in zip(T_chars, T_counts)]

    # Общая длина N = сумма A_i = сумма B_i

    # Идея решения:
    # Ходы идут одновременно.
    # Нужно посчитать количество i (1<=i<=N), для которых позиции совпадают после i-го хода.

    # Позиции после i-го хода:
    # pos_T(i) = (R_t, C_t) + sum_{k=1}^i dS_k
    # pos_A(i) = (R_a, C_a) + sum_{k=1}^i dT_k
    # Нужно посчитать количество i, для которых pos_T(i) == pos_A(i)

    # Рассмотрим разницу позиций:
    # diff(i) = pos_T(i) - pos_A(i) = (R_t - R_a, C_t - C_a) + sum_{k=1}^i (dS_k - dT_k)
    # Нужно посчитать количество i, для которых diff(i) == (0,0)

    # Поскольку N очень велико, и S и T заданы блоками,
    # будем идти по блокам, синхронизируя их.

    # Алгоритм:
    # Идем по блокам S и T параллельно, разбивая ход на минимальные общие части.
    # На каждом таком минимальном отрезке длины l:
    # - dS_step = дельта S за один ход
    # - dT_step = дельта T за один ход
    # - diff_step = dS_step - dT_step
    # diff(i) меняется линейно на этом отрезке:
    # diff(i) = diff_start + diff_step * (i - start_index)
    # Нужно посчитать количество i в [start_index+1, start_index+l], для которых diff(i) == (0,0)

    # Решаем уравнение:
    # diff_start + diff_step * k = (0,0), k=1..l
    # Если diff_step == (0,0):
    #   Если diff_start == (0,0), то все k=1..l подходят
    #   Иначе 0
    # Если diff_step != (0,0):
    #   Нужно найти k, для которого diff_start + diff_step * k = 0
    #   То есть k = -diff_start / diff_step (по обеим координатам)
    #   k должно быть целым и в [1,l]

    # Важно: diff_step может быть (dr, dc), где dr и dc - целые числа
    # Нужно проверить, что k одинаково подходит для r и c

    # Начинаем с diff = (R_t - R_a, C_t - C_a)
    # Идем по блокам, считаем ответ

    i_s = 0  # индекс блока S
    i_t = 0  # индекс блока T
    pos_s = 0  # сколько ходов уже прошло в S
    pos_t = 0  # сколько ходов уже прошло в T

    # Текущие остатки в блоках
    rem_s = S[i_s][1]
    rem_t = T[i_t][1]

    diff_r = R_t - R_a
    diff_c = C_t - C_a

    ans = 0
    total_steps = 0

    while total_steps < N:
        l = min(rem_s, rem_t)  # длина текущего минимального отрезка

        dS_r, dS_c = S[i_s][0]
        dT_r, dT_c = T[i_t][0]

        diff_step_r = dS_r - dT_r
        diff_step_c = dS_c - dT_c

        # diff(i) = diff_start + diff_step * k, k=1..l

        if diff_step_r == 0 and diff_step_c == 0:
            # diff не меняется на этом отрезке
            if diff_r == 0 and diff_c == 0:
                ans += l
            # else 0
        else:
            # Нужно найти k, для которого diff_r + diff_step_r * k = 0
            # и diff_c + diff_step_c * k = 0
            # k - целое, 1 <= k <= l

            # Проверим, что решения есть
            # Если diff_step_r == 0:
            #   diff_r must be 0, иначе нет решения
            # Аналогично для diff_step_c

            # Если diff_step_r == 0 and diff_r != 0 => no solution
            # Если diff_step_c == 0 and diff_c != 0 => no solution

            # Иначе:
            # k_r = -diff_r / diff_step_r (если diff_step_r != 0)
            # k_c = -diff_c / diff_step_c (если diff_step_c != 0)
            # k_r и k_c должны быть равны и целые

            def is_int_div(a, b):
                # Проверка, что a делится на b без остатка
                return b != 0 and a % b == 0

            possible_k = None
            # Проверка по r
            if diff_step_r == 0:
                if diff_r != 0:
                    possible_k = None
                else:
                    # любое k по r
                    possible_k = 'any_r'
            else:
                if diff_r % diff_step_r != 0:
                    possible_k = None
                else:
                    k_r = -diff_r // diff_step_r
                    possible_k = k_r

            # Проверка по c
            if diff_step_c == 0:
                if diff_c != 0:
                    possible_k = None
                else:
                    # любое k по c
                    if possible_k == 'any_r':
                        # оба свободны, значит любое k
                        # но k должен быть в 1..l
                        # значит все k подходят
                        # но diff_step != 0, значит хотя бы одна координата меняется
                        # но обе свободны - значит diff_step_r или diff_step_c != 0, но мы уже проверили
                        # это невозможно, т.к. diff_step != 0
                        # значит возможна ситуация, что одна координата меняется, другая нет
                        # и diff_c == 0, diff_r == 0
                        # значит k по r фиксировано, по c любое
                        # но по r фиксировано 'any_r' - значит любое k
                        # но diff_step_r != 0, значит k_r фиксировано
                        # тут конфликт, значит нужно уточнить
                        # на самом деле, если diff_step_r != 0, possible_k уже число
                        # если diff_step_r == 0, possible_k == 'any_r'
                        # сейчас diff_step_c == 0 и diff_c == 0, значит по c любое k
                        # значит k должен быть равен k_r (число)
                        # значит possible_k = k_r
                        pass
                    # else possible_k уже число или None
            else:
                if diff_c % diff_step_c != 0:
                    possible_k = None
                else:
                    k_c = -diff_c // diff_step_c
                    if possible_k == 'any_r':
                        possible_k = k_c
                    elif possible_k is None:
                        possible_k = None
                    else:
                        # possible_k число k_r
                        if possible_k != k_c:
                            possible_k = None

            if possible_k is None:
                # нет решения
                pass
            elif possible_k == 'any_r':
                # diff_step_r == 0 and diff_r == 0
                # diff_step_c == 0 and diff_c == 0
                # но это случай diff_step == (0,0), который мы уже обработали
                # сюда не попадем
                pass
            else:
                # possible_k - число
                if 1 <= possible_k <= l:
                    ans += 1

        # Обновляем diff_r, diff_c после l ходов
        diff_r += diff_step_r * l
        diff_c += diff_step_c * l

        total_steps += l
        rem_s -= l
        rem_t -= l

        if rem_s == 0:
            i_s += 1
            if i_s < M:
                rem_s = S[i_s][1]
        if rem_t == 0:
            i_t += 1
            if i_t < L:
                rem_t = T[i_t][1]

    print(ans)

if __name__ == "__main__":
    main()