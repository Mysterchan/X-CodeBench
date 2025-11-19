for _ in range(int(input())):
    n = int(input())
    intervals = []
    for i in range(n):
        l, r = map(int, input().split())
        intervals.append((l, r, i))
    
    ans = [-1] * n
    assigned = [False] * n
    
    for p in reversed(range(n)):
        best = -1
        for i in range(n):
            if assigned[i]:
                continue
            
            # Check if person i can be assigned to seat p+1
            valid = True
            for j in range(n):
                if not assigned[j] and j != i:
                    # Check if L[j] is in the open interval (L[i], R[i])
                    if intervals[i][0] < intervals[j][0] < intervals[i][1]:
                        valid = False
                        break
            
            if valid:
                best = i
                break
        
        if best != -1:
            ans[best] = p + 1
            assigned[best] = True
    
    print(*ans)