import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# 思路分析：
# 題目要求找最小的 k 梯路，從根節點出發，覆蓋所有有怪物的節點。
# 這個問題等價於：在樹中，將所有有怪物的節點用最少條從根出發的路徑覆蓋。
# 由於路徑必須從根開始，且路徑是樹上的路徑，最小路徑數等於根節點的子樹中有怪物的子樹數量。
# 具體來說，對每個節點 u：
#   - 如果 u 本身有怪物，則 dp[u] = 1
#   - 否則 dp[u] = sum(dp[v]) for v 是 u 的子節點
# dp[1] 即為答案。
#
# 查詢要求對子樹中所有節點怪物狀態反轉，且查詢是累積的。
# 因此需要支援子樹區間反轉的資料結構。
#
# 解法：
# 1. 對樹做 DFS 序，將子樹區間映射為一段連續區間 [in[u], out[u]]。
# 2. 使用 Segment Tree 支援區間反轉（lazy propagation），節點存儲 dp 值（即該區間內怪物節點數）。
# 3. 初始 dp 值即為 a[u]（0或1）。
# 4. 查詢時對區間反轉，更新 Segment Tree。
# 5. 每次輸出 Segment Tree 根節點的 sum，即為答案。

def main():
    t = int(input())
    # 總 n, q 限制 250000，需注意效率與記憶體
    # 使用全域變數避免重複宣告
    MAXN = 250000
    # 以下變數會在每個測試案例重置
    # 為避免重複宣告，使用函式內宣告

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        g = [[] for __ in range(n)]
        for __ in range(n-1):
            u,v = map(int, input().split())
            u -= 1
            v -= 1
            g[u].append(v)
            g[v].append(u)

        # DFS序，計算in,out
        in_ = [0]*n
        out = [0]*n
        euler = []
        def dfs(u,p):
            in_[u] = len(euler)
            euler.append(u)
            for w in g[u]:
                if w == p:
                    continue
                dfs(w,u)
            out[u] = len(euler)-1
        dfs(0,-1)

        # 建立 segment tree
        # 節點存怪物數量 sum
        # lazy 標記區間反轉
        size = 1
        while size < n:
            size <<= 1
        seg = [0]*(2*size)
        lazy = [False]*(2*size)

        # 初始化葉節點
        for i in range(n):
            seg[size+i] = a[euler[i]]
        for i in range(size-1,0,-1):
            seg[i] = seg[i<<1] + seg[i<<1|1]

        def apply(i, length):
            seg[i] = length - seg[i]
            lazy[i] ^= True

        def push(i, length):
            if lazy[i]:
                apply(i<<1, length>>1)
                apply(i<<1|1, length>>1)
                lazy[i] = False

        def update(l,r,i,il,ir):
            if r < il or ir < l:
                return
            if l <= il and ir <= r:
                apply(i, ir - il + 1)
                return
            push(i, ir - il + 1)
            mid = (il+ir)>>1
            update(l,r,i<<1,il,mid)
            update(l,r,i<<1|1,mid+1,ir)
            seg[i] = seg[i<<1] + seg[i<<1|1]

        q = int(input())
        print(seg[1])
        for __ in range(q):
            v = int(input())-1
            update(in_[v], out[v], 1, 0, size-1)
            print(seg[1])

if __name__ == "__main__":
    main()