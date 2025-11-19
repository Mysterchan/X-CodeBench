import os,sys,random,threading

from random import randint,choice,shuffle

from copy import deepcopy
from io import BytesIO,IOBase
from types import GeneratorType
from functools import lru_cache,reduce

from bisect import bisect_left,bisect_right

from collections import Counter,defaultdict,deque
from itertools import accumulate,combinations,permutations

from heapq import  heapify,heappop,heappush

from typing import Generic,Iterable,Iterator,TypeVar,Union,List
from string import ascii_lowercase,ascii_uppercase,digits

from math import ceil,floor,sqrt,pi,factorial,gcd,log,log10,log2,inf

from decimal import Decimal,getcontext

from sys import stdin, stdout, setrecursionlimit
input = lambda: sys.stdin.readline().rstrip("\r\n")
MI = lambda :map(int,input().split())
li = lambda :list(MI())
ii = lambda :int(input())
mod = int(1e9 + 7)
inf = 1<<60
py = lambda :print("YES")
pn = lambda :print("NO")
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),(-1, 1)]

mod=998244353

b=10

n=ii()

arr=li()

f=[[1]*(1<<b) for _ in range(1<<b)]

full=(1<<b)-1

flag=0

for a in arr:
    if a==0:
        flag=1
    if flag==1:
        print(0)
        continue

    x=a>>b
    y=a&full

    mask=y
    while mask<full+1:
        f[x][mask]*=a
        f[x][mask]%=mod
        mask=(mask+1)|y

    res=f[0][y]
    mask=x
    while mask:
        res*=f[mask][y]
        res%=mod
        mask=(mask-1)&x

    print(res)