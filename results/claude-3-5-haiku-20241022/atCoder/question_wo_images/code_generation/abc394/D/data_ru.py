S = input().strip()

stack = []
pairs = {'(': ')', '[': ']', '<': '>'}

for char in S:
    if char in pairs:
        stack.append(char)
    else:
        if stack and pairs.get(stack[-1]) == char:
            stack.pop()
        else:
            stack.append(char)

if len(stack) == 0:
    print("Yes")
else:
    print("No")