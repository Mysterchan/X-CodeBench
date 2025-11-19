import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        for __ in range(n):
            l = int(data[idx])
            r = int(data[idx + 1])
            idx += 2
        print("YES")

if __name__ == "__main__":
    main()