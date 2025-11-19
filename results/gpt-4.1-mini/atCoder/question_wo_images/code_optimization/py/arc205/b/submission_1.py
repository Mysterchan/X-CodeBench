import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# The problem reduces to parity of M:
# If M is even, max black edges = total edges = n*(n-1)//2
# If M is odd, max black edges = total edges - 1
total = n * (n - 1) // 2
print(total if m % 2 == 0 else total - 1)