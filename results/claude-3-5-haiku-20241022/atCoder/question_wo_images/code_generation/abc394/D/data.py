S = input().strip()

stack = []
matches = {')': '(', ']': '[', '>': '<'}

for char in S:
    if char in '([<':
        stack.append(char)
    else:  # char in ')]>'
        if not stack or stack[-1] != matches[char]:
            print("No")
            exit()
        stack.pop()

if len(stack) == 0:
    print("Yes")
else:
    print("No")