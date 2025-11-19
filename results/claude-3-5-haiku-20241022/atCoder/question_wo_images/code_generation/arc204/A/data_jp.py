def solve():
    MOD = 998244353
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # dp[step][i][j][c] = 操作step回目、次に挿入するインデックスがi、キューの先頭インデックスがj、現在のCの値がcのときの場合の数
    # ただし、メモリ削減のため、cは実際に取りうる値のみを管理
    
    # キューの状態は、次に挿入するインデックスiと、キューの先頭インデックスjで表現できる
    # キュー内の要素は [j, j+1, ..., i-1]
    
    # dp[i][j][c] = 次に挿入するのがi番目、キューの先頭がj番目、現在のCがcのときの場合の数
    from collections import defaultdict
    
    dp = defaultdict(int)
    dp[(1, 1, 0)] = 1  # 初期状態: i=1, j=1 (キューは空), C=0
    
    for step in range(2 * N):
        new_dp = defaultdict(int)
        
        for (i, j, c), cnt in dp.items():
            if cnt == 0:
                continue
            
            # 行動1: iをキューに追加
            if i <= N:
                new_c = max(0, c - A[i - 1])
                new_i = i + 1
                new_j = j if j <= i else i  # キューが空だった場合、jをiに更新
                if j > i:  # キューが空
                    new_j = i
                new_dp[(new_i, new_j, new_c)] = (new_dp[(new_i, new_j, new_c)] + cnt) % MOD
            
            # 行動2: キューの先頭を削除
            if j < i:  # キューが空でない
                new_c = c + B[j - 1]
                new_j = j + 1
                new_dp[(i, new_j, new_c)] = (new_dp[(i, new_j, new_c)] + cnt) % MOD
        
        dp = new_dp
    
    # 最終状態: i=N+1, j=N+1 (すべて処理済み)
    ans = 0
    for (i, j, c), cnt in dp.items():
        if i == N + 1 and j == N + 1 and L <= c <= R:
            ans = (ans + cnt) % MOD
    
    print(ans)

solve()