def fibonacci(n):
    fib = [0] * (n + 1)
    fib[1] = 1
    fib[2] = 2
    for i in range(3, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib

def can_fit(box, cubes):
    w, l, h = sorted(box)
    return w >= cubes[-1] and l >= cubes[-1] and h >= sum(cubes)

def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    index = 0
    t = int(data[index])
    index += 1
    results = []

    fib_sequence = fibonacci(10)
    
    for _ in range(t):
        n, m = map(int, data[index].split())
        index += 1
        
        cubes = sorted(fib_sequence[1:n + 1])
        result = []
        
        for __ in range(m):
            w, l, h = map(int, data[index].split())
            index += 1
            
            if can_fit((w, l, h), cubes):
                result.append('1')
            else:
                result.append('0')
        
        results.append(''.join(result))

    print('\n'.join(results))

solve()