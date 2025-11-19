n, w = map(int,input().split())
xy = list()
xy_dict = dict()

for i in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    xy.append((x, y))
    xy_dict[(x, y)] = i

xy.sort()

from_left = [[] for _ in range(w)]
for col, row in xy:
    from_left[col].append(row)

disapear_row_cnt = len(min(from_left, key = len))

disapear_time = [-1] * n

disapear_list = [[] for _ in range(disapear_row_cnt)]
for i in range(disapear_row_cnt):
    t_max = 0
    for j in range(len(from_left)):
        disapear_list[i].append(from_left[j][i])
        t_max = max(t_max, from_left[j][i])

    for col, row in enumerate(disapear_list[i]):
        disapear_time[xy_dict[(col, row)]] = t_max + 1

q = int(input())
for _ in range(q):
    t, a = map(int,input().split())
    a -= 1
    if disapear_time[a] == -1:
        print("Yes")
    elif disapear_time[a] < t + 0.5:
        print("No")
    else:
        print("Yes")