import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
people = [tuple(map(int, input().split())) for _ in range(M)]
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# 解析問題：
# 城鎮線性排列，邊 j 連接 j 和 j+1，邊權 w_j 可設負數。
# 每人 i 從 S_i 出發，耐力初始0，經最短路徑到 T_i，要求：
# - 出發和到達耐力為0
# - 中間城鎮耐力 > 0
# - 沿路耐力變化為累加邊權
# 
# 因為路徑是線性，最短路即是沿著城鎮序號遞增或遞減的連續邊。
# 設 S_i < T_i，路徑為 S_i -> S_i+1 -> ... -> T_i
# 耐力變化為 w_{S_i} + w_{S_i+1} + ... + w_{T_i-1} = 0
# 中間點 k (S_i < k < T_i) 的耐力為 sum_{j=S_i}^{k-1} w_j > 0
# 
# 若 S_i > T_i，類似，路徑反向，耐力變化為負方向邊權和，條件同理。
#
# 令 d_j = w_j，定義前綴和 P_x = sum_{j=1}^{x-1} d_j，P_1=0
# 對路徑 S_i->T_i，耐力在 k 點為 P_k - P_{S_i}
# 要求：
# 1) P_{T_i} - P_{S_i} = 0
# 2) 對所有 k 在 (S_i, T_i) 範圍內，P_k - P_{S_i} > 0
#
# 若 S_i < T_i，則 P_{S_i} 是區間 (S_i, T_i) 的最小值，且 P_{T_i} = P_{S_i}
# 若 S_i > T_i，則 P_{S_i} 是區間 (T_i, S_i) 的最大值，且 P_{T_i} = P_{S_i}
#
# 總結：
# 對每個人 i，區間 [l_i, r_i] = [min(S_i,T_i), max(S_i,T_i)]
# 條件是 P_{l_i} = P_{r_i}，且在 (l_i, r_i) 內 P_x > P_{l_i} (若 S_i < T_i)
# 或 P_x < P_{l_i} (若 S_i > T_i)
#
# 這表示 P 在該區間端點相等，中間點嚴格大於（或小於）端點值。
#
# 問題轉為：
# 是否存在一個序列 P_1,...,P_N 滿足所有選定人的條件。
#
# 觀察：
# - P_1=0 固定
# - 每個條件限制 P 在某區間端點相等，且中間點嚴格大於或小於端點值
#
# 重要：
# 兩個條件若區間重疊且方向相反（一個要求中間點 > 端點，一個要求中間點 < 端點），則矛盾。
#
# 因此，問題化為檢查區間條件是否有矛盾：
# - 對每個人 i，記錄區間 [l_i, r_i] 和方向 d_i = +1 (S_i < T_i) 或 -1 (S_i > T_i)
# - 若兩個區間重疊且方向相反，則無解。
#
# 查詢要求：
# 對區間 [L_k, R_k] 的人，判斷是否所有條件可同時滿足。
#
# 解法：
# 1. 對所有人 i，記錄 (l_i, r_i, d_i)
# 2. 對所有人 i，找出與 i 有重疊且方向相反的最早衝突位置 j
# 3. 建立一個衝突陣列 conflict[i] = 最早與 i 衝突的索引（若無衝突則為 M+1）
# 4. 對查詢 [L,R]，判斷是否存在 i in [L,R] 使 conflict[i] ≤ R
#    若有，輸出 No，否則 Yes
#
# 實作細節：
# - 對 d=+1 和 d=-1 的人分別排序
# - 使用雙指標掃描兩組區間，找重疊且方向相反的衝突
# - 衝突記錄為雙向
# - 建立 conflict 陣列後，建 segment tree 或 prefix min 方便查詢
#

pos_plus = []
pos_minus = []
for i, (S, T) in enumerate(people, 1):
    l = min(S, T)
    r = max(S, T)
    d = 1 if S < T else -1
    if d == 1:
        pos_plus.append((l, r, i))
    else:
        pos_minus.append((l, r, i))

pos_plus.sort(key=lambda x: (x[0], x[1]))
pos_minus.sort(key=lambda x: (x[0], x[1]))

conflict = [M+1]*(M+1)  # 1-based，conflict[i] = 最早衝突索引，初始無衝突為 M+1

# 對兩組區間找重疊衝突
# 使用雙指標掃描 pos_plus 和 pos_minus
j = 0
# pos_minus 按 l 排序
for l1, r1, i1 in pos_plus:
    # 對 pos_minus 中 l2 <= r1 的區間檢查重疊
    while j < len(pos_minus) and pos_minus[j][0] <= r1:
        j += 1
    # j 指向第一個 l2 > r1
    # pos_minus[0..j-1] 的 l2 <= r1，可能重疊
    # 但要找所有與 (l1,r1) 重疊的 pos_minus
    # 使用二分找 pos_minus 中 r2 >= l1 的區間
    # 因 pos_minus 按 l 排序，r 不一定排序，故用線性掃描
    # 為效率，先用指標 k 從 0 開始掃描 pos_minus
    # 但因 j 可能很大，改用雙指標法：
    # 先用二分找 pos_minus 中第一個 l2 > r1 的位置 j
    # 再從 0 到 j-1 掃描，找 r2 >= l1 的重疊區間
    # 但這會超時，改用兩個指標分別掃描 pos_plus 和 pos_minus
    # 重新實作雙指標：
    pass

# 改用雙指標掃描：
# pos_plus 和 pos_minus 都按 l 排序
# 對 pos_plus[i], pos_minus[j]：
# 若區間重疊且方向相反，記錄衝突

i = 0
j = 0
len_p = len(pos_plus)
len_m = len(pos_minus)

# 為避免重複檢查，對 pos_plus 和 pos_minus 兩邊分別掃描
# 使用兩個指標 i,j，當 pos_plus[i].l <= pos_minus[j].r 且 pos_minus[j].l <= pos_plus[i].r 時重疊

# 先建立 pos_plus 和 pos_minus 的 l,r,i 陣列方便操作
lp = [x[0] for x in pos_plus]
rp = [x[1] for x in pos_plus]
ip = [x[2] for x in pos_plus]

lm = [x[0] for x in pos_minus]
rm = [x[1] for x in pos_minus]
im = [x[2] for x in pos_minus]

# 對 pos_plus 中每個區間，找 pos_minus 中重疊區間
j = 0
for i in range(len_p):
    l1, r1, idx1 = lp[i], rp[i], ip[i]
    # 移動 j 使 pos_minus[j].r >= l1
    while j < len_m and rm[j] < l1:
        j += 1
    k = j
    # 從 k 開始掃描 pos_minus，直到 l2 > r1
    while k < len_m and lm[k] <= r1:
        # 重疊條件已滿足
        idx2 = im[k]
        # 記錄衝突雙向
        if idx2 < conflict[idx1]:
            conflict[idx1] = idx2
        if idx1 < conflict[idx2]:
            conflict[idx2] = idx1
        k += 1

# conflict[i] = 最早與 i 衝突的索引，若無衝突為 M+1

# 為方便查詢區間 [L,R] 是否有衝突 i，且 conflict[i] ≤ R
# 建立一個陣列 min_conflict_prefix，min_conflict_prefix[i] = min(conflict[1..i])
min_conflict_prefix = [M+1]*(M+1)
for i in range(1, M+1):
    min_conflict_prefix[i] = min(min_conflict_prefix[i-1], conflict[i])

# 對每個查詢 [L,R]，判斷是否存在 i in [L,R] 使 conflict[i] ≤ R
# 等價於 min_conflict_prefix[R] ≤ R 且 min_conflict_prefix[R] ≥ L
# 但 min_conflict_prefix 是 prefix min，無法直接判斷區間內最小值
# 改用 segment tree 或 sparse table 查詢區間最小值

# 建立 segment tree 查詢 conflict[i] 的區間最小值
size = 1
while size < M:
    size <<= 1
seg = [M+1]*(2*size)

for i in range(M):
    seg[size+i] = conflict[i+1]
for i in range(size-1, 0, -1):
    seg[i] = min(seg[i<<1], seg[i<<1|1])

def query(l, r):
    # 查詢區間 [l,r] 最小值，1-based
    l += size -1
    r += size -1
    res = M+1
    while l <= r:
        if (l & 1) == 1:
            res = min(res, seg[l])
            l += 1
        if (r & 1) == 0:
            res = min(res, seg[r])
            r -= 1
        l >>= 1
        r >>= 1
    return res

output = []
for L, R in queries:
    mn = query(L, R)
    # 若區間內有 i 使 conflict[i] ≤ R，則無解
    if mn <= R:
        output.append("No")
    else:
        output.append("Yes")

print("\n".join(output))