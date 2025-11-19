def is_fit(cube_sizes, box_dims):
    w, l, h = box_dims
    total_height = sum(cube_sizes)  # Total height required if stacked
    max_width = max(cube_sizes)
    max_length = max(cube_sizes)

    # Check the fit in width, length and height
    return (max_width <= w) and (max_length <= l) and (total_height <= h)

def fibonacci_cubes(n):
    f = [0] * (n + 1)
    f[1], f[2] = 1, 2
    for i in range(3, n + 1):
        f[i] = f[i-1] + f[i-2]
    return f[1:n + 1]  # return only the first n Fibonacci numbers as cube sizes

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n, m = map(int, data[idx].split())
        idx += 1
        
        cube_sizes = fibonacci_cubes(n)
        
        result = []
        for _ in range(m):
            w, l, h = map(int, data[idx].split())
            idx += 1
            
            if is_fit(cube_sizes, (w, l, h)):
                result.append('1')
            else:
                result.append('0')
        
        results.append(''.join(result))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()