import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

stack = []
total = 0

for x in A:
    if x >= 0:
        stack.append(x)
        total += x
    else:
        if stack:
            top = stack[-1]
            if top + x >= 0:
                stack[-1] = top + x
                total += x
            else:
                total -= top
                stack.pop()
        else:
            # S is empty, must add x
            stack.append(x)
            total += x

print(total)