import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, rK, cK, rD, cD = map(int, input().split())

    # クルグの移動距離（マンハッタン距離）
    distK = abs(rK - rD) + abs(cK - cD)
    # ドランの移動距離（チェビシェフ距離）
    distD = max(abs(rK - rD), abs(cK - cD))

    # クルグの生存時間は、ドランが追いつくまでのターン数
    # クルグが先に動くため、ドランが追いつくまでのターン数は distK - distD + 1
    # ただし、distD > distK の場合はドランがすぐ捕まえられるので生存時間は1
    # また、無限に逃げられる場合は -1 を出力（この問題の条件では無限逃げられない）

    # 解析より、クルグが無限に逃げられるケースは存在しないため -1 は出力しない

    # 生存時間は distK - distD + 1 が正ならそれ、負なら1
    ans = distK - distD + 1
    if ans < 1:
        ans = 1

    print(ans)