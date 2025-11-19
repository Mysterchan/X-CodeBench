def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    max_score = 0
    
    # Try all possible subsequences using bitmask
    for mask in range(1, 1 << n):
        subseq = []
        for i in range(n):
            if mask & (1 << i):
                subseq.append(a[i])
        
        # Calculate average
        avg = sum(subseq) / len(subseq)
        
        # Calculate score
        score = sum(1 for x in subseq if x > avg)
        
        max_score = max(max_score, score)
    
    return max_score

t = int(input())
for _ in range(t):
    print(solve())