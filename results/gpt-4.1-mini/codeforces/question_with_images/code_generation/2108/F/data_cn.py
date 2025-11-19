import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    mex = 0
    for x in a:
        if x > mex:
            mex += 1
    print(mex)