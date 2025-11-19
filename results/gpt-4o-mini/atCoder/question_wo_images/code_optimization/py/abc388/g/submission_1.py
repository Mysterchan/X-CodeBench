N = int(input())
A = list(map(int, input().split()))
Q = int(input())
queries = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(Q)]

results = []

for L, R in queries:
    count = 0
    pairs = []

    for i in range(L, R + 1):
        for j in range(i + 1, R + 1):
            if A[i] * 2 >= A[j]:  # A[i] can be stacked on A[j]
                count += 1
                pairs.append((A[i], A[j]))

    results.append(count)

print('\n'.join(map(str, results)))