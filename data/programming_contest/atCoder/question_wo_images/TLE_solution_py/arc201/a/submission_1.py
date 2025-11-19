import io, os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
for _ in range(int(input())):
	n = int(input())
	a, b, c = [0] * n, [0] * n, [0] * n
	for i in range(n):
		a[i], b[i], c[i] = map(int,input().split())
	l, h = 0, 2 * (10 ** 14) + 5
	while(h - l > 1):
		m = (l + h) // 2
		x = [i for i in a]
		y = [i for i in b]
		z = [i for i in c]
		cnt1, cnt2 = 0, 0
		for i in range(n):
			cur = min(y[i] - z[i], x[i])
			cnt1 += cur
			x[i] -= cur
			y[i] -= cur
		for i in range(n):
			cur = min(m - cnt1, x[i], y[i])
			cnt1 += cur
			x[i] -= cur
			y[i] -= cur
		for i in range(n):
			cnt2 += min(y[i], z[i])
		if(cnt1 >= m and cnt2 >= m):
			l = m
		else:
			h = m
	print(l)