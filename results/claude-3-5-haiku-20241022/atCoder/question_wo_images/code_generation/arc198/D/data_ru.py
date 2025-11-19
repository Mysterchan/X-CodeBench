from collections import deque, defaultdict

def solve():
    N = int(input())
    
    # Строим дерево
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Читаем матрицу A
    A = []
    for _ in range(N):
        line = input().strip()
        A.append([int(c) for c in line])
    
    # Находим все пути между вершинами
    def find_path(start, end):
        if start == end:
            return [start]
        
        parent = [-1] * (N + 1)
        visited = [False] * (N + 1)
        queue = deque([start])
        visited[start] = True
        
        while queue:
            u = queue.popleft()
            if u == end:
                break
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
        
        path = []
        curr = end
        while curr != -1:
            path.append(curr)
            curr = parent[curr]
        path.reverse()
        return path
    
    # Предвычисляем все пути
    paths = {}
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            paths[(i, j)] = find_path(i, j)
    
    # Проверяем, является ли пара (i, j) палиндромной для заданного x
    def is_palindromic(i, j, x):
        path = paths[(i, j)]
        n = len(path)
        for k in range(n):
            if x[path[k] - 1] != x[path[n - 1 - k] - 1]:
                return False
        return True
    
    # Находим пары с A[i][j] = 1
    required_pairs = []
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1:
                required_pairs.append((i + 1, j + 1))
    
    # Пробуем все возможные значения для x
    # Оптимизация: ограничиваем диапазон значений
    min_score = 10**100
    
    # Используем BFS по возможным назначениям
    def try_assignments():
        nonlocal min_score
        
        # Пробуем разные максимальные значения
        for max_val in range(1, min(N + 1, 20)):
            # Перебираем все комбинации
            def backtrack(pos, x):
                nonlocal min_score
                
                if pos == N:
                    # Проверяем все обязательные пары
                    valid = True
                    for i, j in required_pairs:
                        if not is_palindromic(i, j, x):
                            valid = False
                            break
                    
                    if valid:
                        # Считаем палиндромные пары
                        count = 0
                        for i in range(1, N + 1):
                            for j in range(1, N + 1):
                                if is_palindromic(i, j, x):
                                    count += 1
                        min_score = min(min_score, count)
                    return
                
                for val in range(1, max_val + 1):
                    x.append(val)
                    backtrack(pos + 1, x)
                    x.pop()
            
            backtrack(0, [])
            
            if min_score < 10**100:
                return
    
    try_assignments()
    print(min_score)

solve()