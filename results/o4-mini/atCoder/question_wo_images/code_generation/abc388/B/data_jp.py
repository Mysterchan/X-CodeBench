import sys

def main():
    input_data = sys.stdin.read().split()
    n, d = map(int, input_data[:2])
    t = []
    l = []
    idx = 2
    for _ in range(n):
        ti = int(input_data[idx]); li = int(input_data[idx+1])
        t.append(ti)
        l.append(li)
        idx += 2

    out = []
    for k in range(1, d+1):
        max_weight = 0
        for i in range(n):
            weight = t[i] * (l[i] + k)
            if weight > max_weight:
                max_weight = weight
        out.append(str(max_weight))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()