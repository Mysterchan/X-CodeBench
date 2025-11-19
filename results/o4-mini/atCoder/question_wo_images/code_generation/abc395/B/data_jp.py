import sys
def main():
    N = int(sys.stdin.readline().strip())
    for i in range(N):
        line = []
        for j in range(N):
            d0 = min(i, j, N-1-i, N-1-j)
            line.append('#' if d0 % 2 == 0 else '.')
        print(''.join(line))

if __name__ == "__main__":
    main()