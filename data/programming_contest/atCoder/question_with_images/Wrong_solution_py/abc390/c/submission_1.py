H,W=map(int,input().split())
S=[]
left=W
right=0
up=H
down=0
for h in range(H):
	M=list(input())
	for enu,m in enumerate(M):
		if m == "
			left=min(left,enu)
			right=max(right,enu)
			up=min(up,h)
			down=max(down,h)
	S.append(M)
for h in range(up,down+1):
	for s in S[h][left:down+1]:
		if s==".":
			print("No")
			exit()
print("Yes")