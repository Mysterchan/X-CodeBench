import sys
input = sys.stdin.readline

N, X = map(int, input().split())
U = [0]*N
D = [0]*N
S = [0]*N
for i in range(N):
    u,d = map(int, input().split())
    U[i] = u
    D[i] = d
    S[i] = u + d

# 我们要找到一个H，使得对所有i，U_i + D_i = H
# 同时满足 |U_i - U_{i+1}| ≤ X
# 只能通过减少牙齿长度来达到条件，减少的总和最小

# 设H为目标和，且H ≤ min(S)（因为只能减少）
# 对固定H，U_i ≤ S_i 且 U_i + D_i = H => U_i = H - D_i
# 但U_i必须满足 |U_i - U_{i+1}| ≤ X
# 也就是说，序列U_i满足差分限制，且U_i ≤ S_i且U_i ≤ H - D_i

# 由于U_i = H - D_i，且U_i ≥ 0（长度不能负）
# 但题目中只说减少长度，不允许增加，故U_i ≤ 原U_i，D_i ≤ 原D_i
# 但我们只减少牙齿长度，不能增加
# 因此U_i ≤ 原U_i，D_i ≤ 原D_i
# 但U_i = H - D_i，D_i = H - U_i
# 由于只能减少，U_i ≤ 原U_i，D_i ≤ 原D_i
# => H - D_i ≤ 原U_i => H ≤ 原U_i + D_i = S_i
# => H ≤ S_i 对所有i成立

# 因此H ≤ min(S)

# 目标是找到最大H，使得存在U序列满足：
# 1) |U_i - U_{i+1}| ≤ X
# 2) 0 ≤ U_i ≤ min(U_i原始, H - D_i原始)
# 其中U_i原始 = U[i], D_i原始 = D[i]

# 由于U_i = H - D_i，且D_i = H - U_i
# 但我们只能减少长度，不能增加
# 所以U_i ≤ U[i], D_i ≤ D[i]
# => U_i ≤ U[i]
# => D_i = H - U_i ≤ D[i] => U_i ≥ H - D[i]

# 因此U_i的范围是：
# max(0, H - D[i]) ≤ U_i ≤ min(U[i], H)

# 但H ≤ min(S)，且H ≤ S[i] = U[i] + D[i]
# 所以H - D[i] ≤ U[i] + D[i] - D[i] = U[i]
# 所以区间是合理的

# 现在问题转化为：
# 对给定H，是否存在序列U满足：
# max(0, H - D[i]) ≤ U_i ≤ min(U[i], H)
# 且 |U_i - U_{i+1}| ≤ X

# 我们用区间DP：
# 从左到右维护U_i的可行区间
# 初始区间为 [max(0,H-D[0]), min(U[0],H)]
# 对于i从1到N-1:
#   U_i的区间为 [L_i, R_i] = [max(0,H-D[i]), min(U[i],H)]
#   结合差分限制：
#   U_i ∈ [L_i, R_i] ∩ [L_{i-1}-X, R_{i-1}+X]
#   更新区间为交集
# 如果区间为空，则不可行

# 同理从右到左也做一次，取交集，保证双向限制

# 最后判断区间是否非空，若非空则H可行

# 用二分搜索H，范围[0, min(S)]

S_min = min(S)

def can(H):
    L = [0]*N
    R = [0]*N
    for i in range(N):
        L[i] = max(0, H - D[i])
        R[i] = min(U[i], H)
        if L[i] > R[i]:
            return False
    # 从左到右
    for i in range(1, N):
        L[i] = max(L[i], L[i-1] - X)
        R[i] = min(R[i], R[i-1] + X)
        if L[i] > R[i]:
            return False
    # 从右到左
    for i in range(N-2, -1, -1):
        L[i] = max(L[i], L[i+1] - X)
        R[i] = min(R[i], R[i+1] + X)
        if L[i] > R[i]:
            return False
    return True

left, right = 0, S_min
while left < right:
    mid = (left + right + 1) // 2
    if can(mid):
        left = mid
    else:
        right = mid - 1

H = left

# 找到最大H后，计算最小花费
# 对每个i，U_i ∈ [max(0,H-D[i]), min(U[i],H)] 且满足差分限制
# 我们可以用同样的区间DP求出一个具体的U序列，使得减少量最小
# 减少量 = sum(U[i]_original - U_i) + sum(D[i]_original - D_i)
# 但D_i = H - U_i
# 减少量 = sum(U[i] - U_i) + sum(D[i] - (H - U_i)) = sum(U[i] + D[i] - H) = sum(S[i] - H)

# 因为H固定，减少量固定为 sum(S[i]) - N*H

ans = sum(S) - N*H
print(ans)