N = int(input())
contests = []
for _ in range(N):
    L, R = map(int, input().split())
    contests.append((L, R))

Q = int(input())
for _ in range(Q):
    X = int(input())
    rating = X
    for L, R in contests:
        if L <= rating <= R:
            rating += 1
    print(rating)