def main():
    import sys
    data = sys.stdin.read().strip().split()
    A, B = map(int, data[:2])
    result = (A + B) ** 2
    print(result)

if __name__ == "__main__":
    main()