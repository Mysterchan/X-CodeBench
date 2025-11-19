t = int(input())
for r in range(t):
    n, m, k = (int(x) for x in input().split())
    t = 0
    mt = 0
    b = [0] * m
    for i in range(k):
        a1, b1 = (int(x) for x in input().split())
        if mt < b1:
            t = 1
            mt = b1
        elif mt == b1:
            t += 1
        b[b1-1] += 1
    if mt == 1:
        print("Yuyu")
    elif n > 1:
        for i in b[1:]:
            if i % 2:
                print("Mimo")
                break
        else:
            print("Yuyu")
    else:
        ans = b[1]
        if ans % 2 == 0:
            print("Yuyu")
        else:
            print("Mimo")




