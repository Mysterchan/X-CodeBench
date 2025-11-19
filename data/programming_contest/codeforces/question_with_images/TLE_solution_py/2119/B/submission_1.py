t=int(input())
for _ in range(t):
    answer=True
    n=int(input())
    px,py,qx,qy=[int(i) for i in input().split()]
    dis=(((px-qx)**2) +((py-qy)**2))**0.5
    arr=[int(i) for i in input().split()]
    for i in range(n):
        if dis+sum(arr)<2*arr[i] or dis+sum(arr)<2*dis:
            answer=False
            break
    if answer:
        print("yes")
    else:
        print("no")
