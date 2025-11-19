import sys
import threading

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    # Read the binary string A, ignoring spaces
    A = ''.join(data[1:])
    # Expected length
    M = 3 ** N
    # Initialize DP arrays for leaves
    dp0 = [0] * M
    dp1 = [0] * M
    for i, ch in enumerate(A):
        if ch == '0':
            dp0[i] = 0
            dp1[i] = 1
        else:
            dp0[i] = 1
            dp1[i] = 0

    # Build up layers
    length = M
    for _ in range(N):
        new_len = length // 3
        ndp0 = []
        ndp1 = []
        p0 = dp0
        p1 = dp1
        # Process each group of three
        for j in range(0, length, 3):
            # costs for child 0
            d00 = p0[j];   d01 = p1[j]
            # child 1
            d10 = p0[j+1]; d11 = p1[j+1]
            # child 2
            d20 = p0[j+2]; d21 = p1[j+2]

            # To make node output 0: majority zeros
            s0 = d00 + d10 + d20
            # either all three zero (cost s0), or exactly two zeros + one one:
            # replacing one child's zero-cost by its one-cost
            m0 = s0
            # child 0 is the one that becomes '1'
            c = s0 - d00 + d01
            if c < m0: m0 = c
            # child 1 flips to '1'
            c = s0 - d10 + d11
            if c < m0: m0 = c
            # child 2 flips to '1'
            c = s0 - d20 + d21
            if c < m0: m0 = c

            # To make node output 1: majority ones
            s1 = d01 + d11 + d21
            m1 = s1
            # exactly two ones + one zero:
            c = s1 - d01 + d00
            if c < m1: m1 = c
            c = s1 - d11 + d10
            if c < m1: m1 = c
            c = s1 - d21 + d20
            if c < m1: m1 = c

            ndp0.append(m0)
            ndp1.append(m1)

        # Move up one layer
        dp0 = ndp0
        dp1 = ndp1
        length = new_len

    # At root, dp0[0] is cost to make final 0; dp1[0] for final 1.
    # The original output bit b_orig is the one with zero cost.
    if dp0[0] == 0:
        # original final is 0, so need cost for 1
        print(dp1[0])
    else:
        # original final is 1
        print(dp0[0])

if __name__ == "__main__":
    main()