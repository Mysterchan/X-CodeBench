def can_buy(k, prices, M):
    # Проверяем, можем ли мы купить k единиц товаров с бюджетом M
    # Оптимально покупать товары с минимальными ценами
    # Для каждого товара нужно решить, сколько единиц купить
    
    # Сортируем цены
    sorted_prices = sorted(prices)
    
    # Жадно распределяем k единиц по товарам с минимальными ценами
    # Для минимизации стоимости при покупке k единиц,
    # нужно распределить их как можно более равномерно по самым дешевым товарам
    
    n = len(sorted_prices)
    total_cost = 0
    
    # Распределяем k единиц по n товарам
    base = k // n  # базовое количество для каждого товара
    extra = k % n  # дополнительные единицы
    
    # Первые extra товаров получают base+1 единиц
    for i in range(extra):
        count = base + 1
        total_cost += count * count * sorted_prices[i]
        if total_cost > M:
            return False
    
    # Остальные товары получают base единиц
    for i in range(extra, n):
        count = base
        total_cost += count * count * sorted_prices[i]
        if total_cost > M:
            return False
    
    return total_cost <= M

def solve():
    N, M = map(int, input().split())
    prices = list(map(int, input().split()))
    
    # Бинарный поиск по количеству единиц
    left, right = 0, 10**18
    
    while left < right:
        mid = (left + right + 1) // 2
        if can_buy(mid, prices, M):
            left = mid
        else:
            right = mid - 1
    
    print(left)

solve()