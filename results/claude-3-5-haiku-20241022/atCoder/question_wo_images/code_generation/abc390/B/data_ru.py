n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print("Yes")
else:
    is_geometric = True
    for i in range(n - 2):
        if a[i] * a[i + 2] != a[i + 1] * a[i + 1]:
            is_geometric = False
            break
    
    if is_geometric:
        print("Yes")
    else:
        print("No")