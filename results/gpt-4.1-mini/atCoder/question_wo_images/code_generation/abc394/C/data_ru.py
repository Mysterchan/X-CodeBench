S = input()

stack = []
for c in S:
    stack.append(c)
    if len(stack) >= 2 and stack[-2] == 'W' and stack[-1] == 'A':
        stack[-2] = 'A'
        stack[-1] = 'C'

print(''.join(stack))