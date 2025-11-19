for i in range(int(input())):
    n = list(map(int, input().split(" ")))
    if n[1] > n[0]:
        print(2)
    elif n[0] // 2 >= n[1] and n[1] > 1:
        print(3)
    else:
        print(-1)
