import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()

    k_max = min(n // 2, m)
    if k_max == 0:
        print(0)
        continue

    # 預計算三角形面積的計算公式：
    # 三角形頂點為 (a[i],0), (a[j],0), (b[k],2)
    # 面積 = |(a[j]-a[i])*2/2| = |a[j]-a[i]|
    # 因為 y=0 和 y=2，三角形面積 = base * height / 2 = |a[j]-a[i]| * 2 / 2 = |a[j]-a[i]|
    # 所以面積等於兩個底點 x 坐標差的絕對值。

    # 為了最大化面積，對於每個 b[k]，我們想選擇兩個 a 點，使 |a[j]-a[i]| 最大。
    # 因為三角形面積只與底邊長度有關，與 b[k] 的 x 坐標無關。
    # 所以最大面積三角形是選擇 a 的最左和最右兩點，搭配任一 b 點。
    # 但因為要執行 k 次操作，每次操作要用 2 個 a 點和 1 個 b 點。
    # 所以我們要從 a 中選出 2*k 個點，從 b 中選出 k 個點。
    # 為了最大化總面積，我們應該選擇 a 中差距最大的 k 對點，b 中最大的 k 個點（因為 b 的 x 不影響面積，選擇任意 k 個即可）。
    # 但因為面積只與 a 的點差有關，b 點只影響可用數量。

    # 解法：
    # 1. 從 a 中選出 2*k 個點，配對成 k 對，使得每對的差值最大化。
    #    這裡最佳策略是從 a 的兩端配對：
    #    - 第 1 對：a[0], a[-1]
    #    - 第 2 對：a[1], a[-2]
    #    - ...
    # 2. 對每對計算差值，乘以 2（因為高度是 2），即面積 = 差值 * 2 / 2 = 差值
    # 3. 對 b 點排序，取最大的 k 個（但因為 b 的 x 不影響面積，任意 k 個即可）
    # 4. 將 k 對差值排序後累加，得到 f(1), f(2), ..., f(k_max)

    # 實作：
    res = []
    for i in range(k_max):
        diff = b[m - 1 - i] - a[i]  # 取 b 最大的和 a 最小的配對
        # 但面積只與 a 的差值有關，b 的 x 不影響面積，這裡錯了。
        # 正確是 a[i] 和 a[n-1 - i] 配對，b 任意取一個點即可。
        # 重新計算：
    res = []
    for i in range(k_max):
        diff = a[n - 1 - i] - a[i]
        res.append(diff * 2)  # 高度是 2，面積 = base * height / 2 = diff * 2 / 2 = diff
        # 但題目中 y=0 和 y=2，三角形面積 = |a[j]-a[i]| * 2 / 2 = |a[j]-a[i]|
        # 所以面積 = diff
        # 這裡乘 2 是錯的，應該是 diff
    # 修正：
    res = []
    for i in range(k_max):
        diff = a[n - 1 - i] - a[i]
        res.append(diff)

    res.sort(reverse=True)
    for i in range(1, k_max):
        res[i] += res[i - 1]

    print(k_max)
    print(*res)