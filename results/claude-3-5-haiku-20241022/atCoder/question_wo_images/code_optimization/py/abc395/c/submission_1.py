N = int(input())
A = list(map(int, input().split()))

min_length = float('inf')
last_pos = {}

for i in range(N):
    if A[i] in last_pos:
        min_length = min(min_length, i - last_pos[A[i]] + 1)
    last_pos[A[i]] = i

if min_length == float('inf'):
    print(-1)
else:
    print(min_length)