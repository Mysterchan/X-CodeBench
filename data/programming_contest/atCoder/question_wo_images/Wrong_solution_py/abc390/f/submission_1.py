n = int(input())
A = list(map(int, input().split()))

I = [[-1] for _ in range(3*(10**5)+2)]

for i in range(n):
    I[A[i]].append(i)

def calc(i):
    res = 0
    ni = len(I[i])
    for j in range(1, ni):
        m = I[i][j] - I[i][j-1] - 1
        res += (m+1)*m//2
    m = n - I[i][-1] - 1
    res += (m+1)*m//2
    return res

def calc2(i):
    res = 0
    X = I[i] + I[i+1]
    X = X[1:]
    X.sort()

    nx = len(X)
    for j in range(1, nx):
        m = X[j] - X[j-1] - 1
        res += m*(m+1)//2
    m = n - X[-1] - 1
    res += m*(m+1)//2
    return res

ans = 0
for i in range(1, 10**5+1):
    ans += n*(n+1)//2
    ans -= calc2(i)
    ans -= n*(n+1)//2
    ans += calc(i+1)

print(ans)