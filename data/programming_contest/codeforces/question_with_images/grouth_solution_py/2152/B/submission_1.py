g = int(input())
for _ in range(g):
    [n,rk,ck,rd,cd] = map(int,input().split())
    print(max((n-rd)*(rk>rd)+rd*(rk<rd),(n-cd)*(ck>cd)+cd*(ck<cd)))
