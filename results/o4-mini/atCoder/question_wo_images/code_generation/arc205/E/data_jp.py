import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353
MAX_BIT = 20

N = int(input())
A = list(map(int, input().split()))

# A_i < 2^20なので、ビットは0~19
# 問題は、k=1..Nに対し、
# i=1..kのうち、A_i | A_k == A_k となるiの積を求める
# つまり、A_iのビットはA_kのビットの部分集合（A_i & ~A_k == 0）であるiの積

# これを効率的に求めるために、A_iの値をキーにして積を管理し、
# 部分集合和的な考えで、あるmask以下の積を求める。

# しかし、積なので部分集合和のように足し算で管理できない。
# そこで、積の管理は指数的に難しいが、A_iの値は20bitなので、
# 20bitのmaskに対して、A_iの積を管理する配列を作る。

# ただし、A_iの値は最大2^20なので、2^20=1,048,576で配列は作れる。

# まず、freq_prod[mask] = A_iの積（iでA_i==maskのもの）
freq_prod = [1]*(1<<MAX_BIT)
count = [0]*(1<<MAX_BIT)

for a in A:
    freq_prod[a] = (freq_prod[a]*a) % MOD
    count[a] += 1

# 部分集合積を求めるために、SOS DPの逆操作を行う
# ここでの操作は、maskの部分集合の積を求めること
# しかし、積は加算のように簡単に分配できないので、
# ここでの操作は「superset」方向に積を伝播させる必要がある。

# 問題の条件は、A_i | A_k == A_k
# つまり、A_iはA_kの部分集合（ビット的に）
# 部分集合積を求めるには、superset方向に積を伝播させる必要がある。

# したがって、superset方向に積を伝播させる
# superset方向のSOS DPは、ビットを1にする方向に伝播

for bit in range(MAX_BIT):
    for mask in range(1<<MAX_BIT):
        if (mask & (1 << bit)) == 0:
            freq_prod[mask] = (freq_prod[mask] * freq_prod[mask | (1 << bit)]) % MOD

# freq_prod[mask] は mask の部分集合の積ではなく、
# mask を含む superset の積になっている。
# しかし、今回の条件は A_i | A_k == A_k
# つまり、A_i は A_k の部分集合
# なので、A_k の部分集合の積を求めたい。
# superset方向に積を伝播させた freq_prod[mask] は
# mask を含む superset の積なので、
# mask の部分集合の積を求めるには逆方向のDPが必要。

# しかし、積は逆方向に簡単に戻せない。
# そこで、superset方向に積を伝播させた freq_prod[mask] は
# mask を含む superset の積なので、
# mask の部分集合の積は freq_prod[mask] の逆元を使って計算できない。

# ここで、問題の条件をよく考えると、
# A_i | A_k == A_k となる i は A_i のビットが A_k のビットの部分集合
# つまり、A_i & (~A_k) == 0

# なので、A_k の補集合のビットが立っているところに
# A_i のビットが立っていないことが条件

# つまり、A_i は A_k の部分集合

# 部分集合積を求めるには、subset方向に積を伝播させる必要がある。

# したがって、freq_prod[mask] は A_i == mask の積
# これを subset方向に積を伝播させる

# subset方向のSOS DPは、ビットを0にする方向に伝播

# なので、freq_prod を初期化し直して subset方向に積を伝播させる

freq_prod = [1]*(1<<MAX_BIT)
for a in A:
    freq_prod[a] = (freq_prod[a]*a) % MOD

for bit in range(MAX_BIT):
    for mask in range(1<<MAX_BIT):
        if (mask & (1 << bit)):
            freq_prod[mask] = (freq_prod[mask] * freq_prod[mask ^ (1 << bit)]) % MOD

# freq_prod[mask] は mask の部分集合の積

# これで、kに対して答えは freq_prod[A_k]

for a in A:
    print(freq_prod[a])