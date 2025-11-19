def solve():
    MOD = 998244353
    N = int(input())
    
    # 各数値の桁数を計算
    digits = []
    for i in range(1, N + 1):
        digits.append(len(str(i)))
    
    # 累積桁数を計算（i番目より後ろの数値の桁数の合計）
    cumsum_digits = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        cumsum_digits[i] = cumsum_digits[i + 1] + digits[i]
    
    # 10のべき乗を事前計算
    pow10 = [1] * (cumsum_digits[0] + 1)
    for i in range(1, len(pow10)):
        pow10[i] = pow10[i - 1] * 10 % MOD
    
    # 各位置に各数値が来る回数
    count_per_position = 1
    for i in range(N - 1):
        count_per_position = count_per_position * (i + 1) % MOD
    
    ans = 0
    
    # 各位置について計算
    for pos in range(N):
        # この位置より後ろの桁数の合計
        right_digits = cumsum_digits[pos + 1]
        
        # 各数値がこの位置に来た時の寄与を計算
        for num in range(1, N + 1):
            # numがpos位置に来た時、その値は10^right_digits倍される
            contribution = num * pow10[right_digits] % MOD
            contribution = contribution * count_per_position % MOD
            ans = (ans + contribution) % MOD
    
    print(ans)

solve()