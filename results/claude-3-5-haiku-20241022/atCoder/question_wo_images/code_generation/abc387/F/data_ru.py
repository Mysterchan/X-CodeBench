def solve():
    MOD = 998244353
    N, M = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    
    # Строим граф: i -> A[i]
    # Находим SCC (циклы)
    visited = [False] * (N + 1)
    scc_id = [0] * (N + 1)
    scc_count = 0
    
    def find_cycle(start):
        path = []
        curr = start
        seen = {}
        while curr not in seen and not visited[curr]:
            seen[curr] = len(path)
            path.append(curr)
            curr = A[curr]
        
        if visited[curr]:
            # Попали в уже обработанную компоненту
            for v in path:
                visited[v] = True
                scc_id[v] = scc_count
            return []
        
        # Найден цикл
        cycle_start_idx = seen[curr]
        cycle = path[cycle_start_idx:]
        return cycle
    
    cycles = []
    for i in range(1, N + 1):
        if not visited[i]:
            cycle = find_cycle(i)
            if cycle:
                for v in cycle:
                    visited[v] = True
                    scc_id[v] = scc_count
                cycles.append(cycle)
                scc_count += 1
            else:
                # Обходим путь до цикла
                curr = i
                while not visited[curr]:
                    visited[curr] = True
                    scc_id[curr] = scc_count
                    curr = A[curr]
    
    # Для каждой вершины вычисляем количество допустимых значений
    # dp[i] = количество способов назначить значения поддереву с корнем i
    dp = [0] * (N + 1)
    
    # Строим обратный граф
    rev_graph = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        rev_graph[A[i]].append(i)
    
    # Обрабатываем в порядке от циклов к листьям
    in_cycle = [False] * (N + 1)
    for cycle in cycles:
        for v in cycle:
            in_cycle[v] = True
    
    def dfs(v):
        if dp[v] > 0:
            return dp[v]
        
        if in_cycle[v]:
            # Вершина в цикле: M вариантов, все вершины цикла имеют одно значение
            result = M
        else:
            # Не в цикле: может быть <= x[A[v]]
            result = 1
        
        for u in rev_graph[v]:
            if not in_cycle[u]:
                result = (result * dfs(u)) % MOD
        
        dp[v] = result
        return result
    
    # Вычисляем ответ
    ans = 1
    for cycle in cycles:
        # Для цикла: M вариантов для общего значения
        cycle_contrib = M
        # Умножаем на вклад всех деревьев, ведущих в цикл
        for v in cycle:
            for u in rev_graph[v]:
                if not in_cycle[u]:
                    cycle_contrib = (cycle_contrib * dfs(u)) % MOD
        ans = (ans * cycle_contrib) % MOD
    
    print(ans)

solve()