def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    # Первые строки информации о блоках
    N, W = map(int, data[0].split())
    blocks = []
    for i in range(1, N + 1):
        x, y = map(int, data[i].split())
        blocks.append((x, y))

    # Запросы
    Q = int(data[N + 1])
    queries = []
    for j in range(N + 2, N + 2 + Q):
        T, A = map(int, data[j].split())
        queries.append((T, A - 1))  # Сохраняем индекс блока (0-индексация)

    # Надо знать максимальные высоты на каждом столбце
    # max_height[x] = максимальная высота в указанном столбце x
    max_height = {}
    for x, y in blocks:
        if x not in max_height:
            max_height[x] = y
        else:
            max_height[x] = max(max_height[x], y)

    # Определяем, будет ли блок существовать в T + 0.5
    results = []
    for T, A in queries:
        x, y = blocks[A]

        # Если указанный блок будет удален до времени T
        if y <= T:
            results.append("No")
            continue

        # Правила перемещения блока: двигаемся, пока под ним нет блока
        # по y-осевой его высота на момент T
        new_y = y

        # Есть блоки внизу?
        while True:
            # Проверяем, в каком положении находится new_y
            if new_y - 1 in max_height.values():
                if (x, new_y - 1) in blocks:
                    break  # Под ним есть блок, не можем двигаться дальше

            # Если мы не достигли нижней части во времени T
            if new_y - 1 < T:
                break

            new_y -= 1

        # После учета движения блока, догадываемся, остался ли он
        if new_y <= 0:  # Если блок достиг нуля, он уничтожается
            results.append("No")
        else:
            results.append("Yes")

    # Печатаем результаты
    print("\n".join(results))

if __name__ == "__main__":
    main()