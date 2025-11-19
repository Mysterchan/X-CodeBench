s = input()
stack = []

for c in s:
    if c == 'A' and stack and stack[-1] == 'W':
        stack.pop()
        stack.append('A')
        stack.append('C')
    else:
        stack.append(c)

print(''.join(stack))