import sys
import math

input = sys.stdin.readline

Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# maintain the current LCM of all removed multiples
# to avoid overflow, we stop updating if LCM > 10**18 (large enough)
lcm = 1
MAX_LCM = 10**18

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for A, B in queries:
    g = gcd(lcm, A)
    # update lcm if possible
    if lcm <= MAX_LCM:
        # lcm = lcm * (A // g)
        # check overflow
        mul = A // g
        if lcm <= MAX_LCM // mul:
            lcm = lcm * mul
        else:
            lcm = MAX_LCM + 1  # mark as overflowed, no need to update further

    # number of removed elements <= x is floor(x / lcm)
    # we want to find x such that:
    # x - floor(x / lcm) = B
    # binary search x
    left, right = B, B * lcm  # upper bound is safe since lcm >= 1
    while left < right:
        mid = (left + right) // 2
        removed = mid // lcm if lcm <= MAX_LCM else 0
        if mid - removed >= B:
            right = mid
        else:
            left = mid + 1
    print(left)