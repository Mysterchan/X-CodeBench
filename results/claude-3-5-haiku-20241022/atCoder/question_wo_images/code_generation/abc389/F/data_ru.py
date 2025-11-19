import sys
input = sys.stdin.read
data = input().split()

idx = 0
N = int(data[idx])
idx += 1

contests = []
for _ in range(N):
    L = int(data[idx])
    R = int(data[idx + 1])
    contests.append((L, R))
    idx += 2

Q = int(data[idx])
idx += 1

queries = []
for _ in range(Q):
    X = int(data[idx])
    queries.append(X)
    idx += 1

for X in queries:
    rating = X
    for L, R in contests:
        if L <= rating <= R:
            rating += 1
    print(rating)