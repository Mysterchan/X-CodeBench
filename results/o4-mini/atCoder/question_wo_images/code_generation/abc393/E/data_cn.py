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

    # freq[x]: number of times x appears in A
    freq = [0] * (maxA + 1)
    for x in A:
        freq[x] += 1

    # count how many A's are divisible by d
    good = [False] * (maxA + 1)
    for d in range(1, maxA + 1):
        cnt = 0
        # sum freq at multiples of d
        for m in range(d, maxA + 1, d):
            cnt += freq[m]
        if cnt >= K:
            good[d] = True

    # bestDiv[x]: largest d dividing x for which good[d] is True
    bestDiv = [0] * (maxA + 1)
    for d in range(1, maxA + 1):
        if good[d]:
            for m in range(d, maxA + 1, d):
                # since d increases, later assignments overwrite with larger d
                bestDiv[m] = d

    # output answers for each A[i]
    out = sys.stdout
    write = out.write
    # buffer lines in chunks to reduce syscalls
    buf = []
    buf_limit = 50000
    for x in A:
        buf.append(str(bestDiv[x]))
        if len(buf) >= buf_limit:
            write("\n".join(buf))
            write("\n")
            buf.clear()
    if buf:
        write("\n".join(buf))
        write("\n")

if __name__ == "__main__":
    main()