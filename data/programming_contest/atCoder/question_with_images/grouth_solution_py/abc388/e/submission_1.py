N = int(input())
A = list(map(int, input().split()))

left = -1
right = N // 2 + 1
while right - left > 1:
    mid = (right + left) // 2

    ok = True
    for i in range(mid):
        if A[i] * 2 <= A[N - mid + i]:
            continue
        else:
            ok = False
            break
    if ok:
        left = mid
    else:
        right = mid

print(left)