import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    # 二分探索で最長ベンチ長の最小値を求める
    left, right = 1, k
    while left < right:
        mid = (left + right) // 2
        # 1行あたり最大midの長さのベンチがいくつ作れるか
        benches_per_row = m // mid
        # 全行で作れるベンチ数
        total_benches = benches_per_row * n
        # 1ベンチあたりmid人座れるので、mid * total_benches >= k ならmidで配置可能
        if mid * total_benches >= k:
            right = mid
        else:
            left = mid + 1
    print(left)