def grundy(a, b, x, y):
    if a == 0 and b == 0:
        return 0
    
    seen = set()
    
    # 金貨を1枚取り除き、銀貨をx枚入れる
    if a > 0:
        g = grundy(a - 1, b + x, y, x)
        seen.add(g)
    
    # 銀貨を1枚取り除く
    if b > 0:
        g = grundy(a, b - 1, y, x)
        seen.add(g)
    
    # mex
    mex = 0
    while mex in seen:
        mex += 1
    return mex

def compute_grundy_memo(a, b, x, y):
    memo = {}
    
    def helper(a, b, turn):
        if a == 0 and b == 0:
            return 0
        
        if (a, b, turn) in memo:
            return memo[(a, b, turn)]
        
        seen = set()
        
        if turn == 0:  # 高橋のターン
            if a > 0:
                g = helper(a - 1, b + x, 1)
                seen.add(g)
            if b > 0:
                g = helper(a, b - 1, 1)
                seen.add(g)
        else:  # 青木のターン
            if a > 0:
                g = helper(a - 1, b + y, 0)
                seen.add(g)
            if b > 0:
                g = helper(a, b - 1, 0)
                seen.add(g)
        
        mex = 0
        while mex in seen:
            mex += 1
        
        memo[(a, b, turn)] = mex
        return mex
    
    return helper(a, b, 0)

def solve():
    MOD = 998244353
    n, x, y = map(int, input().split())
    bags = []
    for _ in range(n):
        a, b = map(int, input().split())
        bags.append((a, b))
    
    # 各袋のGrundy数を計算
    grundy_values = []
    for a, b in bags:
        g = compute_grundy_memo(a, b, x, y)
        grundy_values.append(g)
    
    # 勝つ組み合わせを数える
    count = 0
    for mask in range(1 << n):
        takahashi_xor = 0
        aoki_xor = 0
        
        for i in range(n):
            if mask & (1 << i):
                takahashi_xor ^= grundy_values[i]
            else:
                aoki_xor ^= grundy_values[i]
        
        # 高橋が先手で勝つ = 高橋のXORが0でない
        if takahashi_xor != 0:
            count += 1
    
    print(count % MOD)

solve()