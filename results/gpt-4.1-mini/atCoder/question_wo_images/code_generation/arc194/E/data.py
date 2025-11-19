def main():
    import sys
    input = sys.stdin.readline

    N, X, Y = map(int, input().split())
    S = input().strip()
    T = input().strip()

    # The operations swap a pattern of length X+Y:
    # Operation A: 0...0 (X times) followed by 1...1 (Y times)
    # changes to: 1...1 (Y times) followed by 0...0 (X times)
    # Operation B: 1...1 (Y times) followed by 0...0 (X times)
    # changes to: 0...0 (X times) followed by 1...1 (Y times)
    #
    # Essentially, these operations swap the two blocks of length X and Y.
    #
    # Key insight:
    # The operations only swap adjacent blocks of zeros and ones of lengths X and Y.
    # So the string can be viewed as a sequence of runs of 0s and 1s.
    #
    # The operations allow swapping adjacent runs of length X and Y if they are
    # in the pattern 0^X 1^Y or 1^Y 0^X.
    #
    # This means the runs of zeros and ones can be rearranged by swapping adjacent runs
    # of lengths X and Y.
    #
    # So the problem reduces to:
    # - Decompose S and T into runs of consecutive 0s and 1s.
    # - Check if the number of runs and their order of bits are the same.
    # - For each run, the length can be changed by swapping blocks of length X and Y,
    #   but only by rearranging these blocks.
    #
    # Actually, the operations swap blocks of length X and Y between runs.
    #
    # Let's analyze the runs:
    #
    # For each run, the length mod (X+Y) is invariant under these operations.
    # Because the operations swap blocks of length X and Y, the total length of runs
    # of zeros and ones remain the same, but the distribution of lengths can change
    # by multiples of (X+Y).
    #
    # Actually, the operations swap blocks of length X and Y between runs,
    # so the sum of lengths of runs of zeros and ones remain the same.
    #
    # But the operations only swap blocks of length X and Y between adjacent runs.
    #
    # Let's try to formalize:
    #
    # The runs of S and T must have the same number of runs and the same bit pattern.
    # Because the operations do not change the order of runs of zeros and ones,
    # only the lengths can be changed by swapping blocks.
    #
    # So first check if the runs of bits (0 or 1) in S and T are the same.
    #
    # Then, for each run, check if the length of the run in S can be transformed into
    # the length of the run in T by swapping blocks of length X and Y.
    #
    # Since the operations swap blocks of length X and Y between adjacent runs,
    # the length of each run can be changed by multiples of (X+Y).
    #
    # But the operations only swap blocks of length X and Y between adjacent runs,
    # so the sum of lengths of runs of the same bit is invariant.
    #
    # Wait, the sum of lengths of runs of zeros and ones is fixed.
    #
    # So the total number of zeros and ones in S and T must be the same.
    #
    # But the problem is more subtle.
    #
    # Let's consider the runs:
    #
    # For example, if we have runs:
    # S: (bit, length) = (0, a1), (1, a2), (0, a3), (1, a4), ...
    # T: (bit, length) = (0, b1), (1, b2), (0, b3), (1, b4), ...
    #
    # The bits must match in order.
    #
    # The operations allow swapping blocks of length X and Y between adjacent runs.
    #
    # So the lengths can be changed by moving blocks of length X and Y between runs.
    #
    # The key is that the difference in length between runs must be divisible by (X+Y).
    #
    # Because swapping blocks of length X and Y moves length X from one run to the other,
    # and length Y from the other run to the first.
    #
    # So the net effect on the length of a run is ±(X - Y).
    #
    # Actually, let's analyze the effect of one operation on the lengths of two adjacent runs:
    #
    # Suppose we have two adjacent runs:
    # run_i: length L_i, bit b_i
    # run_{i+1}: length L_{i+1}, bit b_{i+1} (different bit)
    #
    # Operation A or B swaps blocks of length X and Y between these runs.
    #
    # After operation:
    # run_i length changes by: -X + Y = Y - X
    # run_{i+1} length changes by: -Y + X = X - Y
    #
    # So the difference in length between runs changes by ±(X - Y).
    #
    # By applying these operations multiple times, the lengths of runs can be adjusted
    # by multiples of (X - Y).
    #
    # But since the runs must remain positive length, the lengths must be at least 1.
    #
    # So the problem reduces to:
    # - The runs of bits in S and T must be the same.
    # - For each run, the length difference between S and T must be divisible by gcd(X, Y).
    # - The sum of lengths of runs of the same bit must be the same.
    #
    # Let's implement this logic.
    #
    # Steps:
    # 1. Decompose S and T into runs of (bit, length).
    # 2. Check if the runs have the same bit pattern and same number of runs.
    # 3. For each run, check if length difference is divisible by gcd(X, Y).
    # 4. Check if total length of S and T are equal (given).
    #
    # If all conditions hold, print "Yes", else "No".

    from math import gcd

    def run_length_encoding(s):
        runs = []
        prev = s[0]
        count = 1
        for c in s[1:]:
            if c == prev:
                count += 1
            else:
                runs.append((prev, count))
                prev = c
                count = 1
        runs.append((prev, count))
        return runs

    runs_s = run_length_encoding(S)
    runs_t = run_length_encoding(T)

    if len(runs_s) != len(runs_t):
        print("No")
        return

    g = gcd(X, Y)

    for (bs, ls), (bt, lt) in zip(runs_s, runs_t):
        if bs != bt:
            print("No")
            return
        if (ls - lt) % g != 0:
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    main()