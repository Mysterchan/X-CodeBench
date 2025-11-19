import sys
import threading
def main():
    import sys
    data = sys.stdin.buffer.read().split()
    N = int(data[0])
    A = list(map(int, data[1:1+N]))
    C = [0] * (N + 2)
    D = [0] * (N + 3)
    active = 0
    idx = 0
    for i in range(1, N+1):
        active -= D[i]
        in_i = active
        c = A[idx] + in_i
        idx += 1
        C[i] = c
        if c > 0:
            active += 1
            rem_time = i + c + 1
            if rem_time <= N:
                D[rem_time] += 1
    out = []
    for k in range(1, N+1):
        v = C[k] - (N - k)
        if v < 0:
            v = 0
        out.append(str(v))
    sys.stdout.write(" ".join(out))

if __name__ == "__main__":
    main()