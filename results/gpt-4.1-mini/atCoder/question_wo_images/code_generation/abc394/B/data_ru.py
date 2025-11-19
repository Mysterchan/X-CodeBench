n = int(input())
strings = [input() for _ in range(n)]
strings.sort(key=len)
print(''.join(strings))