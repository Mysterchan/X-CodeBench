import sys
from math import gcd

def solve():
    N, K = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    
    max_val = max(A)
    
    # Count occurrences of each value
    count = [0] * (max_val + 1)
    for x in A:
        count[x] += 1
    
    # For each potential GCD g, count how many elements are divisible by g
    divisible_count = [0] * (max_val + 1)
    for g in range(max_val, 0, -1):
        for multiple in range(g, max_val + 1, g):
            divisible_count[g] += count[multiple]
    
    # For each element, find divisors and compute max GCD
    results = []
    for a in A:
        if a == 1:
            results.append(1)
            continue
        
        # Find all divisors of a
        divisors = []
        i = 1
        while i * i <= a:
            if a % i == 0:
                divisors.append(i)
                if i != a // i:
                    divisors.append(a // i)
            i += 1
        
        # Sort divisors in descending order to find maximum GCD first
        divisors.sort(reverse=True)
        
        max_gcd = 1
        for d in divisors:
            if divisible_count[d] >= K:
                max_gcd = d
                break
        
        results.append(max_gcd)
    
    for res in results:
        print(res)

solve()