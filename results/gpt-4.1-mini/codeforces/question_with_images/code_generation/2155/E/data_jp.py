import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    tokens = [tuple(map(int, input().split())) for __ in range(k)]

    # ゲームのルールから考察すると、
    # 各トークンは列b_iに存在し、b_i > 1ならば、
    # そのトークンは1つ左の列(b_i-1)に移動可能な経路を作れる。
    # つまり、列b_i > 1のトークンは必ず動かせる可能性がある。
    #
    # しかし、b_i = 1のトークンは動かせない（左に列がないため）。
    #
    # したがって、ゲームは「列番号が1より大きいトークンの数」によって決まる。
    #
    # 各トークンの「(b_i - 1)」のXORをとると、ニムの山の石の数のように扱える。
    #
    # つまり、各トークンの (y_i - 1) のXORを計算し、
    # それが0なら後手(=Yuyu)の勝ち、0でなければ先手(=Mimo)の勝ち。
    #
    # これは Nim ゲームの基本的な考え方に基づく。

    xor_sum = 0
    for _, y in tokens:
        xor_sum ^= (y - 1)

    if xor_sum != 0:
        print("Mimo")
    else:
        print("Yuyu")