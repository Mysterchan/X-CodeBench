def solve(n, k, arrs):
    # Precompute the required dimensions of the cubes
    fs = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    required_cubes = [fs[n-1], fs[n-2]]  # We need the largest and second largest

    results = []
    for w, l, h in arrs:
        # Sort dimensions of the box
        box_dimensions = sorted([w, l, h])
        # Check if the cubes can fit
        if (box_dimensions[2] >= required_cubes[0] and 
            box_dimensions[1] >= required_cubes[1]):
            results.append('1')
        else:
            results.append('0')
    
    return ''.join(results)

t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split())
    arrs = [tuple(map(int, input().strip().split())) for _ in range(k)]
    print(solve(n, k, arrs))