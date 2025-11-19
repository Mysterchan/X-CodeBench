import sys
input = sys.stdin.readline
II = lambda : int(input())
MI = lambda : map(int, input().split())
LI = lambda : [int(a) for a in input().split()]
SI = lambda : input().rstrip()
LLI = lambda n : [[int(a) for a in input().split()] for _ in range(n)]
LSI = lambda n : [input().rstrip() for _ in range(n)]
MI_1 = lambda : map(lambda x:int(x)-1, input().split())
LI_1 = lambda : [int(a)-1 for a in input().split()]

def graph(n:int, m:int, dir:bool=False, index:int=-1) -> list[set[int]]:
    edge = [set() for i in range(n+1+index)]
    for _ in range(m):
        a,b = map(int, input().split())
        a += index
        b += index
        edge[a].add(b)
        if not dir:
            edge[b].add(a)
    return edge

def graph_w(n:int, m:int, dir:bool=False, index:int=-1) -> list[set[tuple]]:
    edge = [set() for i in range(n+1+index)]
    for _ in range(m):
        a,b,c = map(int, input().split())
        a += index
        b += index
        edge[a].add((b,c))
        if not dir:
            edge[b].add((a,c))
    return edge

mod = 998244353
inf = 1001001001001001001
ordalp = lambda s : ord(s)-65 if s.isupper() else ord(s)-97
ordallalp = lambda s : ord(s)-39 if s.isupper() else ord(s)-97
yes = lambda : print("Yes")
no = lambda : print("No")
yn = lambda flag : print("Yes" if flag else "No")
def acc(a:list[int]):
    sa = [0]*(len(a)+1)
    for i in range(len(a)):
        sa[i+1] = a[i] + sa[i]
    return sa

prinf = lambda ans : print(ans if ans < 1000001001001001001 else -1)
alplow = "abcdefghijklmnopqrstuvwxyz"
alpup = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpall = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
URDL = {'U':(-1,0), 'R':(0,1), 'D':(1,0), 'L':(0,-1)}
DIR_4 = [[-1,0],[0,1],[1,0],[0,-1]]
DIR_8 = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
DIR_BISHOP = [[-1,1],[1,1],[1,-1],[-1,-1]]
prime60 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
sys.set_int_max_str_digits(0)

n,p = MI()
edge = n*(n-1)//2

lim = 500
comb = [[0]*lim for i in range(lim)]
for i in range(lim):
    comb[i][0] = comb[i][i] = 1
    for j in range(1,i):
        comb[i][j] = (comb[i-1][j] + comb[i-1][j-1]) % p

mid = n//2+1
c = [[[0]*(edge+1) for j in range(mid)] for i in range(mid)]
for px in range(mid):
    c[px][0][0] = 1
    for dx in range(n//2):
        for pe in range(edge+1):
            for de in range(1, edge+1 - pe):
                c[px][dx+1][pe+de] += c[px][dx][pe] * comb[px][de] % p
                c[px][dx+1][pe+de] %= p

sc = [[[0]*(edge+1) for j in range(mid)] for i in range(mid)]
for px in range(mid):
    for dx in range(mid):
        for de in range(edge+1):
            res = 0
            for pe in range(dx, de+1):
                res += c[px][dx][pe] * comb[dx*(dx-1)//2][de-pe] % p
                res %= p
            sc[px][dx][de] = res

c1 = mid
c2 = mid*mid
c3 = mid*mid*mid
c4 = (edge+1)*mid*mid*mid

dp = [0]*(2*(edge+1)*mid*mid*mid)
dp[c2 + 1] = 1

for e in range(edge+1):
    for i in range(min(mid, e+2)):
        for j in range(min(mid, e-i+2)):
            for px in range(1,mid):
                if dp[c4 + e*c3 + i*c2 + j*c1 + px]:
                    q = dp[c4 + e*c3 + i*c2 + j*c1 + px] % p
                    for dx in range(1, min((n+1-i-j), mid-i)):
                        for de in range(dx, edge+1 - e):
                            dp[(e+de)*c3 + (i+dx)*c2 + j*c1 + dx] += comb[n-i-j][dx] * \
                                q % p * sc[px][dx][de] % p
                            dp[(e+de)*c3 + (i+dx)*c2 + j*c1 + dx] %= p
                if dp[e*c3 + i*c2 + j*c1 + px]:
                    q = dp[e*c3 + i*c2 + j*c1 + px] % p
                    for dx in range(1, min((n+1-i-j), mid-j)):
                        for de in range(dx, edge+1 - e):
                            dp[c4 + (e+de)*c3 + i*c2 + (j+dx)*c1 + dx] += comb[n-i-j][dx] * \
                                q % p * sc[px][dx][de] % p
                            dp[c4 + (e+de)*c3 + i*c2 + (j+dx)*c1 + dx] %= p
tans = []
for m in range(n-1,edge+1):
    ans = 0
    for px in range(mid):
        off = m*c3 + (mid-1)*c2 + (mid-1)*c1
        ans = (ans + dp[off + px] + dp[c4 + off + px]) % p
    tans.append(ans)

print(*tans)