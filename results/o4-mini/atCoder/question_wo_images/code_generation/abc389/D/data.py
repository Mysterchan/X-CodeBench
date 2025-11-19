import sys
import threading

def main():
    import sys
    from math import isqrt

    data = sys.stdin.read().strip().split()
    if not data:
        return
    R = int(data[0])

    # We count integer (i, j) so that max corner distance squared:
    #   (|i|+0.5)^2 + (|j|+0.5)^2 <= R^2.
    # Equivalently, (2i+1)^2 + (2j+1)^2 <= 4 R^2.
    #
    # We iterate i = 0,1,2,... and maintain a pointer j >= 0 such that
    # for each i, j is the maximum j >= 0 satisfying (2i+1)^2 + (2j+1)^2 <= 4 R^2.
    # Because as i increases, j never increases, we can slide j down from its
    # starting value for i=0.  This costs O(R) time total.
    #
    # After counting how many (i,j) in the first quadrant (i>=0, j>=0) satisfy
    # the condition, call that sum S.  Let
    #   B = number of i>0 with j>=0  (these are the "axis" squares on the x-axis),
    #   D = number of j>0 when i=0    (those on the y-axis),
    #   C0 = 1  if (i=0,j=0) is counted (it is, for R>=1).
    # Then the total number of squares in all four quadrants is
    #   4*A + 2*(B+D) + C0,
    # where A = S - (B+D+ C0).  Simplifying gives:
    #   Total = 4*S - 2*(B + D) - 3*C0,  and here C0 = 1.

    R2 = R * R
    M = 4 * R2

    # Initial j for i = 0: the largest j >= 0 with (2*0+1)^2 + (2j+1)^2 <= M.
    # That means (2j+1)^2 <= M - 1.  Let s0 = floor(sqrt(M-1)), then 2j+1 <= s0,
    # so j <= (s0 - 1)//2.
    # We only do this sqrt once.
    if M - 1 >= 0:
        s0 = isqrt(M - 1)
        j = (s0 - 1) // 2
    else:
        # If M < 1, no squares fit, but R>=1 in constraints so we won't hit this.
        j = -1

    S = 0          # total count in first quadrant i>=0,j>=0
    B_count = 0    # count of i>0 with j>=0
    D = 0          # j_max at i=0

    i = 0
    # Slide j down as needed for each i
    while j >= 0:
        # A = (2i+1)^2
        a = (2*i + 1)
        A = a * a
        # Decrease j while the inequality fails
        #    A + (2j+1)^2 <= M
        # If j falls below 0, no more valid j for larger i.
        while j >= 0:
            b = (2*j + 1)
            if A + b*b <= M:
                break
            j -= 1
        if j < 0:
            break

        # Now j is j_max for this i
        if i == 0:
            D = j
        else:
            B_count += 1

        S += (j + 1)
        i += 1

    # C0 = 1 since (i=0,j=0) is valid for R>=1
    C0 = 1
    # Total squares in all four quadrants:
    total = 4*S - 2*(B_count + D) - 3*C0

    sys.stdout.write(str(total))

if __name__ == "__main__":
    main()