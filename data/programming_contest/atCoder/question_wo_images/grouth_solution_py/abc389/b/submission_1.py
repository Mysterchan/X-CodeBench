X = int(input())
M = 3*10
r = 1
for n in range(1, M):
	r = r*n
	if r >= X: break
if r == X: print(n)