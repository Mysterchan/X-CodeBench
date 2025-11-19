s = input()

for i in range(len(s)-1, 0, -1):
    s = s.replace('W'*i + 'A', 'A' + 'C'*i)

print(s)