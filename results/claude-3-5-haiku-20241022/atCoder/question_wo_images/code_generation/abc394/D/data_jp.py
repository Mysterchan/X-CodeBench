S = input().strip()

stack = []
pairs = {'(': ')', '[': ']', '<': '>'}

for char in S:
    if char in pairs:
        stack.append(char)
    else:
        if not stack or pairs[stack[-1]] != char:
            print("No")
            exit()
        stack.pop()

if stack:
    print("No")
else:
    print("Yes")