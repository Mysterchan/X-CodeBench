import sys
input = sys.stdin.buffer.readline

def solve_case(n, m, A, B):
    A.sort()
    B.sort()
    max_pairs_A = n // 2
    max_pairs_B = m // 2
    dA = [0] * max_pairs_A
    for i in range(max_pairs_A):
        dA[i] = A[n-1-i] - A[i]
    dB = [0] * max_pairs_B
    for i in range(max_pairs_B):
        dB[i] = B[m-1-i] - B[i]
    prefA = [0] * (max_pairs_A + 1)
    for i in range(max_pairs_A):
        prefA[i+1] = prefA[i] + dA[i]
    prefB = [0] * (max_pairs_B + 1)
    for i in range(max_pairs_B):
        prefB[i+1] = prefB[i] + dB[i]

    kmax = min((n + m) // 3, n, m)
    if kmax == 0:
        return 0, []

    res = []
    # Instead of checking all t in range, we find the best t by checking boundaries only
    # Because prefA and prefB are prefix sums of sorted differences, the function val = prefA[t] + prefB[k - t]
    # is unimodal or piecewise linear, so max is at boundary of t_low and t_high or near them.
    for k in range(1, kmax + 1):
        t_low = max(0, 2*k - m)
        t_high = min(k, n - k)
        best = 0
        if t_low <= t_high:
            # Clamp to max_pairs_A and max_pairs_B
            lo = max(t_low, 0)
            hi = min(t_high, max_pairs_A)
            if lo <= hi:
                # Check only lo and hi, and possibly lo+1 and hi-1 if in range, to find max quickly
                candidates = [lo, hi]
                if lo + 1 <= hi:
                    candidates.append(lo + 1)
                if hi - 1 >= lo:
                    candidates.append(hi - 1)
                candidates = [t for t in candidates if 0 <= t <= max_pairs_A]
                for t in candidates:
                    s = k - t
                    if 0 <= s <= max_pairs_B:
                        val = prefA[t] + prefB[s]
                        if val > best:
                            best = val
        res.append(best)
    return kmax, res

def main():
    t = int(input())
    out_lines = []
    for _ in range(t):
        n, m = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        kmax, arr = solve_case(n, m, A, B)
        out_lines.append(str(kmax))
        if kmax > 0:
            out_lines.append(" ".join(str(x) for x in arr))
    print("\n".join(out_lines))

if __name__ == "__main__":
    main()