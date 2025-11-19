import sys
input = sys.stdin.readline

N, W = map(int, input().split())
blocks = [None] * N
col_blocks = [[] for _ in range(W+1)]

for i in range(N):
    x, y = map(int, input().split())
    blocks[i] = (x, y)
    col_blocks[x].append((y, i))

# Sort blocks in each column by descending y (top to bottom)
for c in range(1, W+1):
    col_blocks[c].sort(reverse=True)

# We want to find the "final resting position" of each block after infinite time
# The blocks fall down until they rest on bottom or on another block.
# Because the grid is very tall, the blocks will stack in each column.
# The bottom row is removed if all columns have a block at that row.
# This removal happens repeatedly, so the bottom row "shifts" up over time.

# Key insight:
# The blocks form stacks in each column.
# The bottom row removal happens at rows where all columns have a block.
# Each such row removal removes one block from each column.
# So the number of full rows removed = number of rows where all columns have a block.

# We want to find for each block:
# - Its initial y
# - Its "stack index" in its column (0-based from bottom)
# - The row at which it is located after infinite falling (stacked)
# Then, the number of full rows removed up to time T is min(T, total full rows removed)
# A block disappears if its stack index < number of full rows removed (because that many bottom rows are removed)
# Otherwise, it still exists.

# Step 1: For each column, sort blocks by y ascending (bottom to top) to assign stack indices
for c in range(1, W+1):
    col_blocks[c].sort()

# Step 2: For each column, record the y's in ascending order
# We want to find rows where all columns have a block.
# These rows are the intersection of the sets of y's in each column.
# Because blocks are distinct, and y can be large, we find the common rows where all columns have a block.

# We can find the intersection of the sets of y's in all columns.
# Since W <= N and N up to 2e5, and each column has at least one block,
# we can do this by a pointer approach.

# Prepare pointers for each column
ptrs = [0]*(W+1)
lens = [len(col_blocks[c]) for c in range(W+1)]

full_rows = []

while True:
    # Find current y candidates from each column
    current_ys = []
    for c in range(1, W+1):
        if ptrs[c] == lens[c]:
            # No more blocks in this column
            print("No")  # This line is just a placeholder, will remove later
            break
        current_ys.append(col_blocks[c][ptrs[c]][0])
    else:
        # All columns have a current y
        max_y = max(current_ys)
        min_y = min(current_ys)
        if max_y == min_y:
            # Found a full row
            full_rows.append(max_y)
            for c in range(1, W+1):
                ptrs[c] += 1
        else:
            # Advance pointers in columns with y < max_y
            for c in range(1, W+1):
                while ptrs[c] < lens[c] and col_blocks[c][ptrs[c]][0] < max_y:
                    ptrs[c] += 1
            # If any pointer reached end, break
            if any(ptrs[c] == lens[c] for c in range(1, W+1)):
                break
        continue
    break

# Number of full rows removed = len(full_rows)

# Step 3: For each block, find its stack index in its column (0-based from bottom)
# We already have col_blocks sorted ascending by y
# We can build a map from block index to stack index
stack_index = [0]*N
for c in range(1, W+1):
    for idx, (y, i) in enumerate(col_blocks[c]):
        stack_index[i] = idx

Q = int(input())
for _ in range(Q):
    T, A = map(int, input().split())
    A -= 1
    # Number of full rows removed at time T is min(T, len(full_rows))
    removed = T if T < len(full_rows) else len(full_rows)
    # If block's stack index < removed, it is removed
    if stack_index[A] < removed:
        print("No")
    else:
        print("Yes")