def max_vitamin(N, X, food_data):
    from collections import defaultdict

    # ビタミンごとの食べ物情報を格納する
    vitamins = defaultdict(list)

    for v, a, c in food_data:
        vitamins[v].append((a, c))

    # 各ビタミンごとにカロリー制限を考慮しつつ最大摂取量を求める
    dp = [[0] * (X + 1) for _ in range(4)]  # dp[v][x] = ビタミンvのカロリーxでの最大摂取量

    for v in range(1, 4):
        for a, c in vitamins[v]:
            for x in range(X, c - 1, -1):
                dp[v][x] = max(dp[v][x], dp[v][x - c] + a)

    answer = 0

    # ビタミン1, 2, 3 の最小値を取る
    for x in range(X + 1):
        min_vitamin = min(dp[1][x], dp[2][x], dp[3][x])
        answer = max(answer, min_vitamin)

    return answer

# 入力データの受け取り
import sys
input = sys.stdin.read
data = input().splitlines()
N, X = map(int, data[0].split())
food_data = [tuple(map(int, line.split())) for line in data[1:N + 1]]

# 出力
print(max_vitamin(N, X, food_data))