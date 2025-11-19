def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    total = 0
    
    for L in range(n):
        for R in range(L, n):
            # Вычисляем f(L, R)
            subarray = a[L:R+1]
            total += calculate_f(subarray)
    
    print(total)

def calculate_f(arr):
    if not arr:
        return 0
    
    # Используем динамическое программирование
    n = len(arr)
    memo = {}
    
    def dp(mask):
        if mask == 0:
            return 0
        
        if mask in memo:
            return memo[mask]
        
        # Находим элементы, которые еще есть
        present = []
        for i in range(n):
            if mask & (1 << i):
                present.append(arr[i])
        
        if not present:
            return 0
        
        min_val = min(present)
        max_val = max(present)
        
        result = float('inf')
        
        # Пробуем каждый возможный диапазон [l, r]
        for l in range(min_val, max_val + 1):
            for r in range(l, max_val + 1):
                # Создаем новую маску после удаления элементов в диапазоне [l, r]
                new_mask = mask
                can_remove = True
                
                for i in range(n):
                    if (mask & (1 << i)) and l <= arr[i] <= r:
                        new_mask &= ~(1 << i)
                
                if new_mask != mask:  # Что-то было удалено
                    result = min(result, 1 + dp(new_mask))
        
        memo[mask] = result
        return result
    
    initial_mask = (1 << n) - 1
    return dp(initial_mask)

solve()