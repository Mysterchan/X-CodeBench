n = int(input())

s = []

for _ in range(n):
    s.append(input())

s_num =[]

for i in s:
    s_num.append(len(i))

s_num_sort =  sorted(s_num)

ans = []

for j in s_num_sort:
    for k in s:
        if j == len(k):
            ans.append(k)

for p in ans:
    ans += p