import sys
input = sys.stdin.readline

N, X = map(int, input().split())
U = [0]*N
D = [0]*N
for i in range(N):
    u, d = map(int, input().split())
    U[i] = u
    D[i] = d

# まず、H = U_i + D_i となるように調整する必要がある。
# 操作は歯の長さを1減らすことのみなので、Hは元のU_i + D_iの最大値以下でなければならない。
# Hを決めたら、U_i' = H - D_i とし、U_i' <= U_i かつ U_i' > 0 でなければならない（歯の長さは正）
# また、|U_i' - U_{i+1}'| <= X の条件も満たす必要がある。

# したがって、Hを決めてから、U_i'を決める問題になる。
# U_i' = H - D_i なので、U_i'はHに依存する。
# しかし、U_i'はU_iより小さくなければならない（削るだけなので）
# さらに、U_i' > 0 でなければならない。

# 条件を満たすHの範囲を探索し、最小コストを求める。

# Hの候補は U_i + D_i の最大値以下である。
# Hの下限は max(D_i + 1) 以上（U_i' = H - D_i > 0 より）

# しかし、Hの範囲は非常に大きい（最大2*10^9程度）なので二分探索を使う。

# Hを決めたとき、U_i' = H - D_i
# ただし、U_i' <= U_i かつ U_i' > 0
# もしU_i' > U_iなら不可能（削れない）
# もしU_i' <= 0なら不可能（歯の長さは正）

# さらに、|U_i' - U_{i+1}'| <= X を満たすように調整する必要がある。
# しかし、U_i'はH - D_iで一意に決まるので、条件を満たすかどうかを判定するだけ。

# つまり、Hを決めたら、U_i' = H - D_i
# 条件を満たすか判定し、満たすならコストを計算する。

# コストは sum(U_i - U_i') = sum(U_i) - sum(U_i')
# sum(U_i)は定数なので、sum(U_i')を最大化するHを探すことになる。

# しかし、|U_i' - U_{i+1}'| <= X の条件があるため、U_i'の差が大きすぎるHは不適。

# したがって、Hを二分探索し、条件を満たすか判定し、満たすならコストを計算。

# 判定関数:
# - U_i' = H - D_i
# - すべてのiで 0 < U_i' <= U_i か？
# - すべてのiで |U_i' - U_{i+1}'| <= X か？

# 条件を満たすならTrue、そうでなければFalse

# コストは sum(U_i) - sum(U_i')

# Hの範囲は [max(D_i)+1, max(U_i + D_i)]


def can(H):
    U_prime = [H - d for d in D]
    for i in range(N):
        if U_prime[i] <= 0 or U_prime[i] > U[i]:
            return False, 0
    for i in range(N-1):
        if abs(U_prime[i] - U_prime[i+1]) > X:
            return False, 0
    cost = 0
    for i in range(N):
        cost += U[i] - U_prime[i]
    return True, cost

low = max(d + 1 for d in D)
high = max(U[i] + D[i] for i in range(N))

ans = None
while low <= high:
    mid = (low + high) // 2
    ok, cost = can(mid)
    if ok:
        ans = cost
        high = mid - 1
    else:
        low = mid + 1

print(ans)