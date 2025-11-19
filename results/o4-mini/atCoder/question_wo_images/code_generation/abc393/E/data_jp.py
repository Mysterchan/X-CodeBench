import sys
import threading
def main():
    import sys
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    try:
        n = int(next(it))
    except StopIteration:
        return
    K = int(next(it))
    A = [0]*n
    M = 0
    for i in range(n):
        v = int(next(it))
        A[i] = v
        if v > M: M = v
    freq = [0] * (M+1)
    for v in A:
        freq[v] += 1
    cnt = [0] * (M+1)
    # compute count of multiples
    mfreq = freq
    mcnt = cnt
    mM = M
    for d in range(1, mM+1):
        s = 0
        # sum freq[d], freq[2d], ...
        for j in range(d, mM+1, d):
            s += mfreq[j]
        mcnt[d] = s
    # compute ans_val for each x up to M
    ans_val = [0] * (M+1)
    mans = ans_val
    for d in range(1, mM+1):
        if mcnt[d] >= K:
            for j in range(d, mM+1, d):
                # since d increasing, overwrite with larger d
                mans[j] = d
    # output per A[i]
    out = sys.stdout.write
    CH = 50000
    i = 0
    nA = n
    while i < nA:
        j = i + CH
        if j > nA: j = nA
        # build chunk
        chunk = []
        for k in range(i, j):
            chunk.append(str(mans[A[k]]))
        out("\n".join(chunk))
        out("\n")
        i = j

if __name__ == "__main__":
    main()