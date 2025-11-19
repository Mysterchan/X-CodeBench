def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    N, X = map(int, data[0].split())
    
    food = []
    for i in range(1, N + 1):
        V, A, C = map(int, data[i].split())
        food.append((V, A, C))
    
    # dp[k][j]: 吃了前k种食物，消耗j卡路里的情况下的维他命数量
    dp = [[(0, 0, 0)] * (X + 1) for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        V, A, C = food[i - 1]
        for j in range(X + 1):
            # 不选择当前食物
            dp[i][j] = dp[i - 1][j]
            if j >= C:
                # 选择当前食物
                prev_vitamins = dp[i - 1][j - C]
                if V == 1:
                    new_vitamins = (prev_vitamins[0] + A, prev_vitamins[1], prev_vitamins[2])
                elif V == 2:
                    new_vitamins = (prev_vitamins[0], prev_vitamins[1] + A, prev_vitamins[2])
                else:  # V == 3
                    new_vitamins = (prev_vitamins[0], prev_vitamins[1], prev_vitamins[2] + A)
                
                dp[i][j] = max(dp[i][j], new_vitamins)
    
    # 取最大的最小值
    max_min_vitamin = 0
    for j in range(X + 1):
        vit1, vit2, vit3 = dp[N][j]
        max_min_vitamin = max(max_min_vitamin, min(vit1, vit2, vit3))
    
    print(max_min_vitamin)

if __name__ == "__main__":
    main()