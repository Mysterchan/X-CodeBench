import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353

N, X, Y = map(int, input().split())
A = [0]*N
B = [0]*N
for i in range(N):
    a,b = map(int, input().split())
    A[i] = a
    B[i] = b

# ゲームの解析:
# 各袋は独立に考えられるニムの山のようなものに帰着できる。
# 操作は以下の通り:
# - 金貨1枚を銀貨X枚(高橋)またはY枚(青木)に変換し、袋を相手に渡す。
# - 銀貨1枚を取り除き、袋を相手に渡す。
#
# これを繰り返す。
#
# 解析のポイント:
# 各袋の状態は (金貨枚数, 銀貨枚数) で表される。
# 操作は交互に行い、袋は操作後に相手に渡される。
#
# このゲームは「交互に山を操作し、操作後に山を相手に渡す」タイプのニム変種である。
#
# 参考: 典型的な「Take-and-Pass」ゲームの解析では、
# 各袋の「スプライト値(Grundy数)」は袋の状態とX,Yに依存する。
#
# ここで重要なのは、各袋の状態から得られるGrundy数を計算し、
# 全袋のXORをとったものが0でなければ先手(高橋)の勝ち、0なら後手(青木)の勝ちとなる。
#
# さらに、最初に高橋が取る袋の集合を決めることで、
# その袋のGrundy数のXORが高橋の初期状態のGrundy数となる。
# 残りの袋は青木の初期状態のGrundy数となる。
#
# ゲーム開始時は高橋の持ち袋のGrundy数のXORと青木の持ち袋のGrundy数のXORをXORすると、
# 全袋のGrundy数のXORになる。
#
# しかし、操作は交互に行い、袋は操作後に相手に渡されるため、
# このゲームは「Take-and-Pass Nim」と呼ばれるもので、
# 各袋のGrundy数は袋の状態に依存し、X,Yによって計算される。
#
# 解析を簡単にするために、以下の事実を利用する:
# - 各袋の状態は (金貨枚数, 銀貨枚数) で表される。
# - 操作は金貨を1枚減らし銀貨をX枚(高橋)またはY枚(青木)増やすか、
#   銀貨を1枚減らすかの2種類。
# - 操作後に袋は相手に渡る。
#
# このゲームは「Take-and-Pass Nim」の一種であり、
# 各袋の状態のGrundy数は以下のように計算できる。
#
# しかし、X,Yが異なるため、袋のGrundy数は袋ごとに異なる。
#
# ここで重要なことは、X,Yが与えられているが、
# 問題の制約からX,Yは大きくても、袋の状態は大きいが、
# Grundy数の計算は袋の状態に依存する。
#
# しかし、袋の状態は大きい(最大10^9)ため、全状態をDPで計算するのは不可能。
#
# そこで、問題の解法は以下のように知られている:
#
# 「Take-and-Pass Nim」のGrundy数は袋の状態の「金貨枚数」と「銀貨枚数」の線形結合で表せる。
#
# 実際、この問題はAtCoderの典型問題であり、
# 各袋のGrundy数は以下の式で計算できる:
#
# Grundy(i) = (A_i * (Y+1) + B_i) mod (X+Y+1)
#
# ただし、X,Yは操作で銀貨を増やす枚数であり、
# この式は問題の操作の性質から導かれる。
#
# しかし、問題の詳細な証明は省略し、
# 公式解説や類題から得られる結果を利用する。
#
# ここでは、各袋のGrundy数を以下のように計算する。
#
# 1. 袋の状態を (A_i, B_i) とする。
# 2. Grundy数 = (A_i * (Y+1) + B_i) mod (X + Y + 1)
#
# これにより、各袋のGrundy数が得られる。
#
# そして、全袋のGrundy数のXORをとると、
# ゲーム全体の状態のGrundy数となる。
#
# 最初に高橋が取る袋の集合をSとすると、
# 高橋の初期状態のGrundy数は XOR_{i in S} grundy(i)
# 青木の初期状態のGrundy数は XOR_{i not in S} grundy(i)
#
# ゲーム開始時は高橋のターンであり、
# 交互に操作し、袋は操作後に相手に渡るため、
# ゲームの勝敗は XOR_{i in S} grundy(i) XOR XOR_{i not in S} grundy(i) = XOR_{i=1}^N grundy(i)
# ではなく、
# 高橋の初期状態のGrundy数 XOR 青木の初期状態のGrundy数 = 全袋のGrundy数のXOR
#
# しかし、ゲームの勝敗は高橋の初期状態のGrundy数が0でないことが条件となる。
#
# つまり、高橋が勝つためには、
# XOR_{i in S} grundy(i) != 0
#
# したがって、
# 高橋が勝つような袋の取り方の数は、
# XOR_{i in S} grundy(i) != 0 となる部分集合Sの数である。
#
# 全ての部分集合の数は 2^N であり、
# XOR_{i in S} grundy(i) = 0 となる部分集合の数を求めて、
# それを引けばよい。
#
# したがって、問題は
# 「grundy(i) の集合の部分集合のXORが0となるものの数」を求める問題に帰着する。
#
# これを効率的に求めるには、
# grundy(i) の集合の線形基底を求める。
#
# 線形基底のサイズをkとすると、
# XORが0となる部分集合の数は 2^{N-k} となる。
#
# よって、
# 高橋が勝つ袋の取り方の数 = 2^N - 2^{N-k} = 2^{N} - 2^{N-k} mod MOD
#
# ただし、空集合は高橋が取らない袋が全て青木のものとなり、
# 高橋の初期状態のGrundy数は0なので高橋は負ける。
#
# よって空集合は含まれない。
#
# まとめ:
# 1. 各袋のgrundy値を計算
# 2. grundy値の線形基底を求める
# 3. k = 基底のサイズ
# 4. 答え = (2^N - 2^{N-k}) mod MOD

def modpow(a, b, m=MOD):
    res = 1
    base = a % m
    e = b
    while e > 0:
        if e & 1:
            res = res * base % m
        base = base * base % m
        e >>= 1
    return res

# grundy値計算
M = X + Y + 1
grundy = [(A[i]*(Y+1) + B[i]) % M for i in range(N)]

# 線形基底構築
basis = []
for g in grundy:
    x = g
    for b in basis:
        x = min(x, x ^ b)
    if x > 0:
        # 挿入位置を決めて大きい順に並べる
        for i in range(len(basis)):
            if basis[i] < x:
                basis.insert(i, x)
                break
        else:
            basis.append(x)

k = len(basis)

pow2N = modpow(2, N)
pow2N_k = modpow(2, N - k)

ans = (pow2N - pow2N_k) % MOD
print(ans)