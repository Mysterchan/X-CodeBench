import sys
input = sys.stdin.readline

# Precompute Fibonacci cubes f_i for i=1..10
# f_1=1, f_2=2, f_i=f_{i-1}+f_{i-2}
fib = [0]*11
fib[1] = 1
fib[2] = 2
for i in range(3, 11):
    fib[i] = fib[i-1] + fib[i-2]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    cubes = fib[1:n+1]

    # Total volume of all cubes
    total_volume = sum(c**3 for c in cubes)

    # Max cube side (largest cube)
    max_side = cubes[-1]

    # For each box, check if all cubes fit
    # Conditions:
    # 1) Box height >= sum of cube heights (stacked)
    # 2) Box base can fit largest cube (width and length >= max_side)
    # 3) Box volume >= total_volume

    # Since cubes must be stacked with largest at bottom,
    # height needed = sum of all cube sides
    height_needed = sum(cubes)

    res = []
    for __ in range(m):
        w, l, h = map(int, input().split())
        # Check if box can fit largest cube on base
        if (w >= max_side and l >= max_side) or (w >= max_side and h >= max_side) or (l >= max_side and h >= max_side):
            # We can orient box so base fits largest cube
            # Now check if height dimension can hold sum of cubes
            # The height dimension is the dimension not used for base
            # So we try all 3 orientations and check if any fits:
            # Orientations: base sides and height side permutations
            fits = False
            dims = [w, l, h]
            # Try all permutations of base and height
            # base = dims[i], dims[j], height = dims[k]
            from itertools import permutations
            for base_w, base_l, height in permutations(dims, 3):
                if base_w >= max_side and base_l >= max_side and height >= height_needed:
                    # Check volume
                    if w*l*h >= total_volume:
                        fits = True
                        break
            res.append('1' if fits else '0')
        else:
            res.append('0')
    print(''.join(res))