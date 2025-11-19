test = int(input())

for _ in range(test):
    points , side = map(int,input().split())
    arr = []

    count = 0

    for i in range(points):
        dirx , diry , x , y = map(int,input().split())
        arr.append((dirx,diry,x,y))



    for dirx,diry,x,y in arr:
        if (dirx == 1 and diry == -1) or (dirx == -1 and diry == 1) :
            if abs(x - 4) == abs(y - 0) :
                count += 1
        else:
            if abs(x-0) == abs(y-0):
                count += 1

    print(count)
