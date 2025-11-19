import sys
input = sys.stdin.readline

N, M = map(int, input().split())
intervals = []
for _ in range(M):
    A, B = map(int, input().split())
    intervals.append((A, B))
intervals.sort()

# 將偶數點映射到 [1..N] 範圍 (因為偶數點是2,4,...,2N)
# 方便處理區間
# 例如點2 -> 1, 點4 -> 2, ..., 點2N -> N
def even_to_idx(x):
    return x // 2

# 對 M 條線段，記錄區間 [l,r]，l < r
# 且區間不重疊，且不共點
# 對這些區間，我們建立一個 prefix sum 陣列，方便查詢區間內有多少線段

# intervals 已排序，且不重疊
# 建立 prefix sum，prefix[i] = 前 i 條線段的右端點
# 方便用二分找出區間內的線段數量

# 由於區間不重疊且不共點，且排序後 intervals[i][0] > intervals[i-1][1]
# 我們可以用二分找出在某範圍內的線段數量

# 先建立兩個陣列，分別存左端點和右端點
L = [even_to_idx(a) for a, b in intervals]
R = [even_to_idx(b) for a, b in intervals]

import bisect

Q = int(input())
for _q in range(Q):
    C, D = map(int, input().split())
    # C,D 是奇數點，且 C < D
    # 查詢與連接 C,D 線段相交的線段數量
    # 連接 C,D 線段的點是奇數點，且 C < D
    # 連接 C,D 線段的區間是 (C,D) 之間的點（順時針）
    # 由於點是環狀，且點編號是 1..2N
    # 但題目中 C < D，且都是奇數，且點是順時針編號
    # 連接 C,D 線段的區間是 (C,D) 之間的點（不包含 C,D）
    # 我們要找與此線段相交的線段數量
    # 線段 i 連接偶數點 A_i,B_i，且區間不重疊
    # 線段 i 與查詢線段相交的條件是：
    # 線段 i 的區間 [L_i,R_i] 與查詢線段的區間 (C,D) 有交集
    # 但因為線段 i 連接偶數點，查詢線段連接奇數點，且線段 i 不共點
    # 交集條件是線段 i 的區間與 (C,D) 交疊

    # 將 C,D 映射到奇數點的索引 (奇數點的索引是 (x+1)//2)
    # 但我們只需要比較點的大小即可，因為點是 1..2N
    # 連接 C,D 線段的區間是 (C,D)
    # 線段 i 的區間是 [L[i]*2, R[i]*2] (偶數點)
    # 但為了方便，我們用偶數點的索引來比較
    # 將 C,D 映射到偶數點索引空間的奇數點位置
    # 奇數點 k 對應的偶數點索引是 (k-1)//2 + 0.5 (介於兩個偶數點之間)
    # 例如奇數點1介於偶數點0和1之間 (0.5)
    # 奇數點3介於偶數點1和2之間 (1.5)
    # 所以查詢區間 (C,D) 對應偶數點索引空間的 ( (C-1)/2+0.5, (D-1)/2+0.5 )

    left = (C - 1) / 2 + 0.5
    right = (D - 1) / 2 + 0.5

    # 線段 i 的區間是 [L[i], R[i]] (整數區間)
    # 線段 i 與查詢線段相交當且僅當：
    # 線段 i 的區間與 (left, right) 有交集
    # 即：
    # L[i] < right 且 R[i] > left

    # 找出所有 L[i] < right 的線段數量
    pos1 = bisect.bisect_left(L, right)
    # 找出所有 R[i] <= left 的線段數量
    pos2 = bisect.bisect_right(R, left)

    print(pos1 - pos2)