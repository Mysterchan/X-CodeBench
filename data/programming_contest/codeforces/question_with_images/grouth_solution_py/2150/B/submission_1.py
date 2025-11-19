from math import comb

MOD = 998244353

def D():
    row = (N+1)//2
    if sum(A[row:]) != 0 or sum(A) != N:
        return 0
    else:
        if N%2:
            n = 1
        else:
            n = 2

        ans = 1
        while row:
            row -= 1
            ans = (ans * comb(n, A[row]))%MOD
            n += 2 - A[row]
            if n < 2:
                return 0

        return ans%MOD

for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))

    print(D())
