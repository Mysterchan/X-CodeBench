MOD = 998244353

H, W = map(int, input().split())

# 各行の操作は c_r (0 <= c_r <= W) を選ぶ（c_r=0は操作しない）
# 各列の操作は r_c (0 <= r_c <= H) を選ぶ（r_c=0は操作しない）
# 行列の要素 A[i,j] = 1 iff j <= c_i or i <= r_j

# すべての行列は (c_1,...,c_H), (r_1,...,r_W) の組み合わせで決まる
# c_i ∈ [0,W], r_j ∈ [0,H]

# 総数は (W+1)^H * (H+1)^W 通り

# A[i,j] = 1 iff j <= c_i or i <= r_j
# sum of elements = sum_{i=1}^H sum_{j=1}^W [j <= c_i or i <= r_j]

# これを全ての組み合わせで合計する

# 1) sum over all c_i, r_j of sum_{i,j} A[i,j]
# = sum_{i=1}^H sum_{j=1}^W sum_{c_i=0}^W sum_{r_j=0}^H [j <= c_i or i <= r_j] * (product over other c_k and r_l of counts)
# ただし c_i と r_j は独立なので積に分解可能

# 2) c_i は独立、r_j は独立なので
# 全体の組み合わせ数 = (W+1)^H * (H+1)^W

# 3) A[i,j] = 1 iff (j <= c_i) or (i <= r_j)
# これの期待値を考えると、
# E[A[i,j]] = P(j <= c_i or i <= r_j)
# = 1 - P(j > c_i and i > r_j)
# = 1 - P(c_i < j) * P(r_j < i)
# c_i は一様に0..Wなので P(c_i < j) = j/(W+1)
# r_j は一様に0..Hなので P(r_j < i) = i/(H+1)

# よって
# E[A[i,j]] = 1 - (j/(W+1))*(i/(H+1))

# 4) 総和 = sum_{i=1}^H sum_{j=1}^W E[A[i,j]] * 総組み合わせ数
# = (W+1)^H * (H+1)^W * sum_{i=1}^H sum_{j=1}^W (1 - (i*j)/((H+1)(W+1)))

# 5) sum_{i=1}^H sum_{j=1}^W 1 = H*W
# sum_{i=1}^H sum_{j=1}^W (i*j) = (sum_{i=1}^H i) * (sum_{j=1}^W j) = (H(H+1)/2)*(W(W+1)/2)

# 6) よって
# sum = (W+1)^H * (H+1)^W * (H*W - (H(H+1)/2)*(W(W+1)/2)/((H+1)(W+1)))
# = (W+1)^H * (H+1)^W * (H*W - (H*W*(H+1)*(W+1))/4 / ((H+1)(W+1)))
# = (W+1)^H * (H+1)^W * (H*W - (H*W)/4)
# = (W+1)^H * (H+1)^W * (3/4)*H*W

# 7) ただし分数はMODで計算するので逆元を使う

inv4 = pow(4, MOD-2, MOD)

HW = H * W % MOD
powW = pow(W+1, H, MOD)
powH = pow(H+1, W, MOD)

ans = powW * powH % MOD
ans = ans * HW % MOD
ans = ans * 3 % MOD
ans = ans * inv4 % MOD

print(ans)