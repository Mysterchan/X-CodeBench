import math
from collections import Counter

fs = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
def solve(n, k, arrs):
   s = ''
   for arr in arrs:
      if arr[0] >= arr[1] and arr[0] >= arr[2]:
         x, y, z = arr[0], arr[1], arr[2]
      elif arr[1] >= arr[0] and arr[1] >= arr[2]:
         x, y, z = arr[1], arr[0], arr[2]
      else:
         x, y, z = arr[2], arr[1], arr[0]

      if x >= fs[n] and y >= fs[n-1] and z >= fs[n-1]:
         s += '1'
      else:
         s += '0'
   return s

t = int(input())
for _ in range(t):
   n, k = map(int, input().strip().split())
   arrs = []
   for _ in range(k):
      arr = list(map(int, input().strip().split()))
      arrs.append(arr)
   print(solve(n, k, arrs))
