import math
mod = 1000000007
for _ in range(int(input())):
    a,b,k = map(int,input().split())
    n = ((a-1)*k+1)%mod
    t=math.comb(n,a)
    m = ((b-1)*k*t)%mod+1
    print(n,m)
