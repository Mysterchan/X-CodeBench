import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        l1, r1, l2, r2 = map(int, input().split())
        width = r1 - l1
        height = r2 - l2

        # 找出覆蓋區域的最小四叉樹節點數量
        # 四叉樹節點區域大小為 2^k x 2^k，k >= 0
        # 我們要用最少節點數量覆蓋 [l1,r1] x [l2,r2]
        # 節點區域邊界為 [a*2^k,(a+1)*2^k] x [b*2^k,(b+1)*2^k]
        # 節點大小為 2^k
        # 對於給定區域，最小節點數量 = (覆蓋寬度的節點數) * (覆蓋高度的節點數)
        # 覆蓋寬度的節點數 = ceil(width / 2^k)
        # 覆蓋高度的節點數 = ceil(height / 2^k)
        # k 是使得節點大小 >= max(width, height) 的最小 k
        # 但題目中節點大小必須是 2^k，且節點邊界必須是 a*2^k
        # 因此，我們先找出覆蓋區域的最小外接正方形邊長 = max(width, height)
        # 找出最小的 2^k >= max(width, height)
        # 然後計算覆蓋節點數 = (ceil(width / 2^k)) * (ceil(height / 2^k))
        # 但題目中區域邊界不一定對齊節點邊界，可能需要多個節點拼接
        # 事實上，答案就是：
        # 對 x 軸：節點大小為 2^k，覆蓋區間長度 width，節點數 = ceil(width / 2^k)
        # 對 y 軸同理
        # k = ceil(log2(max(width, height)))
        # 節點大小 = 2^k
        # 答案 = ceil(width / 2^k) * ceil(height / 2^k)

        # 但題目範例中，當區域大小是 1 或 2 時，答案是 1，符合上述邏輯
        # 例如第三個測試案例 [1,3] x [1,3]，width=2, height=2
        # 2^k >= 2 => k=1, 2^1=2
        # ceil(2/2)*ceil(2/2)=1*1=1 不符
        # 但答案是4，說明我們不能只用一個節點大小為2的節點覆蓋
        # 因為節點邊界必須是 a*2^k，區域邊界是[1,3]，不對齊2的倍數
        # 所以節點必須從0開始或2開始，無法用一個節點覆蓋[1,3]
        # 因此，我們必須考慮節點邊界對齊問題

        # 解法：
        # 對於每個 k 從 0 到 20 (因為 10^6 < 2^20)
        # 節點大小 = 2^k
        # 對 x 軸：
        # 節點覆蓋區間為 [a*2^k, (a+1)*2^k]
        # 我們要覆蓋 [l1, r1]
        # 節點數 = (節點覆蓋區間數) = (覆蓋區間的節點索引數)
        # 節點索引範圍：
        # a_min = l1 // 2^k
        # a_max = (r1-1) // 2^k
        # 節點數 = a_max - a_min + 1
        # 同理對 y 軸
        # 答案 = 節點數_x * 節點數_y
        # 我們要找所有 k 中的最小答案

        ans = 10**15
        for k in range(21):
            size = 1 << k
            x_nodes = ( (r1 - 1) // size ) - (l1 // size) + 1
            y_nodes = ( (r2 - 1) // size ) - (l2 // size) + 1
            if x_nodes > 0 and y_nodes > 0:
                ans = min(ans, x_nodes * y_nodes)
        print(ans)

solve()