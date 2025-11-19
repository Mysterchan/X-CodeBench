import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    # 空の花瓶の位置をリストアップ
    empty = [i for i, c in enumerate(s) if c == '0']

    # 空の花瓶が0個または1個なら必ず配置可能
    if len(empty) <= 1:
        print("YES")
        continue

    # 空の花瓶が2個以上の場合、隣接している空の花瓶があるかをチェック
    # 隣接している空の花瓶があればYES、なければNO
    possible = False
    for i in range(len(empty) - 1):
        if empty[i+1] - empty[i] == 1:
            possible = True
            break

    print("YES" if possible else "NO")