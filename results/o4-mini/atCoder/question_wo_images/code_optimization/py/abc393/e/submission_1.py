import sys
import threading

def main():
    import sys
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    A = [int(next(it)) for _ in range(N)]
    maxA = max(A)

    # frequency of each value
    freq = [0] * (maxA + 1)
    for x in A:
        freq[x] += 1

    # count how many numbers are divisible by d
    cnt = [0] * (maxA + 1)
    for d in range(1, maxA + 1):
        c = 0
        for m in range(d, maxA + 1, d):
            c += freq[m]
        cnt[d] = c

    # best[d] = maximum divisor of d that has cnt[div] >= K
    best = [0] * (maxA + 1)
    for div in range(1, maxA + 1):
        if cnt[div] >= K:
            for m in range(div, maxA + 1, div):
                best[m] = div

    out = sys.stdout.write
    for x in A:
        out(str(best[x]))
        out('\n')

if __name__ == "__main__":
    threading.Thread(target=main).start()