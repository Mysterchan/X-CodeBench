import sys
input = sys.stdin.buffer.readline

def solve_case(n, m, A, B):
    A.sort()
    B.sort()
    
    kmax = min((n + m) // 3, n, m)
    if kmax == 0:
        return 0, []

    results = []

    dA = [A[n-1-i] - A[i] for i in range(n // 2)]
    dB = [B[m-1-i] - B[i] for i in range(m // 2)]
    
    prefA = [0] * (len(dA) + 1)
    prefB = [0] * (len(dB) + 1)

    for i in range(len(dA)):
        prefA[i + 1] = prefA[i] + dA[i]
    
    for i in range(len(dB)):
        prefB[i + 1] = prefB[i] + dB[i]

    for k in range(1, kmax + 1):
        t_low = max(0, 2 * k - m)
        t_high = min(k, n - k)
        best = 0
        if t_low <= t_high:
            for t in range(max(t_low, 0), min(t_high, len(dA)) + 1):
                s = k - t
                if s >= 0 and s <= len(dB):
                    best = max(best, prefA[t] + prefB[s])
        results.append(best)

    return kmax, results

def main():
    t = int(input().strip())
    out_lines = []
    for _ in range(t):
        n, m = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        kmax, arr = solve_case(n, m, A, B)
        out_lines.append(str(kmax))
        if kmax > 0:
            out_lines.append(" ".join(map(str, arr)))
    sys.stdout.write("\n".join(out_lines) + "\n")

if __name__ == "__main__":
    main()