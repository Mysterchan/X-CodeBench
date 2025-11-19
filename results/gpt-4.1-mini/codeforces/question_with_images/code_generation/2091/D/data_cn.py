import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    # 最長長椅的最小可能長度即為將 k 個桌子均勻分配到 n 行後，
    # 每行最多的桌子數量的最小值，即 ceil(k / n)
    # 但不能超過每行的最大座位數 m
    ans = (k + n - 1) // n
    if ans > m:
        ans = m
    print(ans)