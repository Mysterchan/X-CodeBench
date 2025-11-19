import sys
input = sys.stdin.readline

N = int(input())
MAX = 500000
diff = [0] * (MAX + 2)

for _ in range(N):
    L, R = map(int, input().split())
    diff[L] += 1
    if R + 1 <= MAX:
        diff[R + 1] -= 1

# prefix sum to get count of intervals covering each rating
for i in range(1, MAX + 1):
    diff[i] += diff[i - 1]

Q = int(input())
for _ in range(Q):
    X = int(input())
    # final rating = initial rating + number of intervals covering X
    print(X + diff[X])