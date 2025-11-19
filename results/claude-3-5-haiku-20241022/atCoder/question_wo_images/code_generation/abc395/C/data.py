N = int(input())
A = list(map(int, input().split()))

last_pos = {}
min_length = float('inf')

for i in range(N):
    if A[i] in last_pos:
        length = i - last_pos[A[i]] + 1
        min_length = min(min_length, length)
    last_pos[A[i]] = i

if min_length == float('inf'):
    print(-1)
else:
    print(min_length)