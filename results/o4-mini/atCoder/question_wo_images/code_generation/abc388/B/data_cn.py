import sys

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    N = int(next(it))
    D = int(next(it))
    
    T = [0]*N
    L = [0]*N
    for i in range(N):
        T[i] = int(next(it))
        L[i] = int(next(it))

    out_lines = []
    for k in range(1, D+1):
        max_weight = 0
        for i in range(N):
            weight = T[i] * (L[i] + k)
            if weight > max_weight:
                max_weight = weight
        out_lines.append(str(max_weight))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()