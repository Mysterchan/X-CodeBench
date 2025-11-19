N, W = map(int, input().split())

blocks = {}
for i in range(N):
    x, y = map(int, input().split())
    if x not in blocks:
        blocks[x] = []
    blocks[x].append((y, i + 1))

for x in blocks:
    blocks[x].sort(reverse=True)

max_height = {}
for x in blocks:
    max_height[x] = blocks[x][0][0]

Q = int(input())
results = []
for _ in range(Q):
    T, A = map(int, input().split())
    x_pos = A - 1
    if x_pos not in blocks or blocks[x_pos + 1][0][1] <= T:
        results.append('No')
        continue
    
    y, block_index = next((y, idx) for y, idx in blocks[x_pos + 1] if idx == A)
    
    if block_index <= T + (max_height[x_pos + 1] <= T):
        results.append('No')
    else:
        results.append('Yes')

print("\n".join(results))