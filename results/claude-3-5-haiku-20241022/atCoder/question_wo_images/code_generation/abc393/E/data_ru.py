import math
from collections import defaultdict

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    # Для каждого элемента найдем максимальный GCD
    result = []
    
    for i in range(N):
        target = A[i]
        
        # Найдем все делители target
        divisors = []
        d = 1
        while d * d <= target:
            if target % d == 0:
                divisors.append(d)
                if d * d != target:
                    divisors.append(target // d)
            d += 1
        
        divisors.sort(reverse=True)
        
        # Для каждого делителя проверим, можем ли мы выбрать K элементов
        max_gcd = 1
        for g in divisors:
            # Подсчитаем количество элементов, кратных g
            count = sum(1 for x in A if x % g == 0)
            if count >= K:
                max_gcd = g
                break
        
        result.append(max_gcd)
    
    for r in result:
        print(r)

solve()