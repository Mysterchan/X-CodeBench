import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        q = int(input())
        size = 1 << n  # 2^n
        total = size * size  # 2^(2n)

        # Precompute half size for convenience
        half = size >> 1

        # The order of quadrants is fixed:
        # 1: top-left
        # 2: bottom-right
        # 3: bottom-left
        # 4: top-right
        # Each quadrant has size (half x half) and contains (half*half) numbers.

        def get_num(x, y, size, start):
            # x,y: 1-based coordinates in current square
            # size: current square size (2^k)
            # start: starting number for this square
            if size == 2:
                # Base case: 2x2 table
                # Positions:
                # (1,1): start + 0
                # (1,2): start + 3
                # (2,1): start + 2
                # (2,2): start + 1
                if x == 1 and y == 1:
                    return start + 0
                elif x == 1 and y == 2:
                    return start + 3
                elif x == 2 and y == 1:
                    return start + 2
                else:  # x==2 and y==2
                    return start + 1

            half = size >> 1
            block_size = half * half

            # Determine which quadrant (x,y) belongs to
            if x <= half and y <= half:
                # top-left
                return get_num(x, y, half, start)
            elif x > half and y > half:
                # bottom-right
                return get_num(x - half, y - half, half, start + block_size)
            elif x > half and y <= half:
                # bottom-left
                return get_num(x - half, y, half, start + 2 * block_size)
            else:
                # top-right
                return get_num(x, y - half, half, start + 3 * block_size)

        def get_pos(d, size, start, top_x, top_y):
            # d: number to find
            # size: current square size
            # start: starting number for this square
            # top_x, top_y: top-left coordinate of current square (1-based)
            if size == 2:
                # Base case: 2x2 table
                # Numbers and positions:
                # start+0: (top_x, top_y)
                # start+3: (top_x, top_y+1)
                # start+2: (top_x+1, top_y)
                # start+1: (top_x+1, top_y+1)
                offset = d - start
                if offset == 0:
                    return (top_x, top_y)
                elif offset == 3:
                    return (top_x, top_y + 1)
                elif offset == 2:
                    return (top_x + 1, top_y)
                else:  # offset == 1
                    return (top_x + 1, top_y + 1)

            half = size >> 1
            block_size = half * half

            # Determine which quadrant d belongs to
            if start <= d < start + block_size:
                # top-left
                return get_pos(d, half, start, top_x, top_y)
            elif start + block_size <= d < start + 2 * block_size:
                # bottom-right
                return get_pos(d, half, start + block_size, top_x + half, top_y + half)
            elif start + 2 * block_size <= d < start + 3 * block_size:
                # bottom-left
                return get_pos(d, half, start + 2 * block_size, top_x + half, top_y)
            else:
                # top-right
                return get_pos(d, half, start + 3 * block_size, top_x, top_y + half)

        for __ in range(q):
            line = input().split()
            if line[0] == '->':
                x, y = int(line[1]), int(line[2])
                print(get_num(x, y, size, 1))
            else:
                d = int(line[1])
                x, y = get_pos(d, size, 1, 1, 1)
                print(x, y)

if __name__ == "__main__":
    solve()