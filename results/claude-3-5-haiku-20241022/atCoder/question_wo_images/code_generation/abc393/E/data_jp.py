import math
from collections import defaultdict

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    max_val = max(A)
    
    # For each divisor d, count how many elements are divisible by d
    divisor_count = [0] * (max_val + 1)
    for a in A:
        d = 1
        while d * d <= a:
            if a % d == 0:
                divisor_count[d] += 1
                if d * d != a:
                    divisor_count[a // d] += 1
            d += 1
    
    # For each element A[i], find the maximum GCD
    results = []
    for i in range(N):
        ai = A[i]
        best_gcd = 1
        
        # Check all divisors of A[i]
        d = 1
        divisors = []
        while d * d <= ai:
            if ai % d == 0:
                divisors.append(d)
                if d * d != ai:
                    divisors.append(ai // d)
            d += 1
        
        # Sort divisors in descending order to find the maximum GCD first
        divisors.sort(reverse=True)
        
        for div in divisors:
            # Count how many elements in A are divisible by div
            count = divisor_count[div]
            
            # We need at least K elements divisible by div
            if count >= K:
                best_gcd = div
                break
        
        results.append(best_gcd)
    
    for res in results:
        print(res)

solve()