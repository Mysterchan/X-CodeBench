import sys

def main():
    data = sys.stdin.read().split()
    n, d = map(int, data[:2])
    nums = list(map(int, data[2:]))
    T = nums[0::2]
    L = nums[1::2]

    out = []
    for k in range(1, d + 1):
        max_w = 0
        for i in range(n):
            w = T[i] * (L[i] + k)
            if w > max_w:
                max_w = w
        out.append(str(max_w))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()