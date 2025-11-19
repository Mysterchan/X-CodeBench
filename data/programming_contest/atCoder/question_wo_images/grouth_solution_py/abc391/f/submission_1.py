def f(x):
    cnt = 0
    for i in range(N):
        if g(i, 0, 0) < x:
            break
        for j in range(N):
            if g(i, j, 0) < x:
                break
            for k in range(N):
                if g(i, j, k) < x:
                    break
                cnt += 1
                if cnt == K:
                    return True
    return False

def g(i, j, k):
    return A[i] * B[j] + B[j] * C[k] + C[k] * A[i]

N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

ok = 0
ng = 3 * 10 ** 18 + 1
while ng - ok > 1:
    mid = (ok + ng) // 2
    if f(mid):
        ok = mid
    else:
        ng = mid
print(ok)