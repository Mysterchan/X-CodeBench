def find_path(N, K):
    path = []
    down_count = 0
    right_count = 0
    total_moves = 2 * N - 2

    # We need to make N-1 down moves and N-1 right moves
    while down_count < N - 1 or right_count < N - 1:
        # Calculate how many paths are possible if we go down next
        down_possible = (N - 1 - down_count)  # Remaining downs
        right_possible = (N - 1 - right_count)  # Remaining rights

        # Using binomial coefficient C(n, k) to calculate the number of paths
        paths_if_down = 1
        if down_possible > 0 and right_possible > 0:
            paths_if_down = factorial(down_possible + right_possible) // (
                factorial(down_possible) * factorial(right_possible)
            )

        if paths_if_down >= K:
            path.append('D')
            down_count += 1
        else:
            path.append('R')
            K -= paths_if_down
            right_count += 1

    return ''.join(path)

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

N, K = map(int, input().split())
print(find_path(N, K))