import sys
import threading

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    s = data[1]
    b = []
    cnt1 = 0
    # Build the transformed positions b[i] = p[i] - i
    for i, ch in enumerate(s):
        if ch == '1':
            b.append(i - cnt1)
            cnt1 += 1

    # Find the median of b (b is already non-decreasing)
    m = cnt1
    mid = b[m // 2]

    # Compute total moves = sum |b[i] - median|
    ans = 0
    for x in b:
        # Python's abs is fast enough here
        ans += abs(x - mid)

    print(ans)

if __name__ == "__main__":
    main()