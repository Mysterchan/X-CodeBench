def min_longest_bench(n, m, k):
    # Binary search setup
    left, right = 1, max(1, (k + n - 1) // n)  # The maximum bench length can't be more than the number of desks divided by rows
    
    while left < right:
        mid = (left + right) // 2
        
        # Calculate how many desks we can accommodate if the longest bench length is `mid`
        num_desks = 0
        for row in range(n):
            num_desks += mid * (m // (mid + 1)) + min(mid, m % (mid + 1))
        
        if num_desks >= k:
            right = mid
        else:
            left = mid + 1
            
    return left

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        k = int(data[index + 2])
        index += 3
        
        result = min_longest_bench(n, m, k)
        results.append(result)
    
    print('\n'.join(map(str, results)))

if __name__ == '__main__':
    main()