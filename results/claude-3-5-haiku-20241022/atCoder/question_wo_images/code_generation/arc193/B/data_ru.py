def solve():
    MOD = 998244353
    
    N = int(input())
    s = input().strip()
    
    # Подсчитываем количество единиц в строке
    ones = s.count('1')
    
    # Граф имеет N рёбер в цикле и ones дополнительных рёбер к вершине N
    # Всего рёбер: N + ones
    
    # Каждое ребро может быть направлено двумя способами
    # Всего 2^(N + ones) способов направить все рёбра
    
    # Нам нужно подсчитать количество различных векторов входящих степеней
    
    # Используем динамическое программирование
    # Состояние: после обработки первых i вершин цикла (0..i-1),
    # отслеживаем входящие степени вершин и ребро между i-1 и i
    
    # Оптимизация: используем словарь для хранения состояний
    # Ключ: кортеж (d_N, направление_первого_ребра, d_0, ..., d_{i-1})
    
    # Более эффективный подход: заметим, что сумма входящих степеней = количество рёбер
    # d_0 + d_1 + ... + d_N = N + ones
    
    # Используем DP по циклу
    from collections import defaultdict
    
    # dp[состояние] = количество способов
    # состояние включает: (d_N, first_edge_dir, degrees_tuple)
    
    dp = defaultdict(int)
    
    # Начальное состояние: обрабатываем ребро {0, 1}
    # Можем направить 0->1 или 1->0
    # Также если s[0] == '1', есть ребро {0, N}
    
    if s[0] == '1':
        # Ребро {0, N} может быть 0->N или N->0
        # Ребро {0, 1} может быть 0->1 или 1->0
        for edge_01 in [0, 1]:  # 0: 0->1, 1: 1->0
            for edge_0N in [0, 1]:  # 0: 0->N, 1: N->0
                d0 = (1 if edge_01 == 1 else 0) + (1 if edge_0N == 1 else 0)
                d1 = 1 if edge_01 == 0 else 0
                dN = 1 if edge_0N == 0 else 0
                dp[(edge_01, d0, d1, dN)] += 1
    else:
        for edge_01 in [0, 1]:
            d0 = 1 if edge_01 == 1 else 0
            d1 = 1 if edge_01 == 0 else 0
            dN = 0
            dp[(edge_01, d0, d1, dN)] += 1
    
    # Обрабатываем вершины 1, 2, ..., N-1
    for i in range(1, N):
        new_dp = defaultdict(int)
        
        for state, count in dp.items():
            first_edge, *degrees = state
            d0, *rest_degrees = degrees[:-1]
            dN = degrees[-1]
            
            # Ребро {i, (i+1) mod N} = {i, i+1} для i < N-1
            # Ребро {N-1, 0} для i = N-1
            
            if i < N - 1:
                # Ребро {i, i+1}
                for edge_dir in [0, 1]:  # 0: i->i+1, 1: i+1->i
                    new_degrees = list(degrees)
                    if edge_dir == 1:
                        new_degrees[i] += 1
                    else:
                        new_degrees[i+1] = 1
                    
                    if s[i] == '1':
                        # Ребро {i, N}
                        for edge_iN in [0, 1]:
                            final_degrees = new_degrees[:]
                            if edge_iN == 1:
                                final_degrees[i] += 1
                            else:
                                final_degrees[-1] += 1
                            new_dp[(first_edge, *final_degrees)] += count
                    else:
                        new_dp[(first_edge, *new_degrees)] += count
            else:
                # i = N-1, ребро {N-1, 0}
                for edge_dir in [0, 1]:
                    new_degrees = list(degrees)
                    if edge_dir == 1:
                        new_degrees[N-1] += 1
                    else:
                        new_degrees[0] += 1
                    
                    if s[N-1] == '1':
                        for edge_iN in [0, 1]:
                            final_degrees = new_degrees[:]
                            if edge_iN == 1:
                                final_degrees[N-1] += 1
                            else:
                                final_degrees[-1] += 1
                            
                            # Проверяем совместимость с первым ребром
                            if first_edge == 0:
                                if final_degrees[0] > 0 and final_degrees[1] > 0:
                                    new_dp[tuple(final_degrees)] += count
                            else:
                                if final_degrees[0] > 0 and final_degrees[1] > 0:
                                    new_dp[tuple(final_degrees)] += count
                    else:
                        if first_edge == 0:
                            if edge_dir == 0 and new_degrees[0] > 0:
                                new_dp[tuple(new_degrees)] += count
                        else:
                            if edge_dir == 1 and new_degrees[1] > 0:
                                new_dp[tuple(new_degrees)] += count
        
        dp = new_dp
        for key in dp:
            dp[key] %= MOD
    
    result = len(dp) % MOD
    print(result)

solve()