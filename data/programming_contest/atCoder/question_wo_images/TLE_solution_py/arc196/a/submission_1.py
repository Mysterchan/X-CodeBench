def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
def cycle_detection(f, x0):

    power = lam = 1
    first = x0
    second = f(x0)
    while first != second:
        if power == lam:
            first = second
            power *= 2
            lam = 0
        second = f(second)
        lam += 1
    first = second = x0
    for i in range(lam):
        second = f(second)
    mu = 0
    while first != second:
        first = f(first)
        second = f(second)
        mu += 1
    return mu, lam
def cycle_detection_lists(f, x0):
    mu, lam = cycle_detection(f, x0)
    before_cycle = [0] * mu
    if mu > 0:
        before_cycle[0] = x0
        for i in range(mu - 1):
            before_cycle[i + 1] = f(before_cycle[i])

    cycle = [0] * lam
    cycle[0] = before_cycle[-1] if mu > 0 else x0
    for i in range(lam - 1):
        cycle[i + 1] = f(cycle[i])
    return before_cycle, cycle

import bisect,collections,copy,heapq,itertools,math,string,sys,queue,time,random
from decimal import Decimal
def I(): return input()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return list(map(int,input().split()))
def LIIS(): return list(map(int,input().split()))
def comb(n, r):return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

INF=float("inf")
MOD=998244353
MOD2=10**9+7
sys.setrecursionlimit(10**7)
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def bit_count(x):
    return bin(x).count("1")
def yesno(f):
    if f:print("Yes")
    else:print("No")

n=II()
def solve(li):
    li.sort()
    return sum(li[len(li)//2:]) - sum(li[:len(li)//2])

A=LIIS()
if n%2==0:
    ans=solve(A)
else:
    ans=0
    for i in range(0,n,2):
        ans=max(ans,solve(A[:i])+solve(A[i+1:]))
print(ans)