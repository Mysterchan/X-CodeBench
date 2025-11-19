def solve(N, C):
	for n in range(N):
		x = 0
		for k in range(n):
			if C[k] > 0:
				C[k] -= 1
				x += 1
		C[n] += x
	S = [str(_) for _ in C]
	return " ".join(S)
N = int(input())
C = [int(_) for _ in input().split(' ')]
print(solve(N, C))