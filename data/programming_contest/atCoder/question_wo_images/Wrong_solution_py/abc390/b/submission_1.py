cnt = int(input())
num_list = list(map(int,input().split()))

if not 0 in num_list:
    ratio = num_list[1] / num_list[0]
    is_geometric = True
    for i in range(cnt - 1):
        eps = 1e-9
        current_ratio = num_list[i+1] / num_list[i]

        if abs(current_ratio - ratio) >eps:
            is_geometric = False
            break
    print("Yes" if is_geometric == True else "No")
else:
    print("No")