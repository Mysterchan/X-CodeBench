import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        q = int(input())
        size = 1 << n  # 2^n
        total = size * size

        # Each quadrant size
        half = size >> 1
        block = half * half

        # The order of quadrants:
        # 1: top-left
        # 2: bottom-right
        # 3: bottom-left
        # 4: top-right
        # The numbering order is: TL -> BR -> BL -> TR

        # For position to number:
        def pos_to_num(x, y, n):
            if n == 1:
                # 2x2 base case:
                # positions:
                # (1,1) = 1
                # (2,2) = 2
                # (2,1) = 3
                # (1,2) = 4
                if x == 1 and y == 1:
                    return 1
                elif x == 2 and y == 2:
                    return 2
                elif x == 2 and y == 1:
                    return 3
                else:  # x==1 and y==2
                    return 4
            half = 1 << (n - 1)
            block = half * half
            if x <= half and y <= half:
                # top-left
                return pos_to_num(x, y, n - 1)
            elif x > half and y > half:
                # bottom-right
                return block + pos_to_num(x - half, y - half, n - 1)
            elif x > half and y <= half:
                # bottom-left
                return 2 * block + pos_to_num(x - half, y, n - 1)
            else:
                # top-right
                return 3 * block + pos_to_num(x, y - half, n - 1)

        # For number to position:
        def num_to_pos(d, n):
            if n == 1:
                # base 2x2
                if d == 1:
                    return (1, 1)
                elif d == 2:
                    return (2, 2)
                elif d == 3:
                    return (2, 1)
                else:  # d == 4
                    return (1, 2)
            half = 1 << (n - 1)
            block = half * half
            if d <= block:
                # top-left
                x, y = num_to_pos(d, n - 1)
                return (x, y)
            elif d <= 2 * block:
                # bottom-right
                x, y = num_to_pos(d - block, n - 1)
                return (x + half, y + half)
            elif d <= 3 * block:
                # bottom-left
                x, y = num_to_pos(d - 2 * block, n - 1)
                return (x + half, y)
            else:
                # top-right
                x, y = num_to_pos(d - 3 * block, n - 1)
                return (x, y + half)

        for __ in range(q):
            line = input().split()
            if line[0] == '->':
                x, y = int(line[1]), int(line[2])
                print(pos_to_num(x, y, n))
            else:
                d = int(line[1])
                x, y = num_to_pos(d, n)
                print(x, y)

if __name__ == "__main__":
    solve()