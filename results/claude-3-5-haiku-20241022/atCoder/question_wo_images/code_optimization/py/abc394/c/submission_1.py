s = input()
result = []

for char in s:
    result.append(char)
    while len(result) >= 2 and result[-2] == 'W' and result[-1] == 'A':
        result.pop()
        result.pop()
        result.append('A')
        result.append('C')

print(''.join(result))