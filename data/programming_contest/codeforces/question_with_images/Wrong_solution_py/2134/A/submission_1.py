t=int(input())
for _ in range(t):
    n,a,b = map(int,input().split())
    if n==a and a==b:
        print("Yes")
        continue
    if n%2==0 and b%2==0:
        if a%2==0 or a<=b:
            print("Yes")
    elif n%2!=0 and b%2!=0:
        if a<=b or a%2!=0:
            print("Yes")

    else:
        print("No")
