def can_reach_n(n, m, a, b, bad_ranges):
    # Create a list to represent if a position is bad
    bad_positions = [False] * (n + 1)

    # Mark bad positions based on the given ranges
    for l, r in bad_ranges:
        for pos in range(l, r + 1):
            bad_positions[pos] = True

    # BFS to find if we can reach position N
    from collections import deque

    queue = deque([1])  # Start from position 1
    visited = [False] * (n + 1)
    visited[1] = True

    while queue:
        current = queue.popleft()

        # Check if we can reach position N
        if current == n:
            return "Yes"

        # Explore the next positions
        for move in range(a, b + 1):
            next_pos = current + move
            if next_pos <= n and not bad_positions[next_pos] and not visited[next_pos]:
                visited[next_pos] = True
                queue.append(next_pos)

    return "No"


# Read input
n, m, a, b = map(int, input().strip().split())
bad_ranges = [tuple(map(int, input().strip().split())) for _ in range(m)]

# Get result and print
result = can_reach_n(n, m, a, b, bad_ranges)
print(result)