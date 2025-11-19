n = int(input())
s = [input() for _ in range(n)]
t = [input() for _ in range(n)]

def rotate_90(grid):
    # Rotate grid 90 degrees clockwise
    return [''.join(grid[n - 1 - j][i] for j in range(n)) for i in range(n)]

ans = float('inf')
current = s
for _ in range(4):
    diff = 0
    for i in range(n):
        for j in range(n):
            if current[i][j] != t[i][j]:
                diff += 1
    ans = min(ans, diff)
    current = rotate_90(current)

print(ans)