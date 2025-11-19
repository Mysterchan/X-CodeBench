import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

stack = []
total = 0

for x in A:
    if not stack:
        # S is empty, must append
        stack.append(x)
        total += x
    else:
        # If current element is negative and removing last element is beneficial
        # i.e. if last element in stack < current element, pop last element and append current
        # Because removing last element costs one operation, but we can only do one operation per step
        # So we must choose either append or pop, not both.
        # So we consider:
        # Option 1: append x -> total + x
        # Option 2: pop last element -> total - last element
        # Choose max
        if x < 0 and stack[-1] < x:
            # pop last element
            total -= stack.pop()
            # do not append x this step (since only one operation per step)
        else:
            # append x
            stack.append(x)
            total += x

print(total)