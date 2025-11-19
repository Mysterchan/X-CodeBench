import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

left = 0
right = N // 2 + 1

while right - left > 1:
    mid = (left + right) // 2
    # Check if we can form mid pairs
    can = True
    for i in range(mid):
        if A[i] * 2 > A[N - mid + i]:
            can = False
            break
    if can:
        left = mid
    else:
        right = mid

print(left)