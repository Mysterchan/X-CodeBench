import math

t=int(input())
for _ in range(t):
    n=int(input())
    q=int(input())
    for i in range(q):
        te=input()
        start_x=0
        start_y=0
        if te[:2]=="->":
            k,x,y=map(str,te.split())
            y,x=int(x),int(y)
            curr=2**(n-1)
            p=(2**(n-1))**2
            num=0
            while curr>0:
                if x>curr:
                    if y>curr:
                        num+=p
                        x-=curr
                        y-=curr
                    else:
                        x-=curr
                        num+=p*3
                else:
                    if y>curr:
                        y-=curr
                        num += p*2
                curr//=2
                p//=4
            print(num+1)
        else:
            k, p = map(str, te.split())
            num=int(p)
            x=(2**(n-1))**2
            l=m=1
            y=2**(n-1)
            while x!=0:
                if num>3*x:
                    l += y
                    num-=3*x
                elif num>2*x:
                    m += y
                    num-=2*x
                elif num>x:
                    l += y
                    m += y
                    num-=x
                x //= 4
                y//=2
            print(m,l)
