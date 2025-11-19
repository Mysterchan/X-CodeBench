N, K = map(int, input().split())

# The number of paths to reach (N, N) from (1, 1) is (2N-2) choose (N-1)
# or equivalently: (2N-2)! / ((N-1)! * (N-1)!)
# This gives us a direct way of determining when to take R or D based on K's binary representation.

def choose(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)  # Take advantage of symmetry
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c

path = []
down_moves, right_moves = N - 1, N - 1

for step in range(2 * N - 2):
    if down_moves == 0:  # Only right moves left
        path.append('R')
        right_moves -= 1
        continue
    if right_moves == 0:  # Only down moves left
        path.append('D')
        down_moves -= 1
        continue

    # Calculate paths if we take a down move
    paths_if_down = choose(down_moves + right_moves - 1, right_moves)

    if K <= paths_if_down:  # We can afford to go down
        path.append('D')
        down_moves -= 1
    else:  # We must go right
        K -= paths_if_down
        path.append('R')
        right_moves -= 1

print(''.join(path))