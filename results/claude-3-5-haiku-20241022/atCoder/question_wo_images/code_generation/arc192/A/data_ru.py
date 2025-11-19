def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # Если все уже 1, то любая строка подходит
    if all(x == 1 for x in a):
        print("Yes")
        return
    
    # Попробуем все возможные строки с помощью BFS/DFS
    # Но это слишком много вариантов. Нужен другой подход.
    
    # Ключевое наблюдение: мы можем попробовать все возможные комбинации
    # операций и проверить, можем ли мы покрыть все нули.
    
    # Давайте попробуем жадный подход с backtracking
    # Для каждой позиции с 0 пытаемся применить операцию
    
    # Альтернативный подход: попробуем построить строку S
    # Для каждой позиции i с A[i]=0, нужно применить операцию
    
    # Попробуем перебор с мемоизацией
    from collections import deque
    
    # BFS по состояниям массива A
    initial = tuple(a)
    if all(x == 1 for x in initial):
        print("Yes")
        return
    
    visited = {initial}
    queue = deque([initial])
    
    while queue:
        state = queue.popleft()
        
        # Попробуем все возможные операции
        for i in range(n):
            # Операция 1: ARC на позициях i, i+1, i+2
            i1, i2 = i, (i + 1) % n
            new_state = list(state)
            new_state[i1] = 1
            new_state[i2] = 1
            new_state_tuple = tuple(new_state)
            
            if new_state_tuple not in visited:
                if all(x == 1 for x in new_state):
                    print("Yes")
                    return
                visited.add(new_state_tuple)
                queue.append(new_state_tuple)
            
            # Операция 2: CRA на позициях i, i+1, i+2
            # (то же самое, что ARC на i-2, i-1, i)
    
    print("No")

solve()