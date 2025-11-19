import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    max_h = max(h)
    start_h = h[k-1]

    # 若起點即為最高塔，直接YES
    if start_h == max_h:
        print("YES")
        continue

    # 目標是任意一座最高塔
    # 傳送時間 = |h_i - h_j|
    # 水位每秒上升1，初始水位1，時間t時水位為t+1
    # 在塔i停留時間t，必須 t+1 <= h_i => t <= h_i -1
    # 傳送時在原塔停留，抵達時刻t+|h_i - h_j|，抵達時刻水位為 t+|h_i - h_j|+1
    # 抵達塔j時水位必須 <= h_j => t+|h_i - h_j|+1 <= h_j => t <= h_j - |h_i - h_j| -1

    # 由於可以任意傳送，且傳送時間只與高度差有關，
    # 我們嘗試判斷是否存在最高塔h_j，使得
    # |h_k - h_j| < h_j
    # 因為起點時間0，抵達時間為 |h_k - h_j|，抵達時水位為 |h_k - h_j| +1
    # 抵達塔j時水位 <= h_j => |h_k - h_j| +1 <= h_j => |h_k - h_j| < h_j

    # 若存在最高塔h_j滿足上述條件，則可直接傳送過去
    # 否則，無法到達最高塔

    # 因為最高塔高度相同，遍歷所有最高塔判斷即可
    can_reach = False
    for i, height in enumerate(h):
        if height == max_h:
            dist = abs(start_h - height)
            if dist < height:
                can_reach = True
                break

    print("YES" if can_reach else "NO")