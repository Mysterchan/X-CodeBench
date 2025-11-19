import sys
sys.setrecursionlimit(10**7)
MOD = 998244353

N = int(sys.stdin.readline())

# 問題の条件を整理すると：
# 「任意の回路の辺数が素数である」かつ「単純無向連結グラフ」
# 回路とは閉路（同じ辺を2回以上通らない閉じた道）であり、
# 同じ頂点を複数回通ってもよい。
#
# 重要なポイント：
# - すべての回路の長さ（辺数）が素数である。
#
# まず、グラフが連結である。
# 次に、回路の長さが素数であることから、
# もし回路の長さが合成数（素数でない）なら条件を満たさない。
#
# つまり、グラフに存在するすべての回路の長さは素数でなければならない。
#
# ここで、グラフの回路の長さは最小のサイクル長（girth）以上である。
# さらに、任意の回路の長さが素数であるためには、
# すべての回路の長さが同じ素数でなければならない（そうでなければ合成数の回路ができる）。
#
# しかし、複数の異なる素数長の回路が存在すると、
# それらの回路の辺の和や差で合成数の回路ができる可能性がある。
#
# したがって、グラフは「すべての回路の長さが同じ素数p」である必要がある。
#
# さらに、グラフは単純無向連結である。
#
# ここで、グラフの回路の長さがすべて同じ素数pであるグラフは、
# 「p長の単一のサイクル」か「木にp長のサイクルを1つだけ持つグラフ」などが考えられるが、
# 複数のサイクルがあると、回路の長さの和や差で合成数の回路ができるため不適。
#
# よって、条件を満たすグラフは以下のいずれか：
# - 木（回路がないので条件を満たす）
# - 単一のサイクル（長さが素数）
#
# しかし、単一のサイクルの長さはN（頂点数）であるため、
# Nが素数のときのみ単一サイクルが条件を満たす。
#
# それ以外の複雑なグラフは条件を満たさない。
#
# まとめ：
# 条件を満たすグラフは
# - 木（辺数 = N-1）
# - Nが素数なら単一サイクル（辺数 = N）
#
# これらのグラフの個数を求める。
#
# 木の個数は、頂点数Nのラベル付き木の数はN^(N-2)（カルタンの公式）
#
# 単一サイクルグラフは、Nが素数のときに存在し、その個数は
# 頂点のラベル付き単一サイクルの数は (N-1)! / 2
# （N頂点のサイクルグラフの数は (N-1)! / 2）
#
# よって答えは
# 木の数 + (Nが素数なら単一サイクルの数)
#
# これをMODで割った余りを出力する。
#
# ただし、N=1のときは木は1個（頂点1つの木）、単一サイクルは存在しない。
#
# 以上の理論をコードに落とす。

# 素数判定（高速化のためミラーラビン法を使用）
def is_prime(n):
    if n < 2:
        return False
    for p in [2,3,5,7,11,13,17,19,23]:
        if n == p:
            return True
        if n % p == 0 and n != p:
            return False
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    def check(a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                return True
        return False
    for a in [2,3,5,7,11]:
        if a >= n:
            break
        if not check(a):
            return False
    return True

# 階乗と逆元の事前計算
max_n = N
fact = [1] * (max_n + 1)
inv_fact = [1] * (max_n + 1)
for i in range(2, max_n + 1):
    fact[i] = fact[i-1] * i % MOD

# フェルマーの小定理による逆元計算
inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)
for i in reversed(range(1, max_n)):
    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

def mod_comb(n, r):
    if r > n or r < 0:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n-r] % MOD

# 木の数 = N^(N-2) mod MOD (N>=1)
if N == 1:
    tree_count = 1
else:
    tree_count = pow(N, N-2, MOD)

# 単一サイクルの数 = (N-1)! / 2 mod MOD (Nが素数かつN>=3)
cycle_count = 0
if N >= 3 and is_prime(N):
    # (N-1)! / 2 mod MOD
    inv2 = (MOD + 1) // 2
    cycle_count = fact[N-1] * inv2 % MOD

ans = (tree_count + cycle_count) % MOD
print(ans)