def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # dp[i][j] = максимальный счет для подпоследовательности a[i:j+1]
    # при условии, что все элементы удалены
    dp = {}
    
    def rec(i, j):
        # Базовый случай: если элементов меньше 2, счет = 0
        if j - i < 1:
            return 0
        
        # Если уже вычислено
        if (i, j) in dp:
            return dp[(i, j)]
        
        result = 0
        
        # Пробуем все способы разбиения
        # Выбираем, какие два элемента удалим последними
        for k in range(i, j):
            # Удаляем последними элементы на позициях k и k+1
            # (после того как все между ними уже удалены)
            # Нужно рассмотреть случай, когда между k и k+1 удалены все элементы
            
            # Но на самом деле нам нужно думать по-другому:
            # Какие два элемента станут соседними в конце?
            
            # Попробуем другой подход: для каждой пары (left, right)
            # где left и right станут соседними после удаления всего между ними
            for m in range(i, j + 1):
                for p in range(m + 1, j + 1):
                    # Элементы на позициях m и p станут соседними
                    # Удаляем их и получаем счет |a[m] - a[p]|
                    score = abs(a[m] - a[p])
                    
                    # Нужно проверить, можем ли мы удалить все между ними
                    # и все вне этой пары в пределах [i, j]
                    
                    # Количество элементов между m и p
                    between = p - m - 1
                    # Количество элементов слева от m (в пределах [i, j])
                    left_count = m - i
                    # Количество элементов справа от p (в пределах [i, j])
                    right_count = j - p
                    
                    # Всего элементов кроме m и p
                    total_others = left_count + between + right_count
                    
                    # Можем удалить все, если количество четное
                    if total_others % 2 == 0:
                        # Вычисляем оптимальный счет для каждой части
                        left_score = rec(i, m - 1) if m > i else 0
                        middle_score = rec(m + 1, p - 1) if p > m + 1 else 0
                        right_score = rec(p + 1, j) if p < j else 0
                        
                        total = score + left_score + middle_score + right_score
                        result = max(result, total)
        
        # Также рассмотрим случай, когда мы не удаляем все элементы
        # (оставляем один)
        if (j - i + 1) % 2 == 1:
            # Нечетное количество элементов - один останется
            for skip in range(i, j + 1):
                # Оставляем элемент на позиции skip
                left_score = rec(i, skip - 1) if skip > i else 0
                right_score = rec(skip + 1, j) if skip < j else 0
                result = max(result, left_score + right_score)
        
        dp[(i, j)] = result
        return result
    
    print(rec(0, n - 1))

solve()