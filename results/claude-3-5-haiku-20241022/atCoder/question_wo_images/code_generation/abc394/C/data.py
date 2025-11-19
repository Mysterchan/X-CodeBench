s = input()
result = []

for char in s:
    result.append(char)
    # Check if we just formed "WA" at the end
    while len(result) >= 2 and result[-2] == 'W' and result[-1] == 'A':
        # Remove "WA" and add "AC"
        result.pop()
        result.pop()
        result.append('A')
        result.append('C')

print(''.join(result))