def solve():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    if sum(a)!=sum(b):
        print("No")
        return

    if sum(a)==1 and a[0]==1:
        if a==b:
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")

for nt in range(int(input())):
    solve()