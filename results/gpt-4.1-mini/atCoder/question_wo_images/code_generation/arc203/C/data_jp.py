import sys
input = sys.stdin.readline
MOD = 998244353

# 問題の本質:
# H×W のグリッドで、左上から右下へ移動可能にするために壊す壁の数がK枚。
# 移動可能にするための最小の壁の数は (H-1)+(W-1) = H+W-2 で、
# それは最短経路の壁の数。
# 条件を満たす壁の組の数は、K枚の壁を選んで左上から右下へ移動可能になる数。
#
# 解析:
# 壁は縦方向に (H-1)*W 枚、横方向に H*(W-1) 枚ある。
# しかし、問題の条件は「左上から右下へ移動可能」なので、
# 最短経路の壁を壊す必要がある。
#
# 最短経路の壁の数は H+W-2。
# これらの壁を壊さずに移動可能にはならない。
#
# さらに、最短経路の壁を壊した上で、残りの壁を壊すか壊さないかは自由。
# つまり、K枚の壁を選ぶとき、必ず最短経路の壁全てを含んでいなければならない。
#
# よって、
# - K < H+W-2 のときは0通り。
# - K >= H+W-2 のときは、
#   最短経路の壁 (H+W-2枚) は必須で選ぶ。
#   残りの壁は total_walls - (H+W-2) 枚あり、
#   そこから K-(H+W-2) 枚を選ぶ組み合わせ数。
#
# total_walls = (H-1)*W + H*(W-1) = 2*H*W - H - W
#
# よって答えは
# C(total_walls - (H+W-2), K-(H+W-2)) mod 998244353
# ただし K >= H+W-2 でなければ0。

# ただし、K ≤ H+W と制約があるので、
# K-(H+W-2) ≤ 2 となることが多いが、
# 入力例に400000があるので大きい場合もある。

# 組み合わせ計算のために階乗と逆元を前計算する。

MAX = 400000 + 10  # 最大値は H,W最大で約2*10^5なので余裕を持って

fact = [1]*(MAX)
inv_fact = [1]*(MAX)

def modinv(a, m=MOD):
    # フェルマーの小定理による逆元計算
    return pow(a, m-2, m)

for i in range(1, MAX):
    fact[i] = fact[i-1]*i % MOD
inv_fact[MAX-1] = modinv(fact[MAX-1], MOD)
for i in reversed(range(1, MAX)):
    inv_fact[i-1] = inv_fact[i]*i % MOD

def comb(n, r):
    if r > n or r < 0:
        return 0
    return fact[n]*inv_fact[r]%MOD*inv_fact[n-r]%MOD

T = int(input())
for _ in range(T):
    H,W,K = map(int,input().split())
    min_needed = H + W - 2
    if K < min_needed:
        print(0)
        continue
    total_walls = (H-1)*W + H*(W-1)  # 壁の総数
    # K枚の壁を選ぶとき、必ず最短経路の壁 min_needed 枚は含む必要がある
    # 残りの壁から K - min_needed 枚を選ぶ組み合わせ
    ans = comb(total_walls - min_needed, K - min_needed)
    print(ans % MOD)