def fibonacci(n):
    fib = [0] * (n + 1)
    fib[1] = 1
    fib[2] = 2
    for i in range(3, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib

def can_fit(cubes, box):
    w, l, h = box
    # Check if the cubes can fit in the box dimensions
    if (cubes[-1] <= w and cubes[-1] <= l and sum(cubes) <= h):
        return True
    return False

def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    # Precompute Fibonacci numbers up to f_10
    fib = fibonacci(10)
    
    for _ in range(t):
        n, m = map(int, data[index].split())
        index += 1
        
        cubes = sorted(fib[1:n + 1])  # Get the first n Fibonacci numbers
        result = []
        
        for _ in range(m):
            w, l, h = map(int, data[index].split())
            index += 1
            
            # Check if cubes can fit in the box
            if can_fit(cubes, (w, l, h)):
                result.append('1')
            else:
                result.append('0')
        
        results.append(''.join(result))
    
    print('\n'.join(results))

solve()