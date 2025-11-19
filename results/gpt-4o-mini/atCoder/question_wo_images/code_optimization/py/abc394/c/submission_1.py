s = input()
result = []
i = 0

while i < len(s):
    if i < len(s) - 1 and s[i] == 'W' and s[i + 1] == 'A':
        result.append('A')
        result.append('C')
        i += 2  # Skip the 'W' and 'A' we just replaced
    else:
        result.append(s[i])
        i += 1

print(''.join(result))