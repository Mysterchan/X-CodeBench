import sys
input = sys.stdin.readline

# Precompute Fibonacci cubes sides for n up to 10
# f1=1, f2=2, f_i = f_{i-1} + f_{i-2}
fib = [0, 1, 2]
for i in range(3, 11):
    fib.append(fib[i-1] + fib[i-2])

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    cubes = fib[1:n+1]

    # Total height needed to stack all cubes
    total_height = sum(cubes)

    # The largest cube side (bottom cube)
    max_side = cubes[-1]

    res = []
    for __ in range(m):
        w, l, h = map(int, input().split())
        # Check if cubes can fit in the box:
        # - The base must fit the largest cube (max_side)
        # - The height must be enough to stack all cubes (total_height)
        # Since cubes can be rotated, base is min(w,l) and max(w,l)
        # We only need to check if the largest cube fits in the base (both sides >= max_side)
        # and height >= total_height
        if (w >= max_side and l >= max_side and h >= total_height) or \
           (w >= max_side and h >= max_side and l >= total_height) or \
           (l >= max_side and h >= max_side and w >= total_height):
            res.append('1')
        else:
            res.append('0')
    print(''.join(res))