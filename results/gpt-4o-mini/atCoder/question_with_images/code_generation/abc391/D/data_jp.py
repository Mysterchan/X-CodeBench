def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    # Read N and W
    index = 0
    N = int(data[index])
    W = int(data[index + 1])
    index += 2

    # Read the positions of the blocks
    positions = []
    for _ in range(N):
        x = int(data[index])
        y = int(data[index + 1])
        positions.append((x, y))
        index += 2

    # Read Q
    Q = int(data[index])
    index += 1

    # Read the queries
    queries = []
    for _ in range(Q):
        T = int(data[index])
        A = int(data[index + 1]) - 1  # Store 0-indexed
        queries.append((T, A))
        index += 2

    # Process the blocks
    # Track the block heights
    from collections import defaultdict

    height_map = defaultdict(int)
    for x, y in positions:
        height_map[x] = max(height_map[x], y)

    results = []

    for T, A in queries:
        block_index = A
        block_x, block_y = positions[block_index]

        # Effective final y-coordinate after T time
        final_y = block_y - T  # How many units it would try to fall

        # Check if it would fall off the grid
        if final_y <= 0:
            results.append("No")
            continue

        # Check if it can go down or will hit another block
        # Getting the blocks in the same column that are higher
        if height_map[block_x] >= final_y:
            results.append("No")
        else:
            results.append("Yes")

    # Print all results
    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    main()