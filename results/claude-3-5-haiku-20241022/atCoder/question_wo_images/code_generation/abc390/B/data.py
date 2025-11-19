n = int(input())
a = list(map(int, input().split()))

if n == 2:
    print("Yes")
else:
    is_gp = True
    for i in range(2, n):
        if a[i] * a[i-2] != a[i-1] * a[i-1]:
            is_gp = False
            break
    
    if is_gp:
        print("Yes")
    else:
        print("No")