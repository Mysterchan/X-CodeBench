def can_hold_k_contests(writers, k):
    total_div1 = 0
    total_div2 = 0
    
    for a, b, c in writers:
        max_div1 = min(a, b)
        max_div2 = min(b, c)
        
        # We want to maximize contributions while respecting x + y <= b
        # Greedy: try to give as much as possible to both
        if max_div1 + max_div2 <= b:
            total_div1 += max_div1
            total_div2 += max_div2
        else:
            # Need to split b between div1 and div2
            # To maximize minimum, we can give equal or prioritize the one that needs more
            # But we want both >= k eventually, so maximize both as much as possible
            total_div1 += max_div1
            total_div2 += max_div2
            excess = max_div1 + max_div2 - b
            # Remove excess proportionally or from the one with more
            if max_div1 >= max_div2:
                remove_from_div1 = min(excess, max_div1 - max(0, b - max_div2))
                total_div1 -= remove_from_div1
                total_div2 -= (excess - remove_from_div1)
            else:
                remove_from_div2 = min(excess, max_div2 - max(0, b - max_div1))
                total_div2 -= remove_from_div2
                total_div1 -= (excess - remove_from_div2)
    
    return total_div1 >= k and total_div2 >= k

def solve(writers):
    left, right = 0, 10**18
    
    while left < right:
        mid = (left + right + 1) // 2
        if can_hold_k_contests(writers, mid):
            left = mid
        else:
            right = mid - 1
    
    return left

T = int(input())
for _ in range(T):
    N = int(input())
    writers = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        writers.append((a, b, c))
    
    print(solve(writers))