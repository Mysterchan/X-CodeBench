import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # まず、AとBの総和が一致しなければ不可能
    if sum(A) != sum(B):
        print("No")
        continue

    # 操作は、同じ和の区間を入れ替えることができる
    # つまり、AとBの1の位置の相対的な順序は変えられないが、
    # 0の位置は自由に入れ替えられる可能性がある。
    # しかし、0と1の数は変わらない。

    # ここで、AとBの1の位置の順序が同じかどうかを確認する。
    # 1の位置の順序が違う場合はNo。

    posA = [i for i, v in enumerate(A) if v == 1]
    posB = [i for i, v in enumerate(B) if v == 1]

    if posA == posB:
        print("Yes")
    else:
        print("No")