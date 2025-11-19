import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    U = list(map(int, input().split()))
    D = list(map(int, input().split()))
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))

    # Минимальное значение на верхней и нижней гранях
    min_ud = min(min(U), min(D))
    # Минимальное значение на левой и правой гранях
    min_lr = min(min(L), min(R))

    # Минимальная стоимость - сумма минимальных значений с двух разных сторон
    # Выбираем пару клеток, одна из верх/низ, другая из лево/право
    ans = min_ud + min_lr

    print(ans)