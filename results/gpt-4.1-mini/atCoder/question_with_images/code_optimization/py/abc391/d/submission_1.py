import sys
input = sys.stdin.readline

N, W = map(int, input().split())

# Wi[x] will hold the sorted list of Y positions for column x
Wi = [[] for _ in range(W + 1)]
pos_in_col = [0] * (N + 1)  # position index of block in its column

blocks = [None] * (N + 1)  # store (x,y) for each block by id

for i in range(1, N + 1):
    x, y = map(int, input().split())
    Wi[x].append((y, i))
    blocks[i] = (x, y)

# Sort each column by Y ascending
for x in range(1, W + 1):
    Wi[x].sort()
    # Assign position index for each block in the column
    for idx, (y, i) in enumerate(Wi[x]):
        pos_in_col[i] = idx

# The number of blocks in each column
col_len = [len(Wi[x]) for x in range(W + 1)]

# The number of full bottom rows removed so far
# We want to find for each block the time it disappears (if any)
# A block disappears at the time when the bottom row is full and removed,
# and the block is in that bottom row.

# The bottom row at time 0 is the minimal Y among the bottom blocks in each column.
# After each removal, the bottom row moves up by 1 (since blocks fall down),
# but the blocks also fall down, so the relative positions matter.

# Key insight:
# The bottom row is full if and only if the bottom-most block in each column
# is at the same height.
# When the bottom row is removed, the bottom block in each column disappears,
# and the rest blocks fall down by 1.

# So the disappearance time of a block is the number of full bottom rows removed
# before it is removed.

# We can simulate the removal times by iterating over the bottom blocks in each column.

# Let's create an array to store the disappearance time for each block
# If a block never disappears, disappearance time = -1

disappear_time = [-1] * (N + 1)

# We keep pointers to the current bottom block in each column
bottom_ptr = [0] * (W + 1)

time = 0
while True:
    # Check if all columns have a bottom block
    if any(bottom_ptr[x] >= col_len[x] for x in range(1, W + 1)):
        break

    # Check if all bottom blocks have the same Y
    base_y = Wi[1][bottom_ptr[1]][0]
    full_row = True
    for x in range(2, W + 1):
        if Wi[x][bottom_ptr[x]][0] != base_y:
            full_row = False
            break

    if not full_row:
        break

    # Remove bottom row blocks
    time += 1
    for x in range(1, W + 1):
        block_id = Wi[x][bottom_ptr[x]][1]
        disappear_time[block_id] = time
        bottom_ptr[x] += 1

# Now answer queries
Q = int(input())
out = []
for _ in range(Q):
    T, A = map(int, input().split())
    dt = disappear_time[A]
    # If block never disappears or disappears after time T, it exists at T+0.5
    if dt == -1 or dt > T:
        out.append("Yes")
    else:
        out.append("No")

print("\n".join(out))