def solve(N, A, B):
    A = [int(x) for x in A]
    B = [int(x) for x in B]
    
    # Get positions of pieces and targets
    pieces = [i for i in range(N) if A[i] == 1]
    targets = [i for i in range(N) if B[i] == 1]
    
    # Check if same number of pieces and targets
    if len(pieces) != len(targets):
        return -1
    
    if len(pieces) == 0:
        return 0
    
    # The minimum operations is the maximum distance any piece needs to travel
    # with optimal assignment (which is just matching sorted positions)
    max_dist = 0
    for i in range(len(pieces)):
        max_dist = max(max_dist, abs(pieces[i] - targets[i]))
    
    return max_dist

T = int(input())
for _ in range(T):
    N = int(input())
    A = input().strip()
    B = input().strip()
    result = solve(N, A, B)
    print(result)