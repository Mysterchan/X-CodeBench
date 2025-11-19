def fibonacci_numbers(n):
    fib = [0] * (n + 1)
    fib[1], fib[2] = 1, 2
    for i in range(3, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib

def can_fit(cube_sizes, box_dimensions):
    box_w, box_l, box_h = box_dimensions
    total_h = 0
    for size in cube_sizes:
        if size > box_w or size > box_l:
            return False
        total_h += size
    return total_h <= box_h

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    idx = 0
    t = int(data[idx])
    idx += 1

    # Prepare Fibonacci numbers for the maximum n = 10
    fib = fibonacci_numbers(10)
    
    results = []
    
    for _ in range(t):
        n, m = map(int, data[idx].split())
        idx += 1
        
        # Get sizes of the cubes which are the first n Fibonacci numbers
        cube_sizes = fib[1:n + 1]

        result = []
        for __ in range(m):
            w, l, h = map(int, data[idx].split())
            idx += 1
            
            if can_fit(cube_sizes, (w, l, h)):
                result.append('1')
            else:
                result.append('0')
        
        results.append(''.join(result))
    
    print('\n'.join(results))

main()