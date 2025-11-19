def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    idx = 0
    N, W = map(int, data[idx].split())
    idx += 1
    
    # Read block positions
    blocks = []
    for i in range(N):
        x, y = map(int, data[idx].split())
        blocks.append((x, y))
        idx += 1
    
    # Read the queries
    Q = int(data[idx])
    idx += 1
    queries = []
    for i in range(Q):
        t, a = map(int, data[idx].split())
        queries.append((t, a - 1))  # store the index (0-based)
        idx += 1
    
    # We need to process the blocks
    # Step 1: Organize blocks by column
    from collections import defaultdict
    
    columns = defaultdict(list)
    for i in range(N):
        x, y = blocks[i]
        columns[x].append((y, i))

    # Step 2: Sort blocks in each column by their y coordinate
    for col in columns:
        columns[col].sort()
    
    # Step 3: Process queries
    results = []
    for t, a in queries:
        x, y = blocks[a]
        
        # Height of the block at (x,y)
        height = y
        moves = 0
        
        # Check if the block will be eliminated
        # Calculate the bottom row state after `t` seconds
        if height <= t:  # the block might be removed
            # Count how many blocks are in the same column and below
            if x in columns:
                lower_blocks = [b[0] for b in columns[x]]  # y coords of blocks in column x
                fills = sum(1 for b in lower_blocks if b <= height)
                moves = min(fills, t)  # max it can move is the number of time units or fills
            else:
                moves = 0  # no blocks below this column

            if height - moves <= 0:
                results.append("No")
            else:
                results.append("Yes")
        else:
            results.append("Yes")
            
    print("\n".join(results))

main()