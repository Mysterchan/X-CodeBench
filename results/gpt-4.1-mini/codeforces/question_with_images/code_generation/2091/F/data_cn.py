import sys
import math
input = sys.stdin.readline
MOD = 998244353

# 由於 n*m 總和可達 4*10^6，且 n 最大 2000，m 最大 2000，
# 需要高效處理。每層最多兩個握點，且每層至少一個握點。
# 路徑定義：從底層到頂層，每層選擇1或2個握點，且握點間距離<=d。
# 計算所有有效路徑數量。

# 思路：
# 1. 對每層提取握點座標（行號固定，列號為握點所在區段）
# 2. 每層握點數量最多 m，m最大2000，握點數量不一定少，但每層最多選2個握點。
# 3. 路徑中每層選1或2個握點，且握點間距離<=d。
# 4. 從底層往上DP，dp[i][mask]表示第i層選擇握點組合mask的路徑數。
#    mask為該層握點的子集，且子集大小為1或2。
# 5. 轉移時，從第i層的mask到第i-1層的mask2，需判斷所有握點對距離<=d。
# 6. 最終答案為dp[1][mask]所有mask和。

# 優化：
# - 每層握點數量可能較多，選擇1或2個握點的組合數為 O(m^2)。
# - 轉移時，兩層的組合數乘積可能很大，需優化。
# - 利用握點間距離<=d的限制，對握點排序後用雙指針或二分剪枝。
# - 由於距離計算包含行差，行差為1（相鄰層），距離公式 sqrt(1 + (j1-j2)^2) <= d
#   => |j1-j2| <= sqrt(d^2 -1)
# - 只需考慮列差在一定範圍內的握點。

# 實作細節：
# - 對每層握點按列排序。
# - 預先計算每層所有1或2個握點的組合，存為states[i]。
# - 對每層握點，建立鄰接關係：哪些握點可從上一層握點到達。
# - 轉移時，對上一層的每個組合mask1，找下一層所有mask2，使得mask1和mask2的握點兩兩距離<=d。
# - 因為每層最多2個握點，組合數為 O(m^2)，但m最大2000，約400萬組合，需優化。
# - 利用距離限制，對握點列號做範圍限制，減少配對數。

# 由於時間限制，以下為可行方案：
# - 只考慮每層握點的1或2個握點組合。
# - 對每層握點，建立鄰接列表，記錄上一層握點可到達的下一層握點。
# - DP中，對上一層組合mask1，下一層組合mask2，判斷是否所有握點對距離<=d。
# - 利用握點排序和距離限制，快速判斷。

# 由於握點數量可能較多，且每層最多2個握點，組合數為 O(m^2)，
# 但總和4*10^6，且t最多1000，需快速實現。

# 以下為實作代碼：

def main():
    t = int(input())
    for _ in range(t):
        n,m,d = map(int,input().split())
        grid = [input().strip() for __ in range(n)]
        # 握點座標，行從1到n，頂層為1，底層為n
        points = []
        for i in range(n):
            row_points = []
            for j in range(m):
                if grid[i][j] == 'X':
                    row_points.append(j)
            points.append(row_points)
        # 若底層無握點，答案為0
        if not points[-1]:
            print(0)
            continue

        # 預處理每層握點的組合（1或2個握點）
        # states[i] = list of tuples (mask, [indices])
        # mask用bit表示該層握點選擇，indices為握點列號
        states = []
        for row_points in points:
            s = []
            l = len(row_points)
            for i1 in range(l):
                s.append((1<<i1, [row_points[i1]]))
            for i1 in range(l):
                for i2 in range(i1+1,l):
                    s.append(((1<<i1)|(1<<i2), [row_points[i1], row_points[i2]]))
            states.append(s)

        # dp[i][k]: 第i層選擇states[i][k]組合的路徑數
        # i從n-1(底層)到0(頂層)
        # 初始化底層dp
        dp = [dict() for __ in range(n)]
        for idx, (mask, cols) in enumerate(states[-1]):
            dp[-1][idx] = 1

        # 預計算距離限制
        # 兩層相鄰，行差為1
        # 距離 sqrt(1 + (c1 - c2)^2) <= d
        # => (c1 - c2)^2 <= d^2 -1
        max_col_diff = int(math.isqrt(max(0,d*d -1)))

        # 建立上一層組合到下一層組合的可達性
        # 由於每層組合數約O(m^2)，m最大2000，約400萬，直接全配對不可行
        # 利用握點列排序和距離限制剪枝
        # 對每層握點排序已經是升序，states[i]中cols已升序

        # 為加速，對每層握點建立列索引映射
        # 轉移時，對上一層組合的握點列，找下一層組合的握點列是否都在距離限制內

        # 儲存每層握點列的索引，方便二分查找
        from bisect import bisect_left, bisect_right

        # 對每層握點列排序（已排序）
        # states[i][k][1]已是升序列

        # 轉移
        for i in range(n-1,0,-1):
            dp_cur = dp[i]
            dp_prev = {}
            s_cur = states[i]
            s_prev = states[i-1]
            # 對下一層握點列建立索引
            next_points = points[i]
            prev_points = points[i-1]

            # 建立下一層握點列的索引映射
            # 方便快速查找距離限制內的握點
            # 但因為組合是1或2個握點，需判斷所有握點對距離<=d

            # 對上一層每個組合k1，嘗試所有下一層組合k2，判斷是否可連接
            # 優化：對上一層組合k1的握點列，找下一層組合k2的握點列是否都在距離限制內
            # 由於握點列已排序，利用二分查找快速判斷

            # 建立下一層組合的握點列集合，方便快速判斷
            # 但因為握點數最多2個，直接判斷即可

            # 對下一層組合k2，建立握點列集合
            # 對上一層組合k1，判斷所有握點對距離<=d

            # 為加速，對下一層組合k2的握點列建立min,max列號
            next_minmax = []
            for mask, cols in s_cur:
                next_minmax.append( (min(cols), max(cols)) )

            # 對上一層組合k1遍歷
            for k1, ways in dp_cur.items():
                mask1, cols1 = s_cur[k1]
                # cols1是下一層握點列，實際上dp_cur是下一層的dp
                # 轉移方向是從下一層到上一層
                # 但我們要從上一層到下一層，故反向遍歷
                # 這裡i從n-1往0走，dp[i]是第i層，dp[i-1]是上一層
                # 目前dp_cur是第i層，dp_prev是第i-1層
                # 轉移是 dp[i-1][k2] += dp[i][k1] if k2->k1可達
                # 所以要判斷上一層組合k2是否能到達下一層組合k1

                # 因此，對上一層組合k2遍歷，判斷k2->k1是否可達
                # 先跳過，改為對上一層組合k2遍歷

            # 重新調整轉移方向：
            # dp[i][k]: 第i層選擇組合k的路徑數
            # dp[i-1][k2] += sum dp[i][k1] if k2->k1可達
            # 所以對上一層組合k2遍歷，找所有下一層組合k1可達，累加dp[i][k1]

            # 建立下一層組合k1的索引，方便查找
            # 由於dp[i]中k1的數量可能很大，建立倒排表

            # 對下一層組合k1，建立握點列集合
            # 對上一層組合k2，判斷是否所有握點對距離<=d

            # 為加速，對下一層組合k1建立握點列集合，並按列排序
            # 對上一層組合k2，利用握點列範圍快速篩選下一層組合k1

            # 先建立下一層組合k1的握點列集合
            # 由於握點數最多2個，直接存cols tuple

            # 建立下一層組合k1的索引，方便快速查找
            # 但因為握點列是整數，且m最大2000，建立二維索引不實際
            # 改用遍歷

            # 對上一層組合k2遍歷
            dp_prev = {}
            s_prev = states[i-1]
            for k2, (mask2, cols2) in enumerate(s_prev):
                total = 0
                # 對下一層組合k1遍歷
                for k1, ways in dp_cur.items():
                    mask1, cols1 = s_cur[k1]
                    # 判斷cols2和cols1所有握點對距離<=d
                    # 行差為1
                    # 距離 sqrt(1 + (c1 - c2)^2) <= d
                    # => |c1 - c2| <= max_col_diff
                    ok = True
                    for c2 in cols2:
                        for c1 in cols1:
                            if abs(c1 - c2) > max_col_diff:
                                ok = False
                                break
                        if not ok:
                            break
                    if ok:
                        total += ways
                if total:
                    dp_prev[k2] = total % MOD
            dp[i-1] = dp_prev

        # 答案為頂層dp[0]所有組合路徑數和
        ans = 0
        for v in dp[0].values():
            ans = (ans + v) % MOD
        print(ans)

if __name__ == "__main__":
    main()