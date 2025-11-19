for i in range(int(input())):
    n = int(input().split(" ")[1])
    l = list(map(int, input().split(" ")))
    n = l[n-1]
    l = sorted(l)
    cmax = 0
    for j in range(len(l)-l.index(n)-1):
        cmax = max(cmax, l[j+1] - l[j])
    if cmax > n:
        print("NO")
    else:
        print("YES")
