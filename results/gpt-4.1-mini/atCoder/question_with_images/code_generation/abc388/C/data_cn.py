import sys
import bisect

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

res = 0
for i in range(N):
    # 找到最大的 j，使得 A[j] <= 2 * A[i]
    # j 必須 > i，因為要放在上面的是較小的麻糬
    limit = 2 * A[i]
    j = bisect.bisect_right(A, limit, i + 1, N)
    res += j - (i + 1)

print(res)