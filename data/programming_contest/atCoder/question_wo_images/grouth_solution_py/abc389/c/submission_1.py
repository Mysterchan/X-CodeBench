def solve(q):
	global delnum, update
	order = int(q[0])

	if order == 1:
		snake = int(q[1])
		if len(S) == 0: pos = 0
		else: pos = S[-1][0]+S[-1][1]
		S.append([snake, pos])
	elif order == 2:
		delnum += 1
	else:
		k = int(q[1])
		if delnum == 0: update = 0
		else: update = S[delnum][1]
		print(S[k-1+delnum][1]-update)

S = []
delnum, update = 0, 0
Q = int(input())
for _ in range(Q):
	solve(input().split(' '))