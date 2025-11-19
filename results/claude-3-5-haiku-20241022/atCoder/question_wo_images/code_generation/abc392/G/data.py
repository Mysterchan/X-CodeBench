n = int(input())
s = list(map(int, input().split()))

s_set = set(s)
count = 0

s_list = sorted(s)

for i in range(n):
    for j in range(i + 1, n):
        a = s_list[i]
        c = s_list[j]
        
        if (a + c) % 2 == 0:
            b = (a + c) // 2
            if b in s_set and a < b < c:
                count += 1

print(count)