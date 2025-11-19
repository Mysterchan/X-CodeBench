import sys
import math
from collections import *
input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

for _ in range(sint()):
    n,m=mint()
    s=input()
    ans=0
    count_D=s.count("D")
    rem_D=n-1-count_D
    count_R=s.count("R")
    rem_R=m-1-count_R
    count_B=s.count("?")
    if rem_D>0 and rem_R>0 and count_B!=len(s):
        ans=len(s)+1+ 2*(count_B)
    elif count_B==len(s):
        ans=n*m
    else:
        ans=len(s)+1
    print(ans)