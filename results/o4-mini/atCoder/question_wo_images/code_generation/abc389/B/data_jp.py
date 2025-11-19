import sys

def main():
    X = int(sys.stdin.readline().strip())
    p = 1
    for n in range(1, 100):
        p *= n
        if p == X:
            print(n)
            return

if __name__ == "__main__":
    main()