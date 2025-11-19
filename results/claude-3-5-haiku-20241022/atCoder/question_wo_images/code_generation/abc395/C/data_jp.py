N = int(input())
A = list(map(int, input().split()))

min_length = float('inf')

for i in range(N):
    seen = set()
    for j in range(i, N):
        if A[j] in seen:
            min_length = min(min_length, j - i + 1)
            break
        seen.add(A[j])

if min_length == float('inf'):
    print(-1)
else:
    print(min_length)