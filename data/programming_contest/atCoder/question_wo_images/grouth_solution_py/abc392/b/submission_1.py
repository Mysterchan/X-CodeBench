import sys
from collections import Counter, deque, defaultdict
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().rstrip()

def II(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def SI(): return input().split()
def SLI(): return list(input().split())
def FL(N): return [list(map(int,input().split())) for _ in range(N)]

def bisect_left(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x: lo = mid + 1
        else: hi = mid
    return lo

def bisect_right(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] <= x: lo = mid + 1
        else: hi = mid
    return lo

def main():
    N,M = MI()
    A = LI()
    ans = []
    for i in range(1,N+1):
        if i not in A:
            ans.append(i)
    ans.sort()
    if not ans:
        print(0)
    else:
        print(len(ans))
        print(*ans)

if __name__ == "__main__":
    main()