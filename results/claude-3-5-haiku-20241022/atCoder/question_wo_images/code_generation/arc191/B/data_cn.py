def solve():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        
        # Find compatible numbers
        # X is compatible if X XOR N == X % N
        # X % N is in range [0, N-1]
        # So we need X XOR N to be in range [0, N-1]
        
        compatible = []
        
        # For each possible remainder r (0 to N-1)
        # We need X such that X % N = r and X XOR N = r
        # This means X XOR N = X % N = r
        
        # From X XOR N = r, we get X = r XOR N
        # We need to check if (r XOR N) % N = r
        
        for r in range(N):
            x_candidate = r ^ N
            if x_candidate % N == r:
                compatible.append(x_candidate)
        
        # Compatible numbers form a pattern
        # If x is compatible, then x + N might also be compatible
        # We need to find all base compatible numbers in [0, some range]
        
        # Actually, let's think differently
        # X is compatible if X XOR N == X % N
        # Let X = qN + r where 0 <= r < N
        # Then X % N = r
        # We need X XOR N = r
        # (qN + r) XOR N = r
        
        # For small values, we can iterate and find pattern
        if len(compatible) == 0:
            print(-1)
            continue
        
        # The compatible numbers follow a pattern
        # Base compatible: those in range [N, 2N-1] where x XOR N == x % N
        base_compatible = []
        for r in range(N):
            x = r ^ N
            if x >= N and x < 2 * N and x % N == r:
                base_compatible.append(x)
        
        if len(base_compatible) == 0:
            print(-1)
            continue
        
        # Check if we have enough
        if K > len(base_compatible):
            print(-1)
            continue
        
        base_compatible.sort()
        print(base_compatible[K - 1])

solve()