import sys

def main():
    X = int(sys.stdin.readline().strip())
    fact = 1
    n = 1
    while fact < X:
        n += 1
        fact *= n
    print(n)

if __name__ == "__main__":
    main()