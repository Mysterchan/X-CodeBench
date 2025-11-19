import sys
import math
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

MAX_A = 10**6

freq = [0]*(MAX_A+1)
for v in A:
    freq[v] += 1

# cnt[d]: Aの中でdの倍数の個数
cnt = [0]*(MAX_A+1)
for d in range(1, MAX_A+1):
    s = 0
    for m in range(d, MAX_A+1, d):
        s += freq[m]
    cnt[d] = s

# dp[d]: 最大公約数がdとなるようなK個の要素の集合が存在するか(1なら存在)
# ここでは存在判定だけでなく、最大値を求めるために
# dp[d] = True if cnt[d]>=K and no multiple of d with larger gcd satisfies condition
dp = [False]*(MAX_A+1)
for d in range(MAX_A, 0, -1):
    if cnt[d] >= K:
        dp[d] = True
        # dの倍数でdより大きいものがTrueならdp[d]はFalseにする
        # しかしここは最大値を求めるために、後で使うのでTrueのままにする

# res[i]: i番目の要素を含むK個の要素の最大GCD
res = [1]*N

# A_iの約数を列挙し、dp[d]がTrueの最大のdを求める
# 約数列挙は高速化のため事前に素因数分解して約数列挙関数を用いる

# 素因数分解用の最小素因数テーブル
spf = [0]*(MAX_A+1)
def build_spf():
    spf[1] = 1
    for i in range(2, MAX_A+1):
        if spf[i] == 0:
            spf[i] = i
            for j in range(i*i, MAX_A+1, i):
                if spf[j] == 0:
                    spf[j] = i
build_spf()

def get_divisors(x):
    # 素因数分解
    pf = []
    while x > 1:
        p = spf[x]
        cnt = 0
        while x % p == 0:
            x //= p
            cnt += 1
        pf.append((p, cnt))
    # 約数列挙
    divisors = [1]
    for p, c in pf:
        new_divs = []
        for d in divisors:
            val = d
            for _ in range(c):
                val *= p
                new_divs.append(val)
        divisors += new_divs
    return divisors

for i in range(N):
    divisors = get_divisors(A[i])
    ans = 1
    for d in divisors:
        if dp[d]:
            if d > ans:
                ans = d
    res[i] = ans

print('\n'.join(map(str, res)))