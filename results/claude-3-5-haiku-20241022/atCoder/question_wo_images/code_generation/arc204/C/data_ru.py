def mex(x, y):
    if x == y:
        return 0 if x != 0 else 1
    if (x == 0 and y == 1) or (x == 1 and y == 0):
        return 2
    if (x == 0 and y == 2) or (x == 2 and y == 0):
        return 1
    if (x == 1 and y == 2) or (x == 2 and y == 1):
        return 0
    return 0

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    # Convert to 0-indexed
    p = [x - 1 for x in p]
    
    q = int(input())
    
    for _ in range(q):
        a0, a1, a2 = map(int, input().split())
        
        max_score = 0
        
        # Try all possible assignments
        from itertools import combinations
        
        indices = list(range(n))
        
        # Generate all ways to choose positions for 0s, 1s, and 2s
        for zero_positions in combinations(indices, a0):
            zero_set = set(zero_positions)
            remaining = [i for i in indices if i not in zero_set]
            
            for one_positions in combinations(remaining, a1):
                one_set = set(one_positions)
                two_positions = [i for i in remaining if i not in one_set]
                
                # Build sequence B
                b = [0] * n
                for i in zero_positions:
                    b[i] = 0
                for i in one_positions:
                    b[i] = 1
                for i in two_positions:
                    b[i] = 2
                
                # Calculate score
                score = 0
                for i in range(n):
                    score += mex(b[i], b[p[i]])
                
                max_score = max(max_score, score)
        
        print(max_score)

solve()