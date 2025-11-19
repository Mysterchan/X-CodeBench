n, q = map(int, input().split())
grid = [input().strip() for _ in range(n)]

# Precompute maximum black positions in a 2D prefix sum array for valid 2x2 regions
s_score = [[0] * (n - 1) for _ in range(n - 1)]

# Fill s_score with counts of valid 2x2 regions
for row in range(n - 1):
    for col in range(n - 1):
        if grid[row][col] == grid[row][col + 1] == grid[row + 1][col] == grid[row + 1][col + 1] == ".":
            s_score[row][col] = 1

# Compute 2D prefix sums
for row in range(n - 1):
    for col in range(1, n - 1):
        s_score[row][col] += s_score[row][col - 1]

# Answer each query using the prefix sums
output = []
for _ in range(q):
    u, d, l, r = map(int, input().split())
    u -= 1
    d -= 1
    l -= 1
    r -= 2

    count = 0
    for row in range(u, d):
        if l == 0:
            count += s_score[row][r]
        else:
            count += s_score[row][r] - s_score[row][l - 1]
    
    output.append(str(count))

print("\n".join(output))