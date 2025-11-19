import math
from collections import defaultdict

def get_divisors(n):
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        i += 1
    return sorted(divisors, reverse=True)

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    # For each divisor, store indices where A[i] is divisible by it
    divisor_to_indices = defaultdict(list)
    
    max_val = max(A)
    
    # For each element, find all its divisors and record
    for i in range(N):
        divisors = get_divisors(A[i])
        for d in divisors:
            divisor_to_indices[d].append(i)
    
    results = []
    
    for i in range(N):
        # Get divisors of A[i] in descending order
        divisors = get_divisors(A[i])
        
        answer = 1
        for d in divisors:
            # Check if there are at least K elements divisible by d
            if len(divisor_to_indices[d]) >= K:
                # Check if A[i] is included in those elements
                if i in divisor_to_indices[d]:
                    answer = d
                    break
        
        results.append(answer)
    
    for r in results:
        print(r)

solve()