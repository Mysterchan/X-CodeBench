import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = input().strip()
    B = input().strip()

    # Получаем позиции фигур в A и B
    posA = [i for i, ch in enumerate(A) if ch == '1']
    posB = [i for i, ch in enumerate(B) if ch == '1']

    # Проверка на равенство количества фигур
    if len(posA) != len(posB):
        print(-1)
        continue

    # Минимальное количество операций - сумма абсолютных сдвигов по парам
    # При этом порядок фигур сохраняется, т.к. фигуры не могут "перескочить" друг друга
    # (операция сдвига всех фигур относительно выбранного i не меняет порядок фигур)
    res = 0
    for a, b in zip(posA, posB):
        res += abs(a - b)

    print(res)