import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        a.sort(reverse=True)
        total = 0
        for i in range(0, len(a) - (len(a) % 3), 3):
            total += a[i] * a[i+1] * a[i+2]
        print(total)

if __name__ == "__main__":
    main()
