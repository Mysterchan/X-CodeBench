import bisect

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    
    for _ in range(Q):
        L, R = map(int, input().split())
        L -= 1  # Convert to 0-indexed
        
        mochi = A[L:R]
        n = len(mochi)
        
        # Binary search on the answer
        left, right = 0, n // 2
        
        while left < right:
            mid = (left + right + 1) // 2
            
            # Check if we can make mid kakamimochi
            # Greedy: try to pair smallest available with smallest valid larger one
            used = [False] * n
            count = 0
            
            for i in range(n):
                if used[i]:
                    continue
                
                # Find smallest j > i such that mochi[i] <= mochi[j] / 2
                target = mochi[i] * 2
                found = False
                
                for j in range(i + 1, n):
                    if not used[j] and mochi[j] >= target:
                        used[i] = True
                        used[j] = True
                        count += 1
                        found = True
                        break
                
                if count >= mid:
                    break
            
            if count >= mid:
                left = mid
            else:
                right = mid - 1
        
        print(left)

solve()