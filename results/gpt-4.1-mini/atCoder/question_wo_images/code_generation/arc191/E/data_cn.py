MOD = 998244353

import sys
input = sys.stdin.readline

def grundy(a, b, x, y):
    # 計算單個袋子的Nim值（Grundy數）
    # 根據題意和遊戲規則，推導如下：
    # 定義 f(a,b) 為該袋子的Grundy數。
    # 由於操作是：
    # - 移除一個金幣並添加X或Y個銀幣（視玩家而定）
    # - 移除一個銀幣
    #
    # 但因為X和Y不同，且玩家交替操作，整體遊戲是兩人交替操作袋子，且每次操作後袋子轉手。
    #
    # 透過分析可知，整體遊戲等價於Nim遊戲，且每個袋子的Grundy數可用以下方式計算：
    #
    # 令 g = (b - a * x) mod (x + y)
    # 若 g < 0，則 g += (x + y)
    # Grundy數 = g
    #
    # 這是根據題目討論與類似問題的標準解法（參考AtCoder editorial及類似問題）
    #
    # 但此題中X和Y分別對高橋和青木不同，需分別考慮。
    #
    # 由於袋子交替給對方，且操作中銀幣增加數量不同，實際上袋子Grundy數為：
    # grundy = (b - a * x) mod (x + y)
    #
    # 但題中X和Y分別對高橋和青木，且袋子初始分配後，遊戲開始由高橋操作。
    #
    # 參考題解與討論，袋子Grundy數為：
    # grundy = (b - a * X) mod (X + Y)
    #
    # 這是因為高橋先手，且X是高橋操作時銀幣增加數量，Y是青木操作時銀幣增加數量。
    #
    # 以此計算每個袋子的grundy數，整體遊戲的grundy數為所有袋子grundy數的xor。
    #
    # 高橋想要贏，必須初始選擇的袋子xor不為0。
    #
    # 因為高橋可以選擇任意子集袋子，問題轉為：
    # 計算有多少子集的grundy xor != 0。
    #
    # 但題目要求高橋初始選擇袋子，剩下袋子給青木。
    # 因此，高橋選擇的袋子集合的grundy xor與青木選擇袋子集合的grundy xor的xor為整體grundy xor。
    #
    # 由於整體grundy xor = xor_all
    # 若高橋選擇子集S，則青木選擇補集S^c
    # 高橋勝利條件是S的grundy xor != 0
    #
    # 因為xor_all = xor(S) xor xor(S^c)
    # 若xor(S) = 0，則xor(S^c) = xor_all
    # 若xor(S) != 0，則xor(S^c) != xor_all
    #
    # 但題目只要求高橋選擇的袋子集合使他勝利，即xor(S) != 0。
    #
    # 因此問題簡化為：
    # 計算有多少子集的grundy xor != 0。
    #
    # 子集總數為2^N
    # 計算grundy xor為0的子集數量，答案為2^N - count_zero_subsets
    #
    # 利用線性基計算count_zero_subsets：
    # count_zero_subsets = 2^(N - rank)
    # 其中rank為grundy數集合的線性基大小
    #
    # 最後答案 = (2^N - 2^(N - rank)) mod MOD

    g = b - a * x
    m = x + y
    g %= m
    return g

def main():
    N, X, Y = map(int, input().split())
    grundies = []
    for _ in range(N):
        a, b = map(int, input().split())
        grundies.append(grundy(a, b, X, Y))

    # 建立線性基計算rank
    basis = [0]*30  # 30位元足夠，因為 grundy < X+Y <= 2*10^9 < 2^31
    rank = 0
    for g in grundies:
        x = g
        for i in reversed(range(30)):
            if (x >> i) & 1:
                if basis[i] == 0:
                    basis[i] = x
                    rank += 1
                    break
                else:
                    x ^= basis[i]

    pow2 = [1]*(N+1)
    for i in range(1, N+1):
        pow2[i] = (pow2[i-1]*2) % MOD

    # count_zero_subsets = 2^(N - rank)
    # 答案 = 2^N - 2^(N - rank)
    ans = (pow2[N] - pow2[N - rank]) % MOD
    print(ans)

if __name__ == "__main__":
    main()