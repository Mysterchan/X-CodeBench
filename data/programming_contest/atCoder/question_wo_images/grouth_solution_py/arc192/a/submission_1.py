a = int(input())
b = list(map(int, input().split()))
if a % 4 == 0:
    print("Yes")
elif a % 2 and not 1 in b:
    print("No")
elif a % 2:
    print("Yes")
else:
    if b.count(1) < 2:
        print("No")
    else:
        x = set()
        for i in range(a):
            if b[i] == 1 and i % 2 == 0:
                x.add(0)
            elif b[i] == 1 and i % 2 == 1:
                x.add(1)
        if len(x) == 2:
            print("Yes")
        else:
            print("No")