def solve():
    MOD = 998244353
    N, M = map(int, input().split())
    S = input().strip()
    
    # dp[i][j][k] = число способов создать строку длины i, где:
    # j = индекс в S (сколько символов S мы сопоставили)
    # k = длина LCS
    # Но нам нужно отслеживать состояние LCS более точно
    
    # Лучший подход: dp по позиции в генерируемой строке и состоянию LCS
    # Состояние LCS можно представить как вектор длины N+1, показывающий
    # максимальную длину LCS используя первые j символов S
    
    # dp[i][state] где state - это tuple представляющий для каждого префикса S
    # какова максимальная длина LCS
    
    # Оптимизация: состояние = tuple длин LCS для каждого префикса S
    # state[j] = макс длина LCS между текущей строкой и S[0:j+1]
    
    from collections import defaultdict
    
    # dp[pos][state] = количество строк
    # state = tuple из N элементов, state[j] = LCS с S[0..j]
    dp = defaultdict(int)
    dp[tuple([0] * N)] = 1
    
    for pos in range(M):
        new_dp = defaultdict(int)
        for state, count in dp.items():
            # Пробуем добавить каждый символ
            for c in range(26):
                ch = chr(ord('a') + c)
                new_state = list(state)
                
                # Обновляем LCS для каждого префикса S
                for j in range(N):
                    if S[j] == ch:
                        # Можем расширить LCS
                        if j == 0:
                            new_state[j] = max(new_state[j], 1)
                        else:
                            new_state[j] = max(new_state[j], new_state[j-1] + 1)
                    else:
                        # Не можем расширить используя этот символ
                        if j > 0:
                            new_state[j] = max(new_state[j], new_state[j-1])
                
                new_dp[tuple(new_state)] = (new_dp[tuple(new_state)] + count) % MOD
        
        dp = new_dp
    
    # Собираем ответы
    ans = [0] * (N + 1)
    for state, count in dp.items():
        lcs_len = state[N-1]  # LCS со всем S
        ans[lcs_len] = (ans[lcs_len] + count) % MOD
    
    print(' '.join(map(str, ans)))

solve()