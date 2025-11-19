n = int(input())
s = [input() for _ in range(n)]
s.sort(key=len)
print(''.join(s))