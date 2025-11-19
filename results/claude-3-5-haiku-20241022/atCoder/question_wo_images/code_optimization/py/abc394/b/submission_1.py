n = int(input())
s = []
for _ in range(n):
    s.append(input())

s.sort(key=len)

print(''.join(s))