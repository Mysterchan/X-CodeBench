t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    # 対称性を満たすためには、赤区間と青区間の位置を反転させたときに青区間が赤区間を覆う形になる必要がある。
    # つまり、x と y は以下の関係を満たす必要がある:
    # y = n - (x + a - 1) - b + 2
    # y は 1 <= y <= n - b + 1 の範囲内でなければならない。
    # x は 1 <= x <= n - a + 1 の範囲内でなければならない。
    # この範囲内に y が存在する x があれば "YES"、なければ "NO"。

    # y = n - (x + a - 1) - b + 2 = n - x - a + 1 - b + 2 = n - x - a - b + 3
    # y の範囲: 1 <= y <= n - b + 1
    # x の範囲: 1 <= x <= n - a + 1

    # y >= 1 なら n - x - a - b + 3 >= 1 => x <= n - a - b + 2
    # y <= n - b + 1 なら n - x - a - b + 3 <= n - b + 1 => -x - a + 3 <= 1 => -x <= a - 2 => x >= 2 - a

    # x は 1 <= x <= n - a + 1 なので、x の範囲は max(1, 2 - a) <= x <= min(n - a + 1, n - a - b + 2)
    # これらの範囲が交差していれば "YES"

    left = max(1, 2 - a)
    right = min(n - a + 1, n - a - b + 2)

    if left <= right:
        print("YES")
    else:
        print("NO")