n = int(input())
strings = []
for _ in range(n):
    strings.append(input())

strings.sort(key=len)
print(''.join(strings))