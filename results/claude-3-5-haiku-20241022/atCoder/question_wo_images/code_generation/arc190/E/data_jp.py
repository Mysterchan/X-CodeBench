def solve_query(B):
    n = len(B)
    if n == 0:
        return 0
    
    # dp[i] = i番目までの要素を使って得られる最大操作回数
    # 各位置で、どれだけの値を残すかを管理する必要がある
    
    # 動的計画法: dp[i][r] = i番目まで見て、i番目に残っている値がrのときの最大操作回数
    # ただし、状態数が多すぎるので工夫が必要
    
    # 別のアプローチ: 貪欲法
    # 各位置について、できるだけ多くペアを作る
    
    # より良いアプローチ: DP with state compression
    # dp[i] = (max_ops, prev_val, prev_prev_val)
    # i番目まで処理したときの(最大操作回数、i-1番目の残り、i-2番目の残り)
    
    # 実装: dp[i][(val_{i-1}, val_{i-2})] = 最大操作回数
    from collections import defaultdict
    
    if n == 1:
        return 0
    
    # dp[i] = dictionary mapping (prev_val, prev_prev_val) to max operations
    dp = [defaultdict(lambda: -1) for _ in range(n + 1)]
    dp[0][(0, 0)] = 0
    
    for i in range(n):
        for (prev, prev_prev), ops in dp[i].items():
            if ops == -1:
                continue
            
            curr_val = B[i]
            
            # Try all possible values to keep at position i
            for keep in range(curr_val + 1):
                used = curr_val - keep
                
                # Calculate pairs we can make
                new_ops = ops
                remaining_prev = prev
                
                # Pair with position i-1
                if i > 0 and remaining_prev > 0 and used > 0:
                    pairs_with_prev = min(remaining_prev, used)
                    new_ops += pairs_with_prev
                    remaining_prev -= pairs_with_prev
                    used -= pairs_with_prev
                
                # Pair with position i-2
                remaining_prev_prev = prev_prev
                if i > 1 and remaining_prev_prev > 0 and used > 0:
                    pairs_with_prev_prev = min(remaining_prev_prev, used)
                    new_ops += pairs_with_prev_prev
                    remaining_prev_prev -= pairs_with_prev_prev
                    used -= pairs_with_prev_prev
                
                new_state = (keep, remaining_prev)
                dp[i + 1][new_state] = max(dp[i + 1][new_state], new_ops)
    
    return max(dp[n].values())

# Read input
N, Q = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(Q):
    L, R = map(int, input().split())
    B = A[L-1:R]
    print(solve_query(B))