t=int(input())
for tc in range(t):
	n=int(input())
	ans=0
	for i in range(n):
		a,b,c,d=map(int,input().split())
		if b>d:
			ans+=b-d+a
		elif a>c:
			ans+=a-c
	print(ans)
