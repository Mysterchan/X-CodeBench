def run_block_simulation():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    # Read N and W
    N, W = map(int, data[0].split())

    # Read positions of blocks
    blocks = []
    for i in range(1, N + 1):
        x, y = map(int, data[i].split())
        blocks.append((x, y))

    # Read number of queries
    Q_start_index = N + 1
    Q = int(data[Q_start_index])

    # Read all queries
    queries = []
    for i in range(Q_start_index + 1, Q_start_index + 1 + Q):
        t, a = map(int, data[i].split())
        queries.append((t, a - 1))  # zero-indexing for easier access

    # Setup game state
    current_heights = [0] * (W + 1)  # max height of blocks in each column
    exists = [True] * N  # whether each block is still in existence

    # Initialize the positions of blocks
    for i in range(N):
        x, y = blocks[i]
        current_heights[x] = max(current_heights[x], y)

    results = []
    for t, a in queries:
        x, y = blocks[a]
        
        # Determine the ground level at the queried time
        if exists[a]:
            ground_level = current_heights[x]
            if y < ground_level:
                # Block 'a' is below the ground level, it must have been removed
                results.append("No")
            else:
                # At time t, how far can block 'a' drop?
                # 1. Find current height minus its own height
                max_drop = t - (y - ground_level)
                
                if max_drop >= 0:
                    # The block will drop
                    if ground_level == y + max_drop:
                        # Just at ground level, it may exist
                        results.append("No")
                    else:
                        # Check if it still exists or is above the ground
                        if max_drop + y >= ground_level:
                            results.append("Yes")
                        else:
                            results.append("Yes")
                else:
                    results.append("Yes")
        else:
            results.append("No")

    print("\n".join(results))

run_block_simulation()