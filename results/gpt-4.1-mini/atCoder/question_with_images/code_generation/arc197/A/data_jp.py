import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    S = input().strip()

    # Sの長さは H+W-2
    # Sに含まれるDの個数はH-1以下、Rの個数はW-1以下

    # まず、Sの中でDが確定している最初の位置を求める（左から）
    # それより左はDで確定していない（?かR）
    first_D = H + W  # 存在しなければ大きい値
    for i, c in enumerate(S):
        if c == 'D':
            first_D = i
            break

    # Sの中でRが確定している最後の位置を求める（右から）
    last_R = -1
    for i in range(len(S)-1, -1, -1):
        if S[i] == 'R':
            last_R = i
            break

    # 最大で黒く塗れるマスは以下の通り
    # (first_D + 1) * (W - last_R - 1) + (H - first_D - 1) * (last_R + 1)
    # ただし、first_Dが存在しない場合は first_D = H+W-2
    # last_Rが存在しない場合は last_R = -1

    # これは、最初にDが確定している位置までの縦方向の範囲と、
    # 最後にRが確定している位置からの横方向の範囲を掛け合わせている。

    # ただし、問題の解説や考察からこの式が導かれている。

    # 具体的には、
    # - first_D + 1 はDが確定している最初の位置までの長さ（0-indexなので+1）
    # - W - last_R - 1 は最後にRが確定している位置から右端までの幅
    # - (H - first_D - 1) はDが確定している位置以降の縦の長さ
    # - last_R + 1 はRが確定している最後の位置までの幅

    # これらの積の和が最大の黒マス数となる。

    ans = (first_D + 1) * (W - last_R - 1) + (H - first_D - 1) * (last_R + 1)
    print(ans)