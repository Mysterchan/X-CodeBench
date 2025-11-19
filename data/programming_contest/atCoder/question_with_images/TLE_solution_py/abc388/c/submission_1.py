def solve(N, A):
	ans = 0
	for n in range(len(A)):
		a = A[n]
		for k in range(n+1,len(A)):
			b = A[k]
			if b >= 2*a:
				ans += (len(A)-k)
				break
	return ans
N = int(input())
A = [int(_) for _ in input().split(' ')]
print(solve(N, A))