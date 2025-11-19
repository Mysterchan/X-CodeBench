import sys
input = sys.stdin.readline
MOD = 998244353

N, a, b = map(int, input().split())
Q = int(input())
ks = list(map(int, input().split()))

# 根據題意，對於每個 K 級 L 形狀，(a,b) 是否包含在該 L 形狀中，
# 取決於 (a,b) 是否能成為該 L 形狀的起點 (i,j) 且滿足四種方向條件之一。

# 四種方向的起點範圍：
# 1) 向下或向右：1 ≤ i ≤ N-K+1, 1 ≤ j ≤ N-K+1
# 2) 向下或向左：1 ≤ i ≤ N-K+1, K ≤ j ≤ N
# 3) 向上或向右：K ≤ i ≤ N, 1 ≤ j ≤ N-K+1
# 4) 向上或向左：K ≤ i ≤ N, K ≤ j ≤ N

# (a,b) 包含在 K 級 L 形狀中，等價於存在起點 (i,j) 使得 (a,b) 在該 L 形狀中。
# L 形狀的格子是從起點 (i,j) 向兩個方向移動 0~K-1 格的格子。
# 因此 (a,b) 必須在該 L 形狀的範圍內。

# 對於每種方向，我們求出起點 (i,j) 的範圍，使得 (a,b) 在該 L 形狀中。

# 以第一種方向為例（向下或向右）：
# 起點 (i,j) 滿足：
# i ≤ a ≤ i + K - 1
# j ≤ b ≤ j + K - 1
# 且 1 ≤ i ≤ N-K+1, 1 ≤ j ≤ N-K+1

# 因此 i ∈ [max(1, a - K + 1), min(a, N - K + 1)]
# j ∈ [max(1, b - K + 1), min(b, N - K + 1)]

# 起點數量 = max(0, i_range_size) * max(0, j_range_size)

# 其他三種方向類似。

# 對每個 K，我計算四種方向的起點數量，取最大值即為該 K 級 L 形狀中包含 (a,b) 的起點數量。

# 題目要求「將網格劃分為恰好一個 1 級 L 形狀、一個 2 級 L 形狀、...、一個 N 級 L 形狀的方式數」，
# 且該方式數是所有級別 L 形狀起點數量的乘積。
# 但題目中 Q 個查詢是對每個 k_i，輸出「將網格劃分為恰好一個 1 級 L 形狀、一個 2 級 L 形狀、...、一個 N 級 L 形狀的方式數，使得 (a,b) 包含在 k_i 級 L 形狀中」。
# 這表示對每個 k_i，我們計算：
#   (所有級別 L 形狀起點數量的乘積) 中，該 k_i 級 L 形狀的起點數量必須是包含 (a,b) 的起點數量，
#   其他級別的起點數量不受限制（即所有可能起點數量）。

# 因此，我們先預處理所有 K 級的起點數量（四種方向最大值），
# 並計算前綴乘積（mod 998244353）。

# 對於每個 k_i，輸出：
#   (前綴乘積[N]) * (包含 (a,b) 的 k_i 級 L 形狀起點數量) / (k_i 級 L 形狀所有起點數量)
# 但題目中「將網格劃分為恰好一個 1 級 L 形狀、一個 2 級 L 形狀、...、一個 N 級 L 形狀的方式數，使得 (a,b) 包含在 k_i 級 L 形狀中」，
# 其實就是將 k_i 級 L 形狀的起點數量限制為包含 (a,b) 的起點數量，
# 其他級別的起點數量不變。

# 因為每級 L 形狀的起點數量是固定的，且獨立，
# 所以答案 = (所有級別起點數量的乘積) / (k_i 級 L 形狀所有起點數量) * (k_i 級 L 形狀包含 (a,b) 的起點數量)

# 但題目中「將網格劃分為恰好一個 1 級 L 形狀、一個 2 級 L 形狀、...、一個 N 級 L 形狀的方式數」，
# 這表示每級 L 形狀的起點數量就是該級別的方式數。

# 因此，我們先計算每級 L 形狀的起點數量（四種方向最大值），
# 並計算前綴乘積。

# 對於每個 k_i，輸出：
#   (前綴乘積[N] * 包含(a,b)的k_i級L形狀起點數量) * 逆元(該k_i級L形狀所有起點數量) mod

# 但題目中沒有說要除以該級別的起點數量，
# 而是「將網格劃分為恰好一個 1 級 L 形狀、一個 2 級 L 形狀、...、一個 N 級 L 形狀的方式數，使得 (a,b) 包含在 k_i 級 L 形狀中」，
# 這表示該級別的 L 形狀起點必須包含 (a,b)，即該級別的起點數量 = 包含 (a,b) 的起點數量，
# 其他級別的起點數量不變。

# 因此答案 = (所有級別起點數量的乘積) / (k_i 級 L 形狀所有起點數量) * (k_i 級 L 形狀包含 (a,b) 的起點數量)

# 先計算每級的所有起點數量（四種方向最大值）
# 再計算每級包含 (a,b) 的起點數量（四種方向起點範圍交集）
# 再計算前綴乘積
# 再對每個 k_i 計算答案

# 由於 N 可達 10^7，需用 O(N) 解法，且記憶體限制，需用生成器或線上計算。

# 實作細節：
# 對每個 K 計算四種方向的起點數量：
# 方向1: i in [1, N-K+1], j in [1, N-K+1]
# 起點數量 = (N-K+1)^2

# 方向2: i in [1, N-K+1], j in [K, N]
# 起點數量 = (N-K+1)*(N-K+1)

# 方向3: i in [K, N], j in [1, N-K+1]
# 起點數量 = (N-K+1)*(N-K+1)

# 方向4: i in [K, N], j in [K, N]
# 起點數量 = (N-K+1)^2

# 其實四種方向的起點數量都相同 = (N-K+1)^2

# 但題目中四種方向的起點範圍不同，起點數量相同。

# 包含 (a,b) 的起點數量計算：
# 對每種方向，計算起點 i,j 範圍使得 (a,b) 在 L 形狀中。

# 實作計算函數：

def count_range(l, r):
    return max(0, r - l + 1)

def count_dir1(K):
    # 向下或向右
    i_l = max(1, a - K + 1)
    i_r = min(a, N - K + 1)
    j_l = max(1, b - K + 1)
    j_r = min(b, N - K + 1)
    return count_range(i_l, i_r) * count_range(j_l, j_r)

def count_dir2(K):
    # 向下或向左
    i_l = max(1, a - K + 1)
    i_r = min(a, N - K + 1)
    j_l = max(K, b)
    j_r = N
    # (a,b) 在 L 形狀中 => j in [j_l, j_r], 且 b in [j, j+K-1]
    # j ≤ b ≤ j + K -1 => j ∈ [b - K + 1, b]
    # j must satisfy both:
    # j ≥ K and j ≥ b - K + 1
    # j ≤ N and j ≤ b
    j_start = max(j_l, b - K + 1)
    j_end = min(j_r, b)
    return count_range(i_l, i_r) * count_range(j_start, j_end)

def count_dir3(K):
    # 向上或向右
    i_l = max(K, a)
    i_r = N
    j_l = max(1, b - K + 1)
    j_r = min(b, N - K + 1)
    # i in [i_l, i_r], i ≤ a ≤ i + K -1 => i ∈ [a - K + 1, a]
    i_start = max(i_l, a - K + 1)
    i_end = min(i_r, a)
    return count_range(i_start, i_end) * count_range(j_l, j_r)

def count_dir4(K):
    # 向上或向左
    i_l = max(K, a)
    i_r = N
    j_l = max(K, b)
    j_r = N
    # i ∈ [a - K + 1, a]
    i_start = max(i_l, a - K + 1)
    i_end = min(i_r, a)
    # j ∈ [b - K + 1, b]
    j_start = max(j_l, b - K + 1)
    j_end = min(j_r, b)
    return count_range(i_start, i_end) * count_range(j_start, j_end)

# 預計算每級的所有起點數量 = (N-K+1)^2
# 預計算每級包含 (a,b) 的起點數量 = max(四方向包含數量)

# 由於 N 可達 10^7，Q 最多 2*10^5，無法全部預計算。
# 只需對 Q 中的 k_i 計算包含 (a,b) 的起點數量。
# 但要計算所有級別的起點數量乘積，需 O(N)。
# N=10^7，計算乘積可行，但記憶體存放10^7整數不可行。
# 需用線上計算。

# 先計算 prefix_prod:
# prefix_prod[0] = 1
# prefix_prod[k] = prefix_prod[k-1] * (N - k + 1)^2 mod

# 由於 Q ≤ 2*10^5，且 k_i 有序，我們可以只計算 prefix_prod 到 max(k_i)

max_k = ks[-1]

prefix_prod = [1] * (max_k + 1)
for k in range(1, max_k + 1):
    val = (N - k + 1)
    prefix_prod[k] = prefix_prod[k-1] * (val * val % MOD) % MOD

# 計算包含 (a,b) 的起點數量函數
def contain_count(K):
    c1 = count_dir1(K)
    c2 = count_dir2(K)
    c3 = count_dir3(K)
    c4 = count_dir4(K)
    return max(c1, c2, c3, c4)

# 計算所有級別起點數量乘積 = prefix_prod[N]
# 但 prefix_prod 只計算到 max_k，N 可能更大。
# 題目中 Q ≤ min(N, 200000)，且 k_i ≤ N
# 但題目要求「將網格劃分為恰好一個 1 級 L 形狀、一個 2 級 L 形狀、...、以及一個 N 級 L 形狀的方式數」
# 這表示要計算 prefix_prod[N]，N 可達 10^7，無法全部計算。

# 觀察題目範例，輸出結果是對 k_i 級 L 形狀包含 (a,b) 的方式數，
# 這是「將網格劃分為恰好一個 1 級 L 形狀、一個 2 級 L 形狀、...、一個 N 級 L 形狀的方式數，使得 (a,b) 包含在 k_i 級 L 形狀中」，
# 也就是所有級別起點數量乘積中，k_i 級 L 形狀的起點數量被限制為包含 (a,b) 的起點數量。

# 但題目中沒有要求輸出整個乘積，只要求對每個 k_i 輸出該條件下的方式數。

# 由於每級 L 形狀的起點數量為 (N-K+1)^2，
# 且包含 (a,b) 的起點數量 ≤ (N-K+1)^2，
# 方式數 = ∏_{k=1}^N 起點數量，
# 但第 k_i 級的起點數量改為包含 (a,b) 的起點數量。

# 因此答案 = (∏_{k=1}^N (N-k+1)^2) / ( (N-k_i+1)^2 ) * contain_count(k_i)

# ∏_{k=1}^N (N-k+1)^2 = (N!)^2 mod

# 計算 factorial 和逆元：

max_val = N
# 由於 N 可達 10^7，計算 factorial 需要大量記憶體和時間，可能超時。
# 但題目中 Q ≤ min(N, 200000)，且 k_i ≤ N。
# 我們只需計算 factorial 到 N。

# 使用快速階乘計算：

fact = [1] * (N + 1)
for i in range(1, N + 1):
    fact[i] = fact[i-1] * i % MOD

inv_fact = [1] * (N + 1)
inv_fact[N] = pow(fact[N], MOD - 2, MOD)
for i in range(N - 1, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

def n_factorial(n):
    return fact[n]

def n_factorial_inv(n):
    return inv_fact[n]

# ∏_{k=1}^N (N-k+1)^2 = (N!)^2 mod
total = fact[N] * fact[N] % MOD

# 對每個 k_i 計算答案：
# ans = total * contain_count(k_i) * inv((N-k_i+1)^2) mod
# (N-k_i+1)^2 = val^2
# 逆元 = pow(val, -2, MOD) = pow(val, MOD-1-2, MOD) = pow(val, MOD-3, MOD)

for k_i in ks:
    val = N - k_i + 1
    inv_val_sq = pow(val, MOD - 3, MOD)  # val^{-2} mod
    c = contain_count(k_i)
    ans = total * c % MOD
    ans = ans * inv_val_sq % MOD
    print(ans)