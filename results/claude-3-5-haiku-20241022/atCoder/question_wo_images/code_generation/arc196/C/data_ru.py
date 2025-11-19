def solve():
    MOD = 998244353
    N = int(input())
    S = input().strip()
    
    # Найдем позиции белых и черных вершин
    whites = [i for i in range(2*N) if S[i] == 'W']
    blacks = [i for i in range(2*N) if S[i] == 'B']
    
    # dp[mask] = количество способов сопоставить черные вершины из mask
    # так, чтобы граф оставался сильно связным
    
    # Для сильной связности нужно, чтобы из любой вершины можно было
    # добраться в любую другую
    
    # Ключевое наблюдение: граф сильно связан тогда и только тогда,
    # когда для любого префикса [0, i] количество исходящих ребер
    # (включая добавленные) >= количество вершин в префиксе минус 1
    # И симметрично для суффиксов
    
    # Более точно: для сильной связности необходимо и достаточно,
    # чтобы для любого k от 1 до 2N-1:
    # - из вершин [0, k) должно быть хотя бы одно ребро в [k, 2N)
    # - из вершин [k, 2N) должно быть хотя бы одно ребро в [0, k)
    
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def dp(w_idx, b_mask):
        if w_idx == N:
            # Проверяем сильную связность
            # Строим список пар
            pairs = []
            b_list = [i for i in range(N) if (b_mask >> i) & 1]
            if len(b_list) != N:
                return 0
            
            matching = {}
            b_used = list(b_list)
            for i in range(N):
                matching[whites[i]] = blacks[b_used[i]]
            
            # Проверка сильной связности
            # Для каждого разреза проверяем наличие ребер в обе стороны
            for cut in range(1, 2*N):
                # Проверяем есть ли ребро из [0, cut) в [cut, 2N)
                has_forward = False
                has_backward = False
                
                for v in range(cut):
                    # Исходное ребро v -> v+1
                    if v + 1 >= cut:
                        has_forward = True
                    # Добавленное ребро
                    if v in matching and matching[v] >= cut:
                        has_forward = True
                    if v in matching.values():
                        for w, b in matching.items():
                            if b == v and w >= cut:
                                has_backward = True
                
                for v in range(cut, 2*N):
                    # Исходное ребро v -> v+1
                    if v + 1 < cut:
                        has_backward = True
                    # Добавленное ребро
                    if v in matching and matching[v] < cut:
                        has_backward = True
                    if v in matching.values():
                        for w, b in matching.items():
                            if b == v and w < cut:
                                has_forward = True
                
                if not has_forward or not has_backward:
                    return 0
            
            return 1
        
        result = 0
        for b_idx in range(N):
            if not ((b_mask >> b_idx) & 1):
                result = (result + dp(w_idx + 1, b_mask | (1 << b_idx))) % MOD
        
        return result
    
    print(dp(0, 0))

solve()