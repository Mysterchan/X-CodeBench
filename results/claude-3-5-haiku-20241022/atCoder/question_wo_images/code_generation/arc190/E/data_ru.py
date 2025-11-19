def solve_query(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return 0
    
    # dp[i] = максимальное количество операций для подмассива arr[0:i+1]
    # при условии, что arr[i] может участвовать в парах
    
    # Используем жадный подход с динамическим программированием
    # dp[i][remainder] = максимум операций для первых i элементов,
    # где remainder - остаток в позиции i
    
    # Оптимизация: для каждой позиции храним только необходимую информацию
    
    total = sum(arr)
    max_ops = total // 2
    
    # Попробуем жадный подход с ДП
    # dp[i] = (max_operations, remainder_at_i)
    
    if n == 2:
        return min(arr[0], arr[1])
    
    # Для каждой позиции нужно решить, сколько оставить
    # Ключевая идея: можем образовывать пары с соседями на расстоянии 1 или 2
    
    # Используем ДП где состояние - (позиция, остаток на предыдущей позиции, остаток на позиции перед предыдущей)
    # Но это слишком много состояний
    
    # Упрощенный подход: для каждой позиции решаем жадно
    # На самом деле, максимум операций = min(total//2, что позволяет структура)
    
    # Правильный подход через ДП:
    # dp[i][j][k] где i - позиция, j - остаток на i-1, k - остаток на i-2
    # Но значения могут быть большими
    
    # Оптимизация: заметим, что остатки ограничены
    # Максимальный полезный остаток на позиции не превышает суммы следующих элементов
    
    # Используем ДП с хешмапом для состояний
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def dp(pos, prev1, prev2):
        if pos == n:
            return 0
        
        result = 0
        cur_val = arr[pos]
        
        # Перебираем сколько оставить на текущей позиции
        for remain in range(cur_val + 1):
            used = cur_val - remain
            ops = 0
            
            # Сколько можем спарить с prev1 (позиция pos-1)
            pair_with_prev1 = min(used, prev1)
            ops += pair_with_prev1
            used -= pair_with_prev1
            new_prev1 = prev1 - pair_with_prev1
            
            # Сколько можем спарить с prev2 (позиция pos-2)
            pair_with_prev2 = min(used, prev2)
            ops += pair_with_prev2
            used -= pair_with_prev2
            new_prev2 = prev2 - pair_with_prev2
            
            # Рекурсивно решаем для следующей позиции
            result = max(result, ops + dp(pos + 1, remain, new_prev1))
        
        return result
    
    return dp(0, 0, 0)

n, q = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(q):
    l, r = map(int, input().split())
    subarr = a[l-1:r]
    print(solve_query(subarr))