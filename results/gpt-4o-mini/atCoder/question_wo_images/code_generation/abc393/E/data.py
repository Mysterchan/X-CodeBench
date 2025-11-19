import sys
from math import gcd
from collections import defaultdict

input = sys.stdin.read

def max_gcd_for_each_element(N, K, A):
    max_count = max(A)
    count = [0] * (max_count + 1)
    
    # Count occurrences of each number in A
    for num in A:
        count[num] += 1

    # Prepare to find maximum GCD for each possible GCD
    possible_gcd = [0] * (max_count + 1)

    # Going backwards to find maximum GCDs
    for g in range(max_count, 0, -1):
        multiples = 0
        for multiple in range(g, max_count + 1, g):
            multiples += count[multiple]
        
        # We can take at most K elements
        if multiples >= K:
            possible_gcd[g] = g

    # Generate the results for each element in A
    results = []
    for i in range(N):
        a_i = A[i]
        
        # We need to check downwards for the largest GCD that includes A[i]
        g = a_i
        while g <= max_count:
            if possible_gcd[g] != 0:
                results.append(possible_gcd[g])
                break
            g += a_i

    return results

def main():
    data = input().split()
    N, K = int(data[0]), int(data[1])
    A = list(map(int, data[2:]))
    
    results = max_gcd_for_each_element(N, K, A)
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()