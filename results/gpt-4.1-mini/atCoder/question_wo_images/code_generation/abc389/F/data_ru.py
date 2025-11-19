import sys
input = sys.stdin.readline

MAX_R = 500000

N = int(input())
diff = [0] * (MAX_R + 2)  # +2 to avoid index error on R_i+1

for _ in range(N):
    L, R = map(int, input().split())
    diff[L] += 1
    if R + 1 <= MAX_R:
        diff[R + 1] -= 1

# Prefix sum to get count of intervals covering each rating
for i in range(1, MAX_R + 1):
    diff[i] += diff[i - 1]

Q = int(input())
for _ in range(Q):
    X = int(input())
    # Final rating = initial rating + number of intervals covering X
    print(X + diff[X])