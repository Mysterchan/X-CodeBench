import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        q = int(input())
        size = 1 << n  # 2^n
        total = size * size

        # Precompute powers of 4 for quick access
        pow4 = [1] * (n+1)
        for i in range(1, n+1):
            pow4[i] = pow4[i-1] << 2  # 4^i

        # The order of quadrants is:
        # 0: top-left
        # 1: bottom-right
        # 2: bottom-left
        # 3: top-right
        # Each quadrant has size (2^(n-1))^2 = 4^(n-1)

        def pos_to_num(x, y, level):
            if level == 1:
                # Base case 2x2 matrix
                # Positions (x,y) in {0,1}
                # Fill order:
                # (0,0) -> 1
                # (1,1) -> 2
                # (1,0) -> 3
                # (0,1) -> 4
                if x == 0 and y == 0:
                    return 1
                elif x == 1 and y == 1:
                    return 2
                elif x == 1 and y == 0:
                    return 3
                else:  # x==0 and y==1
                    return 4
            half = 1 << (level - 1)
            block_size = pow4[level - 1]
            if x < half and y < half:
                # top-left
                return pos_to_num(x, y, level - 1)
            elif x >= half and y >= half:
                # bottom-right
                return block_size + pos_to_num(x - half, y - half, level - 1)
            elif x >= half and y < half:
                # bottom-left
                return 2 * block_size + pos_to_num(x - half, y, level - 1)
            else:
                # top-right
                return 3 * block_size + pos_to_num(x, y - half, level - 1)

        def num_to_pos(d, level):
            if level == 1:
                # Base case 2x2 matrix
                # d in 1..4
                if d == 1:
                    return (0, 0)
                elif d == 2:
                    return (1, 1)
                elif d == 3:
                    return (1, 0)
                else:  # d == 4
                    return (0, 1)
            half = 1 << (level - 1)
            block_size = pow4[level - 1]
            if d <= block_size:
                # top-left
                x, y = num_to_pos(d, level - 1)
                return (x, y)
            elif d <= 2 * block_size:
                # bottom-right
                x, y = num_to_pos(d - block_size, level - 1)
                return (x + half, y + half)
            elif d <= 3 * block_size:
                # bottom-left
                x, y = num_to_pos(d - 2 * block_size, level - 1)
                return (x + half, y)
            else:
                # top-right
                x, y = num_to_pos(d - 3 * block_size, level - 1)
                return (x, y + half)

        for __ in range(q):
            line = input().split()
            if line[0] == '->':
                x, y = int(line[1]) - 1, int(line[2]) - 1
                print(pos_to_num(x, y, n))
            else:
                d = int(line[1])
                x, y = num_to_pos(d, n)
                print(x + 1, y + 1)

if __name__ == "__main__":
    solve()