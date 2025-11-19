n = int(input())
s = [input().strip() for _ in range(n)]
s.sort(key=len)
print(''.join(s))