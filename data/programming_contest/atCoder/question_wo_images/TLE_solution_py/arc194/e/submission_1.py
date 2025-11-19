import sys
input = lambda :sys.stdin.readline()[:-1]
ni = lambda :int(input())
na = lambda :list(map(int,input().split()))
yes = lambda :print("yes");Yes = lambda :print("Yes");YES = lambda : print("YES")
no = lambda :print("no");No = lambda :print("No");NO = lambda : print("NO")

def naive(s, x, y):
    while True:
        for i in range(len(s)-x-y+1):
            if s[i:i+x] == [0] * x and s[i+x:i+x+y] == [1] * y:
                s[i:i+x+y] = [1] * y + [0] * x
                break
        else:
            break
    return s

n, x, y = na()
s = [int(i) for i in input()]
t = [int(i) for i in input()]

if naive(s, x, y) == naive(t, x, y):
    Yes()
else:
    No()