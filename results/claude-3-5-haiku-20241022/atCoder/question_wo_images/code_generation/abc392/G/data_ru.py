n = int(input())
s = list(map(int, input().split()))
s_set = set(s)
s.sort()

count = 0
for i in range(n):
    b = s[i]
    for j in range(i):
        a = s[j]
        c = 2 * b - a
        if c > b and c in s_set:
            count += 1

print(count)