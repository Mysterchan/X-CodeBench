def solve_case():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort()
    
    def check(max_val):
        # Проверяем, можем ли мы достичь максимума <= max_val
        # Используем жадный подход с двумя указателями
        used = [False] * n
        
        for bi in b:
            # Для каждого b[i] ищем подходящий a[j]
            found = False
            
            # Случай 1: (a[j] + bi) % m <= max_val и a[j] + bi < m
            # Это означает a[j] <= max_val - bi
            if max_val >= bi:
                target = max_val - bi
                for j in range(n):
                    if not used[j] and a[j] <= target:
                        used[j] = True
                        found = True
                        break
            
            if not found:
                # Случай 2: (a[j] + bi) % m <= max_val и a[j] + bi >= m
                # Это означает (a[j] + bi - m) <= max_val
                # a[j] <= max_val + m - bi
                # И a[j] + bi >= m, т.е. a[j] >= m - bi
                lower = m - bi
                upper = max_val + m - bi
                for j in range(n - 1, -1, -1):
                    if not used[j] and lower <= a[j] <= upper:
                        used[j] = True
                        found = True
                        break
            
            if not found:
                return False
        
        return True
    
    # Бинарный поиск по ответу
    left, right = 0, m - 1
    
    while left < right:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1
    
    return left

t = int(input())
for _ in range(t):
    print(solve_case())