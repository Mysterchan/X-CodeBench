def main():
    import sys
    A = list(map(int, sys.stdin.read().split()))
    a, b, c = A
    if a * b == c or a * c == b or b * c == a:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()