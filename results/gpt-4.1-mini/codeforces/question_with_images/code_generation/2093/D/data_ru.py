import sys
input = sys.stdin.readline

def get_val(n, x, y):
    if n == 1:
        # 2x2 base case
        # positions:
        # (1,1) = 1
        # (1,2) = 4
        # (2,1) = 3
        # (2,2) = 2
        if x == 1 and y == 1:
            return 1
        elif x == 1 and y == 2:
            return 4
        elif x == 2 and y == 1:
            return 3
        else:  # x==2 and y==2
            return 2
    half = 1 << (n - 1)  # 2^(n-1)
    block_size = half * half
    if x <= half and y <= half:
        # top-left quadrant
        return get_val(n - 1, x, y)
    elif x > half and y > half:
        # bottom-right quadrant
        return block_size + get_val(n - 1, x - half, y - half)
    elif x > half and y <= half:
        # bottom-left quadrant
        return 2 * block_size + get_val(n - 1, x - half, y)
    else:
        # top-right quadrant
        return 3 * block_size + get_val(n - 1, x, y - half)

def get_pos(n, d):
    if n == 1:
        # base 2x2
        # values:
        # 1 -> (1,1)
        # 2 -> (2,2)
        # 3 -> (2,1)
        # 4 -> (1,2)
        if d == 1:
            return (1,1)
        elif d == 2:
            return (2,2)
        elif d == 3:
            return (2,1)
        else:  # d ==4
            return (1,2)
    half = 1 << (n - 1)
    block_size = half * half
    if d <= block_size:
        # top-left quadrant
        return get_pos(n - 1, d)
    elif d <= 2 * block_size:
        # bottom-right quadrant
        x, y = get_pos(n - 1, d - block_size)
        return (x + half, y + half)
    elif d <= 3 * block_size:
        # bottom-left quadrant
        x, y = get_pos(n - 1, d - 2 * block_size)
        return (x + half, y)
    else:
        # top-right quadrant
        x, y = get_pos(n - 1, d - 3 * block_size)
        return (x, y + half)

t = int(input())
for _ in range(t):
    n = int(input())
    q = int(input())
    for __ in range(q):
        line = input().split()
        if line[0] == '->':
            x, y = int(line[1]), int(line[2])
            print(get_val(n, x, y))
        else:
            d = int(line[1])
            x, y = get_pos(n, d)
            print(x, y)