import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    S = list(map(int, input().split()))
    if n < 3:
        print(0)
        return

    max_val = max(S)
    present = [False] * (max_val + 1)
    for x in S:
        present[x] = True

    S.sort()
    total_count = 0

    # For each B, check possible A and C with equal difference d
    # Since A < B < C and B - A = C - B => C = 2*B - A
    # We iterate over A < B and check if C exists.
    # This is O(N^2) worst case, but we optimize by limiting the search.

    # To optimize, for each B, we only check A in S with A < B,
    # and check if C = 2*B - A <= max_val and present.

    # Since N can be up to 10^6, O(N^2) is too large.
    # Instead, we use a two-pointer approach:
    # For each B, we iterate over A in S with A < B,
    # but we can do this efficiently by iterating over all pairs (A,B)
    # and checking if C exists.

    # We'll iterate over all pairs (A,B) with A < B,
    # and check if C = 2*B - A exists.
    # To avoid O(N^2), we use the fact that S is sorted and use binary search.

    # But binary search for each pair is O(N^2 log N), still too large.

    # Instead, we use a hash set for O(1) lookup and iterate over all pairs (A,B)
    # with A < B, but we limit the pairs by using a sliding window approach.

    # Since the problem is equivalent to counting arithmetic progressions of length 3,
    # we can use a method similar to:
    # For each element B, count the number of pairs (A,C) such that A + C = 2*B.

    # We can do this by iterating over all B and for each B,
    # iterate over A in S with A < B, check if C = 2*B - A exists.

    # This is O(N^2) worst case, but we can optimize by using a dictionary to map values to indices,
    # and for each B, iterate over A in S with A < B, but break early if difference too large.

    # Since the original FFT approach is complex and slow in Python,
    # we implement a more efficient approach using a dictionary and two pointers.

    # Implementation:
    # For each B in S:
    #   For each A in S with A < B:
    #       C = 2*B - A
    #       If C in present and C > B:
    #           count++

    # To optimize, we can fix B and iterate A from start to B-1,
    # but this is still O(N^2).

    # Since constraints are large, we implement the FFT approach in a faster way using numpy.

    # But since external libraries are not allowed, we implement a faster approach:

    # Use a frequency array and convolution via built-in complex FFT from Python's cmath.

    # We'll implement a faster FFT using numpy if allowed, but since not allowed,
    # we implement a faster approach using a frequency array and a single pass.

    # Since the problem is counting arithmetic progressions of length 3,
    # we can use the formula:
    # Number of triplets = sum over all B of number of pairs (A,C) with A + C = 2*B.

    # We can precompute frequency array freq[x] = 1 if x in S else 0.

    # Then, convolution freq * freq gives number of pairs (A,C) with sum = k.

    # For each B, number of pairs (A,C) with sum = 2*B is convolution[2*B].

    # Since (B,B) pair is counted, subtract 1 and divide by 2.

    # Implementing FFT from scratch is slow in Python, so we optimize the original code:

    # Optimized FFT implementation with preallocation and avoiding repeated list creations.

    import math
    import cmath

    def fft(a, invert):
        n = len(a)
        j = 0
        for i in range(1, n):
            bit = n >> 1
            while j & bit:
                j ^= bit
                bit >>= 1
            j |= bit
            if i < j:
                a[i], a[j] = a[j], a[i]

        length = 2
        while length <= n:
            angle = 2 * math.pi / length * (-1 if invert else 1)
            wlen = complex(math.cos(angle), math.sin(angle))
            for i in range(0, n, length):
                w = 1+0j
                half = length >> 1
                for j in range(i, i + half):
                    u = a[j]
                    v = a[j + half] * w
                    a[j] = u + v
                    a[j + half] = u - v
                    w *= wlen
            length <<= 1

        if invert:
            for i in range(n):
                a[i] /= n

    size = 1
    while size < 2 * max_val + 1:
        size <<= 1

    freq = [0.0] * size
    for x in S:
        freq[x] = 1.0

    fa = list(map(complex, freq))
    fft(fa, False)
    for i in range(size):
        fa[i] *= fa[i]
    fft(fa, True)

    # Round the real parts to nearest integer
    conv = [int(round(fa[i].real)) for i in range(size)]

    total_count = 0
    for B in S:
        val = conv[2 * B]
        # subtract the pair (B,B) counted once
        if val > 0:
            total_count += (val - 1) // 2

    print(total_count)

if __name__ == '__main__':
    main()