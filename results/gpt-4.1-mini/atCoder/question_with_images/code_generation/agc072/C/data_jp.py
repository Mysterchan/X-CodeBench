N, K = map(int, input().split())

# 各エクササイズでの経路は、(N-1)回のDと(R-1)回のRの順列の一つである。
# ルールにより、K回目の経路は辞書順でK番目のパスに対応する。
# ここで、Dを「下方向」、Rを「右方向」とする。
# 
# 理由：
# - 各マスの訪問回数は、これまでの経路の通過回数の累積で決まる。
# - 移動可能な2方向の訪問回数が同じならDを選ぶ。
# - これを繰り返すと、K回目の経路は「これまでの経路の訪問回数の累積分布に基づく辞書順K番目のパス」となる。
#
# よって、(N-1)個のDと(N-1)個のRからなる文字列の辞書順K番目を求めればよい。
#
# 辞書順でのパスの数はcomb(2N-2, N-1)であり、Kは最大10^18なので、
# 動的計画法で組み合わせ数を計算しながらK番目のパスを復元する。

from math import comb

down = N - 1
right = N - 1
path = []

while down > 0 and right > 0:
    # 下方向に進むパスの数
    count = comb(down + right - 1, down - 1)
    if K <= count:
        path.append('D')
        down -= 1
    else:
        path.append('R')
        K -= count
        right -= 1

# 残りはすべてDまたはR
path.extend(['D'] * down)
path.extend(['R'] * right)

print(''.join(path))