import bisect

def ril():
    return map(int, input().split())

T = int(input())

for _ in range(T):
    n, M = ril()
    a = list(ril())
    b = list(ril())
    
    # Quick check for answer = 0
    a.sort()
    b.sort()
    
    # Check if we can make all sums = 0 (mod M)
    can_zero = True
    b_copy = b[:]
    for x in a:
        target = (M - x) % M
        idx = bisect.bisect_left(b_copy, target)
        if idx < len(b_copy) and b_copy[idx] == target:
            b_copy.pop(idx)
        else:
            can_zero = False
            break
    
    if can_zero:
        print(0)
        continue
    
    # Binary search on answer
    def can_achieve(threshold):
        # For each a[i], find valid positions in b
        # b[j] is valid if (a[i] + b[j]) % M <= threshold
        used = [False] * n
        
        for i in range(n):
            # Try to find an unused b[j] for a[i]
            found = False
            for j in range(n):
                if not used[j]:
                    val = (a[i] + b[j]) % M
                    if val <= threshold:
                        used[j] = True
                        found = True
                        break
            if not found:
                return False
        return True
    
    left, right = 1, M - 1
    
    while left < right:
        mid = (left + right) // 2
        if can_achieve(mid):
            right = mid
        else:
            left = mid + 1
    
    print(left)