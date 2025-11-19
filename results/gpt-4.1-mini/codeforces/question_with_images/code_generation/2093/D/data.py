import sys
input = sys.stdin.readline

# The order of filling 2x2 blocks is:
# top-left (0), bottom-right (1), bottom-left (2), top-right (3)
# with numbers assigned as:
# (0,0) -> 1
# (1,1) -> 2
# (1,0) -> 3
# (0,1) -> 4

# We'll implement two functions:
# 1) get_number(x, y, size, start_num): returns the number at cell (x,y)
# 2) get_position(d, size, start_num): returns the (x,y) position of number d

# Coordinates and numbering are 1-based externally, but internally we use 0-based.

def get_number(x, y, size, start_num):
    # x,y: 0-based coordinates inside current square of size 'size'
    # start_num: the starting number for this square
    if size == 2:
        # base case: 2x2 block
        # positions:
        # (0,0) -> start_num + 0
        # (1,1) -> start_num + 1
        # (1,0) -> start_num + 2
        # (0,1) -> start_num + 3
        if x == 0 and y == 0:
            return start_num + 0
        elif x == 1 and y == 1:
            return start_num + 1
        elif x == 1 and y == 0:
            return start_num + 2
        elif x == 0 and y == 1:
            return start_num + 3
    half = size // 2
    block_size = half * half
    # Determine which quadrant (x,y) belongs to:
    # order: top-left(0), bottom-right(1), bottom-left(2), top-right(3)
    if x < half and y < half:
        # top-left
        return get_number(x, y, half, start_num)
    elif x >= half and y >= half:
        # bottom-right
        return get_number(x - half, y - half, half, start_num + block_size)
    elif x >= half and y < half:
        # bottom-left
        return get_number(x - half, y, half, start_num + 2 * block_size)
    else:
        # top-right
        return get_number(x, y - half, half, start_num + 3 * block_size)

def get_position(d, size, start_num):
    # returns (x,y) 0-based coordinates of number d in current square
    if size == 2:
        # base case: 2x2 block
        # numbers:
        # start_num + 0 -> (0,0)
        # start_num + 1 -> (1,1)
        # start_num + 2 -> (1,0)
        # start_num + 3 -> (0,1)
        offset = d - start_num
        if offset == 0:
            return (0,0)
        elif offset == 1:
            return (1,1)
        elif offset == 2:
            return (1,0)
        elif offset == 3:
            return (0,1)
    half = size // 2
    block_size = half * half
    # Determine which quadrant d belongs to:
    if d < start_num + block_size:
        # top-left
        x, y = get_position(d, half, start_num)
        return (x, y)
    elif d < start_num + 2 * block_size:
        # bottom-right
        x, y = get_position(d, half, start_num + block_size)
        return (x + half, y + half)
    elif d < start_num + 3 * block_size:
        # bottom-left
        x, y = get_position(d, half, start_num + 2 * block_size)
        return (x + half, y)
    else:
        # top-right
        x, y = get_position(d, half, start_num + 3 * block_size)
        return (x, y + half)

t = int(input())
for _ in range(t):
    n = int(input())
    q = int(input())
    size = 1 << n  # 2^n
    for __ in range(q):
        line = input().split()
        if line[0] == '->':
            # query: what number at (x,y)
            x = int(line[1]) - 1
            y = int(line[2]) - 1
            ans = get_number(x, y, size, 1)
            print(ans)
        else:
            # query: where is number d
            d = int(line[1])
            x, y = get_position(d, size, 1)
            print(x+1, y+1)