for _ in range(int(input())):
  n,k=map(int,input().split())
  a=list(map(int,input().split()))
  x=a[k-1]
  a.sort()
  print("NO"if any(a[i]-a[i-1]>x for i in range(1,n))else"YES")
