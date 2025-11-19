for _ in range(int(input())):
    n=int(input());a=sorted([list(map(int,input().split()))[1:] for i in range(n)], reverse=1);res=[]
    while len(a):res+=a[-1];l=len(a[-1]);a=sorted([i[l:] for i in a if i[l:]], reverse=1)
    print(*res)
