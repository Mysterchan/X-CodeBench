import sys
input = sys.stdin.readline
def solve():
  N = int(input())
  A = list(map(int, input().split()))
  A.sort()
  pre = [0] * (N + 1)
  for i in range(N):
    pre[i + 1] = pre[i] + A[i]
  ans = 0
  for i in range(1, N + 1):
    lo, hi = 0, i - 1
    while lo <= hi:
      x = (lo + hi) // 2
      if A[x] * i <= pre[i]:
        lo = x + 1
      else:
        hi = x - 1
    ans = max(ans,i - lo)
  print(ans)
if __name__ == "__main__":
  for test in range(int(input())):
    solve()