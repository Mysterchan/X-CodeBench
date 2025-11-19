import sys
from collections import defaultdict
from math import factorial

MOD = 998244353

input = sys.stdin.readline

def calculate_combinations(n, counts):
    result = factorial(n)
    for count in counts.values():
        result *= pow(factorial(count), MOD-2, MOD)
        result %= MOD
    return result

def main():
    Q = int(input())
    for _ in range(Q):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))

        groups = defaultdict(list)
        for i in range(N):
            groups[B[i]].append(A[i])

        total_ways = 1
        
        for value in groups.values():
            if not value:
                continue
            color_counts = defaultdict(int)
            for a in value:
                color_counts[a] += 1
            total_ways *= calculate_combinations(len(value), color_counts)
            total_ways %= MOD

        print(total_ways)

main()