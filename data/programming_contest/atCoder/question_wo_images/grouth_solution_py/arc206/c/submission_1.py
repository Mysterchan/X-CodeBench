from sys import stdin
input = stdin.readline
inp = lambda : list(map(int,input().split()))

mod = 998244353
def answer():

    dp = [1 , 0]
    for i in range(n):
        ndp = [0 , 0]
        if(a[i] == -1):
            ndp[1] += dp[1]
            ndp[1] %= mod

            ndp[1] += (n - 1)*dp[0]
            ndp[1] %= mod
            ndp[0] += dp[0]
            ndp[0] %= mod
        else:
            if(a[i] == i):
                ndp[1] += dp[1]
                ndp[1] %= mod
            if(a[i] != (i + 2)):
                ndp[1] += dp[0]
                ndp[1] %= mod
            else:
                ndp[0] += dp[0]
                ndp[0] %= mod

        dp = ndp


    ans = sum(dp) % mod
    return ans
            
 
for T in range(1):

    n = int(input())
    a = inp()

    print(answer())
