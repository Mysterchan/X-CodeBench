def solve():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    if sum(a)!=sum(b):
        print("No")
        return

    if sum(a)==1:
        if a==b:
            print("Yes")
            return

        i = a.index(1)
        j = b.index(1)
        if 0<i<n-1 and 0<j<n-1:
            print("Yes")
        else:
            print("No")

    else:
        print("Yes")

for nt in range(int(input())):
    solve()