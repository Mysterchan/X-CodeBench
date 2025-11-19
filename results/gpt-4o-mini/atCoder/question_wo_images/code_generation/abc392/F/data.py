import sys
from collections import deque

input = sys.stdin.read
data = input().split()

N = int(data[0])
P = list(map(int, data[1:]))

A = deque()

for i in range(1, N + 1):
    A.insert(P[i - 1] - 1, i)

print(" ".join(map(str, A)))