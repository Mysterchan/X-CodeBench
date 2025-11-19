import sys
input = lambda :sys.stdin.readline()[:-1]
ni = lambda :int(input())
na = lambda :list(map(int,input().split()))
yes = lambda :print("yes");Yes = lambda :print("Yes");YES = lambda : print("YES")
no = lambda :print("no");No = lambda :print("No");NO = lambda : print("NO")

n, x, y = na()
s = list(map(int, input()))
t = list(map(int, input()))

def can_transform(s, t, x, y):
    diff = [s[i] ^ t[i] for i in range(n)]  # Create a difference array
    one_segments = 0
    zero_segments = 0

    for i in range(n):
        if diff[i] == 1:
            if zero_segments > 0:
                if zero_segments >= x:
                    one_segments += 1
                zero_segments = 0
            zero_segments += 1
        else:
            if one_segments > 0:
                if one_segments >= y:
                    zero_segments += 1
                one_segments = 0
                
    # Handle remaining segments at the end
    if zero_segments > 0 and zero_segments >= x:
        one_segments += 1
    if one_segments > 0 and one_segments >= y:
        zero_segments += 1

    return one_segments > 0 and zero_segments > 0

if can_transform(s, t, x, y):
    Yes()
else:
    No()