import sys
import threading

def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    S = input().rstrip()

    # Collect positions of '1's (0-based)
    ones = [i for i, ch in enumerate(S) if ch == '1']
    k = len(ones)

    # Build adjusted positions a[i] = ones[i] - i
    a = [ones[i] - i for i in range(k)]

    # Median of a (non-decreasing), choose a[k//2]
    m = a[k // 2]

    # Sum of absolute deviations
    ans = 0
    for v in a:
        ans += abs(v - m)

    print(ans)

if __name__ == "__main__":
    main()