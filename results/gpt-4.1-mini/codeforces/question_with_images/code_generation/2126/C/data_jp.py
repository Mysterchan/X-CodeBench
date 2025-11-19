import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    k -= 1  # 0-indexed

    max_h = max(h)
    max_indices = [i for i, height in enumerate(h) if height == max_h]

    # dp[i]: 最大の余裕時間（= h[i] - 時刻）で塔iに到達可能かの判定に使う
    # 初期状態は-1（到達不可）
    dp = [-1] * n
    dp[k] = h[k] - 1  # 時刻0に塔kにいるので余裕は h[k] - 1

    # 左から右へ
    for i in range(k + 1, n):
        # テレポート時間は |h[i] - h[i-1]|、移動中は元の塔にいるので
        # 到達時刻 = (h[i-1] - dp[i-1]) + |h[i] - h[i-1]|
        # 余裕 = h[i] - 到達時刻
        cost = abs(h[i] - h[i - 1])
        arrive_time = (h[i - 1] - dp[i - 1]) + cost
        remain = h[i] - arrive_time
        if dp[i - 1] >= cost and remain > 0:
            dp[i] = max(dp[i], remain)

    # 右から左へ
    for i in range(k - 1, -1, -1):
        cost = abs(h[i] - h[i + 1])
        arrive_time = (h[i + 1] - dp[i + 1]) + cost
        remain = h[i] - arrive_time
        if dp[i + 1] >= cost and remain > 0:
            dp[i] = max(dp[i], remain)

    # 最大高さの塔に到達可能か判定
    ans = any(dp[i] >= 0 for i in max_indices)
    print("YES" if ans else "NO")