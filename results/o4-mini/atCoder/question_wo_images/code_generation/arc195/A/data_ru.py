def has_multiple_subsequences(N, M, A, B):
    # Словарь для хранения индексов каждого элемента A
    from collections import defaultdict
    
    index_map = defaultdict(list)
    
    # Заполняем словарь индексами
    for i in range(N):
        index_map[A[i]].append(i)
    
    # Проверяем, можем ли мы найти B в A
    last_index = -1
    for b in B:
        if b not in index_map:
            return "No"
        
        # Находим первый индекс в A, который больше last_index
        found = False
        for idx in index_map[b]:
            if idx > last_index:
                last_index = idx
                found = True
                break
        
        if not found:
            return "No"
    
    # Теперь проверяем, можем ли мы найти B еще раз
    last_index = -1
    count = 0
    for b in B:
        if b not in index_map:
            return "No"
        
        # Находим первый индекс в A, который больше last_index
        found = False
        for idx in index_map[b]:
            if idx > last_index:
                last_index = idx
                found = True
                break
        
        if not found:
            count += 1
            last_index = -1  # Сбрасываем last_index для новой попытки
    
    return "Yes" if count >= 1 else "No"

# Чтение входных данных
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Вывод результата
print(has_multiple_subsequences(N, M, A, B))