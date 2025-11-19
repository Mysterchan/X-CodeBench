import sys
input = sys.stdin.readline

def cover_1d(l, r):
    # Возвращает минимальное количество отрезков вида [a*2^k, (a+1)*2^k], покрывающих [l,r]
    # Алгоритм: жадно выбираем максимально возможный блок слева
    count = 0
    cur = l
    while cur < r:
        length = 1 << (r - cur).bit_length() - 1  # максимальная степень двойки <= r-cur
        # Подвинем length вниз, чтобы блок [cur, cur+length] был aligned (начинается с кратного length)
        while cur % length != 0:
            length >>= 1
        count += 1
        cur += length
    return count

t = int(input())
for _ in range(t):
    l1, r1, l2, r2 = map(int, input().split())
    # Минимальное количество узлов = произведение минимального покрытия по x и по y
    print(cover_1d(l1, r1) * cover_1d(l2, r2))