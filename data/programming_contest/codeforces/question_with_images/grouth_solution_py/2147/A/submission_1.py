for _ in range(int(input())):
    x, y = map(int, input().split())
    print(2 if x<y else 3 if x-1>y>1 else -1)
