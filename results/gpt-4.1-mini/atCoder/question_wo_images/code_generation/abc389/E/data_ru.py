import sys
input = sys.stdin.readline

N, M = map(int, input().split())
P = list(map(int, input().split()))

# Функция для проверки, можно ли купить total_units единиц при бюджете M
def can_buy(total_units):
    # Для минимизации суммы k_i^2 * P_i при фиксированной сумме k_i = total_units,
    # оптимально распределить units пропорционально 1/sqrt(P_i).
    # Формула для k_i:
    # k_i = total_units * (1/sqrt(P_i)) / sum_j (1/sqrt(P_j))
    # Тогда сумма стоимости:
    # sum_i k_i^2 * P_i = total_units^2 / (sum_j 1/sqrt(P_j))^2 * sum_i P_i / P_i = total_units^2 / (sum_j 1/sqrt(P_j))^2 * N
    # Но это неверно, нужно посчитать точнее.

    # Рассчитаем sum_inv_sqrt = sum_i 1/sqrt(P_i)
    # Тогда k_i = total_units * (1/sqrt(P_i)) / sum_inv_sqrt
    # Стоимость = sum_i (k_i^2 * P_i) = total_units^2 / (sum_inv_sqrt^2) * sum_i (P_i / P_i) = total_units^2 / (sum_inv_sqrt^2) * N
    # Но sum_i (k_i^2 * P_i) = total_units^2 / (sum_inv_sqrt^2) * sum_i P_i / P_i = total_units^2 / (sum_inv_sqrt^2) * N
    # Это неверно, т.к. P_i / P_i = 1, но мы должны учитывать P_i * (k_i)^2.

    # Правильнее:
    # k_i = total_units * (1/sqrt(P_i)) / sum_inv_sqrt
    # k_i^2 * P_i = (total_units^2 * (1/P_i) / (sum_inv_sqrt^2)) * P_i = total_units^2 / (sum_inv_sqrt^2)
    # sum_i k_i^2 * P_i = N * total_units^2 / (sum_inv_sqrt^2)
    # Но это не учитывает, что сумма k_i^2 * P_i = total_units^2 / (sum_inv_sqrt^2) * sum_i 1 = total_units^2 * N / (sum_inv_sqrt^2)

    # Однако, sum_i k_i^2 * P_i = total_units^2 / (sum_inv_sqrt^2) * sum_i 1 = total_units^2 * N / (sum_inv_sqrt^2)
    # Это неверно, т.к. sum_i 1 = N, но мы должны учитывать P_i.

    # Перепишем:
    # k_i = total_units * (1/sqrt(P_i)) / sum_inv_sqrt
    # k_i^2 * P_i = total_units^2 * (1/P_i) / (sum_inv_sqrt^2) * P_i = total_units^2 / (sum_inv_sqrt^2)
    # sum_i k_i^2 * P_i = sum_i total_units^2 / (sum_inv_sqrt^2) = N * total_units^2 / (sum_inv_sqrt^2)

    # Значит стоимость = N * total_units^2 / (sum_inv_sqrt^2)

    # Проверим на примере:
    # Sample Input 1:
    # P = [4,1,9]
    # sqrt(P) = [2,1,3]
    # 1/sqrt(P) = [0.5,1,0.3333]
    # sum_inv_sqrt = 1.8333
    # N=3
    # Стоимость = 3 * total_units^2 / (1.8333^2) = 3 * total_units^2 / 3.3611 = 0.892 * total_units^2
    # При total_units=3 стоимость ~ 0.892 * 9 = 8.03 < 9, подходит.
    # При total_units=4 стоимость ~ 0.892 * 16 = 14.27 > 9, не подходит.
    # Совпадает с примером.

    # Таким образом, можно использовать эту формулу для проверки.

    return N * total_units * total_units <= M * (sum_inv_sqrt * sum_inv_sqrt)

sum_inv_sqrt = 0.0
for p in P:
    sum_inv_sqrt += 1.0 / (p ** 0.5)

left, right = 0, 10**19  # достаточно большой верхний предел

while left < right:
    mid = (left + right + 1) // 2
    if can_buy(mid):
        left = mid
    else:
        right = mid - 1

print(left)