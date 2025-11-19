n = int(input())
s = list(map(int, input().split()))

s_set = set(s)
count = 0

for b in s:
    for a in s:
        if a < b:
            c = 2 * b - a
            if c > b and c in s_set:
                count += 1

print(count)