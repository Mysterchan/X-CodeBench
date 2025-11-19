import sys
import threading
def main():
    import sys
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it)); K = int(next(it))
    A = [0]*n
    for i in range(n):
        A[i] = int(next(it))
    maxA = max(A)
    # frequency of each value
    freq = [0] * (maxA + 1)
    for a in A:
        freq[a] += 1
    # cnt[d] = how many A's are divisible by d
    cnt = [0] * (maxA + 1)
    freq_local = freq
    cnt_local = cnt
    MA = maxA
    for d in range(1, MA + 1):
        s = 0
        # sum frequencies of multiples of d
        for m in range(d, MA + 1, d):
            s += freq_local[m]
        cnt_local[d] = s
    # fval[v] = the answer for value v
    fval = [0] * (MA + 1)
    fv = fval
    # count how many distinct values we need to fill
    rem = 0
    for v in range(1, MA + 1):
        if freq_local[v]:
            rem += 1
    Kreq = K
    # assign fval by descending d
    for d in range(MA, 0, -1):
        if cnt_local[d] >= Kreq:
            for m in range(d, MA + 1, d):
                if freq_local[m] and fv[m] == 0:
                    fv[m] = d
                    rem -= 1
                    if rem == 0:
                        break
        if rem == 0:
            break
    # output answers
    out = sys.stdout.write
    for a in A:
        out(str(fv[a]))
        out('\n')

if __name__ == "__main__":
    main()