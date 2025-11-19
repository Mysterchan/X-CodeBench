def main():
    import sys
    sys.setrecursionlimit(10**7)
    L, R = map(int, sys.stdin.readline().split())

    # Число Змейка: первая (старшая) цифра строго больше всех остальных цифр.
    # Задача: посчитать количество таких чисел в [L, R].

    # Подход:
    # Используем digit DP для подсчёта количества чисел <= X, которые являются "Змейками".
    # Затем ответ = count(R) - count(L-1).

    # digit DP параметры:
    # pos - текущая позиция в числе (слева направо)
    # leading_digit - первая цифра числа (None, если ещё не выбрана)
    # max_digit - максимальная цифра, которую можно ставить на текущей позиции (ограничение по верхней границе)
    # is_limit - флаг, что текущая позиция ограничена верхней границей (т.е. цифра не может быть больше цифры X[pos])
    # is_num - флаг, что уже выбрана хотя бы одна цифра (чтобы не считать ведущие нули)
    # digits - массив цифр числа X

    # Условие "Змейка":
    # - первая выбранная цифра > всех остальных цифр
    # - значит, после выбора leading_digit, все последующие цифры < leading_digit

    from functools import lru_cache

    def digits_of(x):
        return list(map(int, str(x)))

    def count_snake(x):
        if x < 10:
            return 0  # по условию числа >= 10

        digits = digits_of(x)
        n = len(digits)

        @lru_cache(None)
        def dfs(pos, leading_digit, is_limit, is_num):
            # pos: текущая позиция
            # leading_digit: первая цифра (0-9), или -1 если ещё не выбрана
            # is_limit: ограничение верхней границей
            # is_num: выбрана ли уже цифра (чтобы не считать ведущие нули)
            if pos == n:
                # если число уже выбрано и длина >= 2 (т.к. x>=10)
                return 1 if is_num else 0

            res = 0
            up = digits[pos] if is_limit else 9

            for d in range(up + 1):
                if not is_num:
                    # ещё не выбрали первую цифру
                    # если d == 0, то число ещё не началось (ведущие нули)
                    # но по условию число >= 10, значит длина >= 2, но ведущие нули допустимы
                    # однако, число должно быть >= 10, значит длина >= 2, но ведущие нули не влияют на leading_digit
                    # чтобы не считать числа с длиной 1, мы просто не считаем числа с is_num=False в конце
                    # здесь можно выбрать d=0 и не начинать число
                    # если d>0, то это первая цифра
                    if d == 0:
                        # не начинаем число, leading_digit не меняется
                        res += dfs(pos + 1, leading_digit, is_limit and d == up, False)
                    else:
                        # выбираем первую цифру
                        # leading_digit = d
                        res += dfs(pos + 1, d, is_limit and d == up, True)
                else:
                    # число уже началось, leading_digit уже выбран
                    # условие: d < leading_digit
                    if d < leading_digit:
                        res += dfs(pos + 1, leading_digit, is_limit and d == up, True)
                    # d == leading_digit или d > leading_digit - запрещено
                    # т.к. ведущая цифра строго больше всех остальных
                    # d == leading_digit - не строго больше
                    # d > leading_digit - тоже нет
                    # значит пропускаем

            return res

        return dfs(0, -1, True, False)

    ans = count_snake(R) - count_snake(L - 1)
    print(ans)


if __name__ == "__main__":
    main()