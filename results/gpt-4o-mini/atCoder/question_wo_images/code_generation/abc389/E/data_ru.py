def max_products(N, M, P):
    P.sort()  # Сортируем цены по возрастанию
    total_count = 0
    for price in P:
        k = 1
        # Находим максимальное количество единиц для данного типа продукта
        while True:
            cost = k * k * price
            if cost > M:  # Если стоимость превышает бюджет, выходим из цикла
                break
            total_count += k  # Увеличиваем общее количество изделий
            M -= cost  # Уменьшаем бюджет
            k += 1  # Переходим к следующему количеству единиц

    return total_count

# Чтение входных данных
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
M = int(data[1])
P = list(map(int, data[2:N+2]))

# Вывод результата
print(max_products(N, M, P))