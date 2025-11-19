import sys
input = sys.stdin.readline

def min_steps(x, y):
    # 若 x > y，交換，確保 x <= y，方便討論
    if x > y:
        x, y = y, x

    # n步中，奇數步沿x軸，偶數步沿y軸
    # 設 n 為步數，分兩種情況：
    # 1. n為偶數，則x軸步數 = n/2，y軸步數 = n/2
    # 2. n為奇數，則x軸步數 = (n+1)/2，y軸步數 = (n-1)/2

    # 對於步數k，步長嚴格遞增，且每步長為正整數
    # x軸步數為 a，y軸步數為 b
    # x軸步長和至少為 sum(1..a) = a(a+1)/2
    # y軸步長和至少為 sum(1..b) = b(b+1)/2
    # 因為步長嚴格遞增，且交替使用，x軸和y軸的步長集合互不重疊
    # 所以x軸和y軸的步長分別是兩個嚴格遞增的正整數序列

    # 我們要找最小的 n，使得：
    # x <= a(a+1)/2 且 y <= b(b+1)/2
    # 且 a,b 根據 n 的奇偶決定

    # 因為 x,y 最大 1e9，n 不會太大，二分搜尋 n

    left, right = 1, 2*10**5  # upper bound足夠大

    res = -1
    while left <= right:
        mid = (left + right) // 2
        if mid % 2 == 0:
            a = mid // 2
            b = mid // 2
        else:
            a = (mid + 1) // 2
            b = (mid - 1) // 2

        sum_x = a * (a + 1) // 2
        sum_y = b * (b + 1) // 2

        if sum_x >= x and sum_y >= y:
            res = mid
            right = mid - 1
        else:
            left = mid + 1

    return res

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print(min_steps(x, y))