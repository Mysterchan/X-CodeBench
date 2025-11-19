def solve_query(arr):
    n = len(arr)
    if n < 2:
        return 0
    
    left = 0
    right = n // 2
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if we can make mid kagamimochi
        valid = True
        for i in range(mid):
            if arr[i] * 2 > arr[n - mid + i]:
                valid = False
                break
        
        if valid:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    
    # Extract subarray for this query
    subarray = A[l:r+1]
    
    # Solve for this subarray
    print(solve_query(subarray))