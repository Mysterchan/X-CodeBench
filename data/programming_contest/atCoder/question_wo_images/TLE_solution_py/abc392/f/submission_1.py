class FenwickTree:
	def __init__(self, arr):
		baibai = 1
		while baibai < len(arr):
			baibai *= 2
		self.full = baibai * 2 - 1
		self.dat  = [0 for _ in range(baibai + 1 + 1)]
		for idx in range(len(arr)):
			self.tasu(idx, arr[idx])
	def get(self, pos):
		return(self.q(pos, pos+1))

	def tasu(self, pos, x):

		ptr = pos + 1
		while ptr < len(self.dat):
			self.dat[ptr] = self.dat[ptr] + x
			ptr += (ptr & (self.full - ptr + 1))

	def sum(self, r):

		ret = 0
		ptr = r
		while ptr > 0:
			ret = ret + self.dat[ptr]
			ptr ^= (ptr & (self.full - ptr + 1))
		return(ret)

	def q(self, l, r):

		return(self.sum(r) - self.sum(l))

n = int(input())
p = list(map(int,input().split()))

ans = [None for _ in range(n)]
tree = FenwickTree([1 for _ in range(n)])

num = n
for elem in reversed(p):
	ng = -1
	ok = n
	while ng + 1 < ok:
		mid = (ng + ok) // 2
		if tree.sum(mid+1) >= elem:
			ok = mid
		else:
			ng = mid
	pos = ok
	ans[pos] = num
	num -= 1
	tree.tasu(pos,-1)

print(" ".join(map(str, ans)))