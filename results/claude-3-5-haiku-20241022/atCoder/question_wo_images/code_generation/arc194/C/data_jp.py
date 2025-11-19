N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# 反転が必要な位置を特定
need_flip = [i for i in range(N) if A[i] != B[i]]

if not need_flip:
    print(0)
else:
    # DP: dp[i] = 最初のi個の反転必要な位置を処理した後の最小コスト
    # 状態: 現在のAの状態を追跡
    
    # 現在の状態を管理
    current = A[:]
    
    # 全ての2^m通りの反転順序を試すのは現実的でないため、
    # 貪欲 + DPアプローチを使用
    
    # より効率的なアプローチ: ビットマスクDP
    m = len(need_flip)
    
    if m <= 20:
        # 小さい場合は全探索
        min_cost = float('inf')
        
        from itertools import permutations
        
        # 各順列を試す
        for perm in permutations(need_flip):
            current = A[:]
            total_cost = 0
            
            for idx in perm:
                current[idx] = 1 - current[idx]
                cost = sum(current[i] * C[i] for i in range(N))
                total_cost += cost
            
            min_cost = min(min_cost, total_cost)
        
        print(min_cost)
    else:
        # 大きい場合は貪欲法
        # コストの低い順に反転
        current = A[:]
        total_cost = 0
        
        # (コスト削減量, インデックス)のリストを作成
        flip_order = []
        for idx in need_flip:
            # このインデックスを反転することによる将来的な影響を考慮
            flip_order.append((C[idx], idx))
        
        flip_order.sort()
        
        for _, idx in flip_order:
            current[idx] = 1 - current[idx]
            cost = sum(current[i] * C[i] for i in range(N))
            total_cost += cost
        
        print(total_cost)