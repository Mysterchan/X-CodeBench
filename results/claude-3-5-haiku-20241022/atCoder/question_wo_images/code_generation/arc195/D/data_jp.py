def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # dp[i] = i番目以降の要素を削除するのに必要な最小操作回数
    dp = [float('inf')] * (n + 1)
    dp[n] = 0
    
    for i in range(n - 1, -1, -1):
        # 選択肢1: a[i]を1つだけ削除 (先頭に持ってきて削除)
        # i番目を先頭に移動させるにはi回のswapが必要
        # その後1回の削除操作
        dp[i] = min(dp[i], i + 1 + dp[i + 1])
        
        # 選択肢2: a[i]と同じ値が連続する部分をまとめて削除
        j = i
        while j < n and a[j] == a[i]:
            j += 1
        # a[i:j]を全て先頭に集めて削除
        # i回のswapでa[i]を先頭に、その後a[i+1]をa[i]の隣に...
        # 合計i回のswapで全てを先頭に集められる
        # その後1回の削除で全て削除
        dp[i] = min(dp[i], i + 1 + dp[j])
        
        # 選択肢3: 間に他の要素がある同じ値を集める
        # a[i]と同じ値の要素を全て先頭に集める
        count = 0
        swaps = 0
        pos = i
        for k in range(i, n):
            if a[k] == a[i]:
                count += 1
                # a[k]をposの位置に移動
                swaps += k - pos
                pos += 1
        # swaps回のswapとcount個の要素を削除する1回の操作
        dp[i] = min(dp[i], swaps + 1 + dp[pos])
    
    return dp[0]

t = int(input())
for _ in range(t):
    print(solve())