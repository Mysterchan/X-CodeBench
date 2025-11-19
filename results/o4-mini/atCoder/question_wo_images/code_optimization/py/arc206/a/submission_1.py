import sys
import threading
def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    A = list(map(int, data[1:]))
    # total occurrences of each value
    total = [0] * (n + 1)
    for v in A:
        total[v] += 1
    # prefix counts as we scan
    pref = [0] * (n + 1)
    ans = 0
    last = n - 1
    for i in range(last):
        v = A[i]
        # always update prefix count for v at this position
        # but if same as previous, skip contribution
        if i > 0 and v == A[i-1]:
            pref[v] += 1
            continue
        # suffix count of v after i
        suf = total[v] - pref[v] - 1
        # positions j>i where A[j]!=v is (last-i) - suf
        ans += (last - i) - suf
        pref[v] += 1
    # plus the original sequence (choosing R=L everywhere)
    print(ans + 1)

if __name__ == "__main__":
    main()