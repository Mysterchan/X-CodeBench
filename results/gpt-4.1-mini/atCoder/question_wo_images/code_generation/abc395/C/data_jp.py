N = int(input())
A = list(map(int, input().split()))

last_pos = {}
min_length = float('inf')

for i, x in enumerate(A):
    if x in last_pos:
        length = i - last_pos[x] + 1
        if length < min_length:
            min_length = length
    last_pos[x] = i

print(min_length if min_length != float('inf') else -1)