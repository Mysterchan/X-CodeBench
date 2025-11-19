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
sys.setrecursionlimit(10**6)

from collections import defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right
DD = defaultdict
BSL = bisect_left
BSR = bisect_right

from itertools import combinations,permutations,product
from random import randint
from functools import cache
from math import lcm

def naive(n):
    loop = lcm(*range(1, n + 1))

    now = [[0]*n for i in range(n)]
    one = two = None
    ptmp = None
    passs = []
    print(n, loop)
    pre = 0
    qint = []

    c = 5
    v = [0] * c
    for k in range(60):
        x,y = 0,0
        now[x][y] += 1
        tmp = [[0]*n for i in range(n)]
        pas = []
        qas = []
        sf = 0
        pf = 0
        for i in range(n - 1):
            if x == n - 1:
                y += 1
                nf = 1
            elif y == n - 1:
                x += 1
                nf = 0
            else:
                if now[x+1][y] <= now[x][y+1]:
                    x += 1
                    nf = 0
                else:
                    y += 1
                    nf = 1
            pas.append(str(nf))

            now[x][y] += 1
            tmp[x][y] += 1
        print(*now, sep= "\n")
        print()
        u = []
        for i in range(c):
            u.append(now[i][c-1-i])
        v = []
        for i in range(c):
            v.append(tmp[i][c-1-i])

        pas = "".join(pas)

        pint = int(pas[::-1], 2)

        pre ^= pint
        passs.append(pas)

    print(qint)

    return

def calc(n, k):
    c = [[0] * n for i in range(n)]
    c[0][0] = k
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i + j > n:
                break
            t = c[i-1][j-1]
            d = i + j
            t1 = i * (t//d) + min(i, t%d)
            c[i][j-1] += t1
            c[i-1][j] += t - t1

    return c

n, k = MI()

c1 = calc(n, k)
c2 = calc(n, k-1)

c = [[0] * (n + 1) for i in range(n + 1)]

for i in range(n):
    for j in range(n):
        c[i][j] = c1[i][j] - c2[i][j]

x, y = 0, 0
ans = ""
ans2 = ""
for i in range(n - 1):
    if c[x+1][y]:
        ans += "D"
        ans2 += "R"
        x += 1
    else:
        ans += "R"
        ans2 +="D"
        y += 1

print(ans + ans2[::-1])