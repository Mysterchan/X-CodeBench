import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        H, W = map(int, input().split())
        grid = [input().strip() for __ in range(H)]

        # Преобразуем сетку в битовую маску: 1 - черная, 0 - белая
        black = 0
        for i in range(H):
            for j in range(W):
                if grid[i][j] == '#':
                    black |= 1 << (i * W + j)

        # Проверка, что в раскраске нет 2x2 полностью черных квадратов
        def valid(mask):
            for i in range(H - 1):
                for j in range(W - 1):
                    # Проверяем 4 клетки 2x2 блока
                    # Если все 4 черные (1), то invalid
                    pos = [i * W + j, i * W + (j + 1), (i + 1) * W + j, (i + 1) * W + (j + 1)]
                    if all((mask & (1 << p)) != 0 for p in pos):
                        return False
            return True

        # Нужно перекрасить некоторые черные клетки в белые
        # То есть из black убрать некоторые биты, чтобы valid(mask) == True
        # Минимизируем количество перекрашенных (удаленных) черных клеток

        # Переберем подмножества черных клеток, которые перекрашиваем в белые
        # mask - множество черных клеток после перекраски
        # mask = black & ~remove_mask, где remove_mask - подмножество black

        # Перебор по подмножествам black, минимизируя количество удаленных бит
        # H,W <=7 => максимум 49 клеток, но черных может быть меньше
        # Перебор всех подмножеств черных клеток может быть слишком большим (2^число_черных)
        # Но H,W <=7, T<=100, можно попробовать перебор с отсечками

        # Получим список позиций черных клеток
        black_positions = [i for i in range(H*W) if (black & (1 << i)) != 0]
        n_black = len(black_positions)

        # Если нет черных или уже валидно, ответ 0
        if n_black == 0 or valid(black):
            print(0)
            continue

        # Перебор по количеству перекрашенных от 1 до n_black
        # Перебираем все подмножества размера k из black_positions
        # Для перебора подмножеств используем битмаски от 0 до 2^n_black-1
        # Отсеиваем по количеству бит

        from math import inf
        ans = inf

        # Для ускорения проверок можно кэшировать valid, но не обязательно

        # Перебор по количеству перекрашенных
        for removed_count in range(1, n_black + 1):
            # Перебор подмножеств размера removed_count
            # Используем битмаски от 0 до 2^n_black-1
            # Отсеиваем по количеству бит
            # При достижении первого решения с минимальным removed_count - выводим и прерываем
            # Чтобы ускорить, можно использовать генератор подмножеств фиксированного размера

            # Генератор подмножеств фиксированного размера k из n элементов
            def subsets_of_size_k(n, k):
                # Используем алгоритм генерации комбинаций в битмасках
                # Начинаем с (1<<k)-1
                comb = (1 << k) - 1
                limit = 1 << n
                while comb < limit:
                    yield comb
                    c = comb & -comb
                    r = comb + c
                    comb = (((r ^ comb) >> 2) // c) | r

            for remove_mask in subsets_of_size_k(n_black, removed_count):
                # Формируем маску после удаления
                mask = black
                for idx in range(n_black):
                    if (remove_mask & (1 << idx)) != 0:
                        mask &= ~(1 << black_positions[idx])
                if valid(mask):
                    ans = removed_count
                    break
            if ans != inf:
                break

        print(ans if ans != inf else 0)

if __name__ == "__main__":
    solve()