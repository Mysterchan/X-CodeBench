import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
pigeon = [i for i in range(1, N+1)]
nest = [1]*N

for _ in range(Q):
  ty, *q = map(int, input().split())
  if ty == 1:
    n = pigeon[q[0]-1]
    nest[n-1] -= 1
    pigeon[q[0]-1] = q[1]
    nest[q[1]-1] += 1
  elif ty == 2:
    print(sum(i>=2 for i in nest))