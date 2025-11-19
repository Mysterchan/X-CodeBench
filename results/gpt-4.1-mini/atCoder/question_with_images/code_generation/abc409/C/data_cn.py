import sys
input = sys.stdin.readline

N, L = map(int, input().split())
d = list(map(int, input().split()))

# 計算每個點相對於點1的絕對位置（順時針方向）
pos = [0]*(N+1)
for i in range(2, N+1):
    pos[i] = (pos[i-1] + d[i-2]) % L

# 建立位置到點的映射（因為位置可能重複）
pos_map = {}
for i in range(1, N+1):
    p = pos[i]
    if p not in pos_map:
        pos_map[p] = []
    pos_map[p].append(i)

# 等邊三角形條件：
# 三點 a,b,c 在圓上，且 a<b<c
# 位置分別為 pos[a], pos[b], pos[c]
# 三角形等邊 => 三點間距皆為 L/3
# 因此，三點位置必須是等差數列，公差為 L/3 或 2L/3 (因為圓周長為L)
# 具體來說，若 pos[b] - pos[a] ≡ L/3 (mod L)，且 pos[c] - pos[b] ≡ L/3 (mod L)
# 則三點形成等邊三角形。

# 先判斷 L 是否能被3整除，否則不可能有等邊三角形
if L % 3 != 0:
    print(0)
    sys.exit()

step = L // 3
ans = 0

# 對每個點 i，嘗試找位置 (pos[i] + step) % L 和 (pos[i] + 2*step) % L 的點
# 並計算符合條件的三元組數量
for i in range(1, N+1):
    p1 = pos[i]
    p2 = (p1 + step) % L
    p3 = (p1 + 2*step) % L
    if p2 in pos_map and p3 in pos_map:
        # pos_map[p2], pos_map[p3] 是點的列表
        # 需要找出所有 (a,b,c) 使得 a=i < b < c 且 pos[b]=p2, pos[c]=p3
        # 因為點編號是1..N，且 a<b<c
        # pos_map[p2], pos_map[p3] 中的點可能無序，先排序
        b_list = pos_map[p2]
        c_list = pos_map[p3]

        # 對 b_list 和 c_list 排序
        # 由於 pos_map 是在建立時依序加入，可能已經是排序的，但為保險起見排序
        # 但為了效率，只排序一次
        # 這裡可先排序一次，避免重複排序
        # 先判斷是否已排序，若未排序則排序
        # 但為簡潔，直接排序
        b_list = sorted(b_list)
        c_list = sorted(c_list)

        # 對 b_list 中的每個 b，找 c_list 中大於 b 的點數量
        # 並且 b > i (因為 a < b)
        # 使用二分搜尋
        import bisect

        # 找 b_list 中 b > i 的起始位置
        b_start = bisect.bisect_right(b_list, i)
        for b in b_list[b_start:]:
            # 找 c_list 中 c > b 的數量
            c_start = bisect.bisect_right(c_list, b)
            ans += len(c_list) - c_start

print(ans)