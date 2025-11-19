import sys
from array import array

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    # Join all remaining tokens (in case the binary string has spaces)
    A = "".join(data[1:])
    size = len(A)

    # Initialize cost arrays for leaves
    cost0 = array('I', [0]) * size
    cost1 = array('I', [0]) * size
    for i, ch in enumerate(A):
        if ch == '0':
            cost0[i] = 0
            cost1[i] = 1
        else:
            cost0[i] = 1
            cost1[i] = 0

    # Bottom-up DP over the ternary tree
    for _ in range(N):
        new_size = size // 3
        nc0 = array('I', [0]) * new_size
        nc1 = array('I', [0]) * new_size

        c0 = cost0
        c1 = cost1
        for i in range(new_size):
            base = 3 * i
            v0 = c0[base]
            v1 = c0[base + 1]
            v2 = c0[base + 2]
            w0 = c1[base]
            w1 = c1[base + 1]
            w2 = c1[base + 2]

            s0 = v0 + v1 + v2
            s1 = w0 + w1 + w2

            # For making parent = 0, we prefer children = 0
            d0 = v0 - w0
            t = v1 - w1
            if t > d0: d0 = t
            t = v2 - w2
            if t > d0: d0 = t
            if d0 < 0: d0 = 0
            nc0[i] = s0 - d0

            # For making parent = 1, we prefer children = 1
            d1 = w0 - v0
            t = w1 - v1
            if t > d1: d1 = t
            t = w2 - v2
            if t > d1: d1 = t
            if d1 < 0: d1 = 0
            nc1[i] = s1 - d1

        cost0, cost1 = nc0, nc1
        size = new_size

    # At root, one of cost0[0], cost1[0] is zero (the current value);
    # the other is the min flips to change it.
    if cost0[0] == 0:
        print(cost1[0])
    else:
        print(cost0[0])

if __name__ == "__main__":
    main()