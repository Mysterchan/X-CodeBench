import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

left, right = 0, N // 2
res = 0

while left <= right:
    mid = (left + right) // 2
    # 嘗試配對 mid 組
    # 小的麻糬從 A[0:mid]，大的麻糬從 A[N-mid:N]
    # 檢查是否所有小的麻糬都能放在對應大的麻糬上
    ok = True
    for i in range(mid):
        if A[i] * 2 > A[N - mid + i]:
            ok = False
            break
    if ok:
        res = mid
        left = mid + 1
    else:
        right = mid - 1

print(res)