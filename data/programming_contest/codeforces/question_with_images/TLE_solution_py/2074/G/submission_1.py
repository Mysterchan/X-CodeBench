import sys
import math
t = int(input())

def sol():
	n = int(input())




	a = [int(i) for i in input().split()]


	def help(s):

		if len(s) < 3:
			return 0
		else:

			best = 0
			nl = len(s)
			for i in range(nl):
				for j in range(i+1, nl):
					for k in range(j+1, nl):
						best = max(best, s[i] * s[j] * s[k] + help(s[i+1: j]) + help(s[j+1:k]) + help(s[:i] + s[k+1:]))
			return best
	print(help(a))



for _ in range(t):
	sol()
