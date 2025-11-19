import sys
import math

input = sys.stdin.readline

def min_steps(x, y):
    # We want to find the minimum n such that:
    # sum of odd steps (x-axis) = x
    # sum of even steps (y-axis) = y
    # steps strictly increasing positive integers
    #
    # Steps: s1 < s2 < s3 < ... < sn
    # s1 + s3 + s5 + ... = x
    # s2 + s4 + s6 + ... = y
    #
    # Number of x-steps = (n+1)//2
    # Number of y-steps = n//2
    #
    # The minimal sum of first k integers is k(k+1)/2
    # The sum of all steps is n(n+1)/2
    #
    # We want to find the minimal n such that:
    # There exists a strictly increasing sequence s1 < s2 < ... < sn
    # with s1 + s3 + ... = x and s2 + s4 + ... = y
    #
    # Key observations:
    # - The steps are strictly increasing positive integers.
    # - The sum of all steps is x + y.
    # - The minimal sum of first n integers is n(n+1)/2.
    # So n(n+1)/2 <= x + y must hold.
    #
    # Also, the sum of odd-indexed steps is x, sum of even-indexed steps is y.
    # The minimal sum of k odd steps (positions 1,3,5...) is at least k^2
    # because the smallest k odd numbers are 1,3,5,...,2k-1 and their sum is k^2.
    # Similarly, the minimal sum of k even steps (positions 2,4,6...) is at least k(k+1)
    # because the smallest k even numbers are 2,4,6,...,2k and their sum is k(k+1).
    #
    # So for n steps:
    # x >= ((n+1)//2)^2
    # y >= (n//2)*(n//2 + 1)
    #
    # If these conditions are not met, return -1.
    #
    # Otherwise, find minimal n satisfying:
    # n(n+1)/2 >= x + y
    # x >= ((n+1)//2)^2
    # y >= (n//2)*(n//2 + 1)
    #
    # We'll try increasing n from 1 upwards until conditions met or impossible.

    total = x + y

    # Binary search for minimal n such that n(n+1)/2 >= total
    left, right = 1, 2 * 10**5  # upper bound large enough for constraints
    while left < right:
        mid = (left + right) // 2
        if mid * (mid + 1) // 2 >= total:
            right = mid
        else:
            left = mid + 1
    n = left

    # Check if conditions on x and y sums hold for this n or larger n
    # If not, try increasing n until conditions hold or n too large
    while True:
        kx = (n + 1) // 2  # number of x steps
        ky = n // 2        # number of y steps
        min_x = kx * kx
        min_y = ky * (ky + 1)
        if x >= min_x and y >= min_y:
            return n
        n += 1
        if n > 2 * 10**5:
            return -1

def main():
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        print(min_steps(x, y))

if __name__ == "__main__":
    main()