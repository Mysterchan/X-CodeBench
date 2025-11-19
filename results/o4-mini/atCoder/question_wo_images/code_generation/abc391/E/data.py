import sys
import threading

def main():
    import sys
    from array import array

    data = sys.stdin.read().split()
    N = int(data[0])
    # Read bits, possibly separated or not
    bits = ''.join(data[1:])
    L = 3 ** N

    # Initialize dp arrays: dp0[i] = cost to make leaf i be 0, dp1[i] for 1
    dp0 = array('I', [0]) * L
    dp1 = array('I', [0]) * L
    for i, ch in enumerate(bits):
        if ch == '0':
            dp0[i] = 0
            dp1[i] = 1
        else:
            dp0[i] = 1
            dp1[i] = 0

    length = L
    # Bottom-up DP: each round reduces length by factor 3
    for _ in range(N):
        new_len = length // 3
        ndp0 = array('I', [0]) * new_len
        ndp1 = array('I', [0]) * new_len

        # Local references for speed
        old0 = dp0
        old1 = dp1

        for k in range(new_len):
            i = 3 * k
            # Sum costs to force all three children to 0
            s0 = old0[i] + old0[i+1] + old0[i+2]
            # Deltas if we flip one child to 1 instead
            d0_0 = old1[i]   - old0[i]
            d0_1 = old1[i+1] - old0[i+1]
            d0_2 = old1[i+2] - old0[i+2]
            min_d0 = d0_0 if d0_0 < d0_1 else d0_1
            if d0_2 < min_d0:
                min_d0 = d0_2
            # Best cost for node=0: either all zeros, or one child=1 (if cheaper)
            c0 = s0 + (min_d0 if min_d0 < 0 else 0)
            ndp0[k] = c0

            # Sum costs to force all three children to 1
            s1 = old1[i] + old1[i+1] + old1[i+2]
            # Deltas if we flip one child to 0 instead
            d1_0 = old0[i]   - old1[i]
            d1_1 = old0[i+1] - old1[i+1]
            d1_2 = old0[i+2] - old1[i+2]
            min_d1 = d1_0 if d1_0 < d1_1 else d1_1
            if d1_2 < min_d1:
                min_d1 = d1_2
            # Best cost for node=1: either all ones, or one child=0 (if cheaper)
            c1 = s1 + (min_d1 if min_d1 < 0 else 0)
            ndp1[k] = c1

        dp0, dp1 = ndp0, ndp1
        length = new_len

    # At the root, dp0[0] is cost to get final=0, dp1[0] for final=1.
    # Determine original final value: it costs zero to keep it as is.
    if dp0[0] == 0:
        # original is 0, to flip needs dp1
        print(dp1[0])
    else:
        # original is 1, to flip needs dp0
        print(dp0[0])

if __name__ == "__main__":
    main()