def check(a, mex):
    n = len(a)
    da = [0]*(n+1)
    d = 0
    for i in range(n):
        d -= da[i]
        if d < mex + i - n:
            return False
        da[min(i+a[i]+d+1 - max(0, mex + i - n), n)] += 1
        d += 1
    return True

t_ = int(input())
for _ in range(t_):
    n = int(input())
    a = list(map(int, input().split()))
    l, r = 1, len(a) + 1
    while r-l > 1:
        mid = (r+l)//2
        if check(a, mid):
            l = mid
        else:
            r = mid
    print(l)
