def main():
    import sys
    data = sys.stdin.read().strip().split()
    A, B = map(int, data)
    S = A + B
    print(S * S)

if __name__ == "__main__":
    main()