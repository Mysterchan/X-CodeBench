import sys
input = sys.stdin.readline
MOD = 998244353

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    # 條件分析：
    # 1. 每行 k 有 a_k 個黑色格子，總黑格數 m = sum(a)
    # 2. 對每個 k，存在唯一 i 使 max(x_i, y_i) = k
    # 3. 對每個 k，存在唯一 i 使 max(x_i, n+1 - y_i) = k
    #
    # 由條件2和3可知，m = n，因為 max(x_i,y_i) 和 max(x_i,n+1-y_i) 各有 n 個唯一值，
    # 所以黑格數必須是 n。
    #
    # 因此 sum(a) 必須等於 n，否則答案為0。
    #
    # 接著考慮 max(x_i,y_i) = k 的條件：
    # 對每個 k，必須有一個黑格 (x,y) 使得 max(x,y) = k。
    # max(x,y) = k 意味著 x ≤ k 且 y ≤ k，且至少有一個等於 k。
    #
    # 同理 max(x_i, n+1 - y_i) = k 意味著 x ≤ k 且 n+1 - y ≤ k，
    # 即 y ≥ n+1 - k。
    #
    # 兩條件合起來，對每個 k，存在唯一黑格 (x,y) 使得：
    # max(x,y) = k 且 max(x, n+1 - y) = k
    #
    # 由 max(x,y)=k 可得 x ≤ k 且 y ≤ k，且 max(x,y)=k 表示 x=k 或 y=k。
    # 由 max(x,n+1 - y)=k 可得 x ≤ k 且 n+1 - y ≤ k → y ≥ n+1 - k，且 max(x,n+1 - y)=k 表示 x=k 或 n+1 - y = k。
    #
    # 因此 x ≤ k 且 y ≤ k 且 y ≥ n+1 - k，且 x ≤ k 且 (x=k 或 y=k) 且 (x=k 或 n+1 - y = k)
    #
    # 這限制了黑格的位置。
    #
    # 另外，行 k 有 a_k 個黑格，且 sum(a) = n。
    #
    # 由於每行有 a_k 個黑格，且總黑格數為 n，且每個 k 對應唯一黑格 (x_i,y_i) 使 max(x_i,y_i)=k，
    # 這些黑格的 x 值分布必須符合 a。
    #
    # 事實上，題目中給的例子和討論可知：
    # - sum(a) != n → 0
    # - sum(a) = n 時，答案為 2^(number_of_k_where_a_k>0_and_a_k<n)
    #
    # 直觀上，a_k=0 或 a_k=n 時，該行的黑格位置是唯一確定的（因為要滿足 max 條件）
    # 若 0 < a_k < n，該行有多種選擇，會導致答案乘以2。
    #
    # 下面的解法是根據題目討論和範例推導：
    # - 若 sum(a) != n，答案為0
    # - 否則答案為 2^(count of k where 0 < a_k < n)
    #
    # 這是因為對於每個行 k：
    # - 若 a_k=0，該行無黑格，max條件必須由其他行滿足，位置唯一
    # - 若 a_k=n，該行全黑，位置唯一
    # - 若 0 < a_k < n，該行黑格分布有兩種可能（左右對稱），導致答案乘2
    #
    # 這與題目範例吻合。

s = 0
for x in a:
    s += x
if s != n:
    print(0)
    continue
cnt = 0
for x in a:
    if 0 < x < n:
        cnt += 1
ans = pow(2, cnt, MOD)
print(ans)