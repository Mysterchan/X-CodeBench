import bisect

def lis_length(arr):
    """Find length of longest increasing subsequence using binary search"""
    if not arr:
        return 0
    
    # tails[i] = smallest tail element of all increasing subsequences of length i+1
    tails = []
    
    for num in arr:
        # Find position where num should be inserted
        pos = bisect.bisect_left(tails, num)
        
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    
    return len(tails)

def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    
    for _ in range(q):
        r, x = map(int, input().split())
        
        # Filter elements: first r elements that are <= x
        filtered = [a[i] for i in range(r) if a[i] <= x]
        
        # Find LIS length
        result = lis_length(filtered)
        print(result)

solve()