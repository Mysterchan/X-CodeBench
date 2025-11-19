def solve():
    MOD = 998244353
    N = int(input())
    S = input().strip()
    
    # 白と黒の頂点の位置を記録
    white = []
    black = []
    for i in range(2 * N):
        if S[i] == 'W':
            white.append(i + 1)
        else:
            black.append(i + 1)
    
    # dp[i][j] = i番目の白頂点まで、j個の黒頂点を使った時の方法数
    # ただし、各段階でグラフが強連結になる可能性を保つ
    
    # 強連結の条件: 任意の頂点から任意の頂点に到達可能
    # 元のグラフは 1 -> 2 -> ... -> 2N の一方向パス
    # 追加辺は白から黒へ
    
    # 強連結になるためには、最小の頂点から最大の頂点へのパスと
    # 最大の頂点から最小の頂点へのパスが必要
    
    # より具体的には、各プレフィックスで「戻る辺」が必要
    
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def dp(wi, bi, used_black):
        # wi: 次に処理する白頂点のインデックス
        # bi: 次に考慮する黒頂点のインデックス
        # used_black: 使用済み黒頂点のビットマスク
        
        if wi == N:
            # 全ての白頂点を処理した
            # 強連結性をチェック
            return 1 if is_strongly_connected(used_black) else 0
        
        if bi == N:
            return 0
        
        result = 0
        # 黒頂点を選択
        for j in range(N):
            if not (used_black & (1 << j)):
                new_mask = used_black | (1 << j)
                result = (result + dp(wi + 1, 0, new_mask)) % MOD
        
        return result
    
    def is_strongly_connected(mask):
        # マッチングを復元
        edges = set()
        # 元の辺
        for i in range(1, 2 * N):
            edges.add((i, i + 1))
        
        # 追加辺
        used = [False] * N
        for wi in range(N):
            for bi in range(N):
                if (mask >> (wi * N + bi)) & 1:
                    edges.add((white[wi], black[bi]))
                    used[bi] = True
                    break
        
        # BFSで到達可能性チェック
        # 簡易実装
        return True
    
    # より効率的なアプローチ
    # 動的計画法で全マッチングを列挙し、各マッチングについて強連結性をチェック
    
    def count_valid_matchings():
        # 全てのマッチングを生成
        from itertools import permutations
        
        count = 0
        for perm in permutations(range(N)):
            # white[i] -> black[perm[i]]
            if is_valid_matching(perm):
                count = (count + 1) % MOD
        
        return count
    
    def is_valid_matching(perm):
        # グラフを構築
        adj = [[] for _ in range(2 * N + 1)]
        for i in range(1, 2 * N):
            adj[i].append(i + 1)
        
        for i in range(N):
            adj[white[i]].append(black[perm[i]])
        
        # 強連結性チェック (Tarjanのアルゴリズムまたは2回のDFS)
        # 全頂点から到達可能かチェック
        def can_reach_all(start):
            visited = [False] * (2 * N + 1)
            stack = [start]
            visited[start] = True
            count = 1
            
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        count += 1
                        stack.append(v)
            
            return count == 2 * N
        
        # 頂点1から全頂点に到達可能かチェック
        if not can_reach_all(1):
            return False
        
        # 逆グラフを構築
        rev_adj = [[] for _ in range(2 * N + 1)]
        for i in range(1, 2 * N):
            rev_adj[i + 1].append(i)
        for i in range(N):
            rev_adj[black[perm[i]]].append(white[i])
        
        # 頂点1への到達可能性チェック
        visited = [False] * (2 * N + 1)
        stack = [1]
        visited[1] = True
        count = 1
        
        while stack:
            u = stack.pop()
            for v in rev_adj[u]:
                if not visited[v]:
                    visited[v] = True
                    count += 1
                    stack.append(v)
        
        return count == 2 * N
    
    print(count_valid_matchings())

solve()