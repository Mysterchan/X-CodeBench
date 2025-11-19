import sys
import threading

def main():
    import sys

    data = sys.stdin.read().split()
    N = int(data[0])
    A = [0] + list(map(int, data[1:]))

    # D is a difference array: D[i] will contribute to the current number of active adults with stones
    # at time i via a running prefix sum 'curr'.
    # We only need indices up to N+1.
    D = [0] * (N + 3)

    curr = 0  # current in_j, i.e., number of gifts received from earlier adults
    S = [0] * (N + 1)  # S[j] = A[j] + in_j

    for j in range(1, N + 1):
        curr += D[j]
        in_j = curr
        s = A[j] + in_j
        S[j] = s

        # This alien j can give one stone to each future adult up to when he runs out:
        # he gives at times t = j+1, j+2, ..., j+s (clamped to N).
        end = j + s
        if end > N:
            end = N
        if j + 1 <= end:
            D[j + 1]     += 1
            D[end + 1]   -= 1

    # Compute the final stones B_j:
    # He gives min(S[j], N-j) stones in total after becoming adult,
    # so B_j = S[j] - min(S[j], N-j) = max(S[j] - (N-j), 0).
    out = []
    for j in range(1, N + 1):
        rem = S[j] - (N - j)
        if rem < 0:
            rem = 0
        out.append(str(rem))

    sys.stdout.write(" ".join(out))

if __name__ == "__main__":
    main()