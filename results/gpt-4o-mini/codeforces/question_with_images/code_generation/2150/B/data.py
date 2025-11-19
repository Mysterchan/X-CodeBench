def count_valid_grids(test_cases):
    MOD = 998244353
    results = []

    for n, a in test_cases:
        rows = [0] * (n + 1)
        cols = [0] * (n + 1)

        # Check if sum of a matches n
        if sum(a) != n:
            results.append(0)
            continue
        
        # Count valid maximum occurrences
        for i in range(1, n + 1):
            if a[i - 1] > 0:
                rows[i] += 1
                cols[i] += 1
        
        filled_rows = sum(1 for count in a if count > 0)
        
        # We need to ensure the number of filled rows equals the number of distinct max positions
        if filled_rows > n:
            results.append(0)
            continue
        
        # Calculate the factorial of the number of arrangements
        arrangements = 1
        available_cells = n  # Total available positions to fill

        for k in range(1, n + 1):
            if a[k - 1] > 0:
                arrangements *= factorial(a[k - 1])
                arrangements %= MOD
                available_cells -= a[k - 1]

        # Calculate permutation of rows occupied by the counts
        arrangements *= factorial(filled_rows)
        arrangements %= MOD

        # Check for the uniqueness of arrangements based on counts
        if filled_rows < n:
            arrangements = (arrangements * pow(factorial(available_cells), MOD - 2, MOD)) % MOD
            
        results.append(arrangements)

    return results

def factorial(num):
    result = 1
    for i in range(2, num + 1):
        result = (result * i) % 998244353
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    test_cases = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index+n]))
        index += n
        test_cases.append((n, a))
    
    results = count_valid_grids(test_cases)
    
    for result in results:
        print(result)