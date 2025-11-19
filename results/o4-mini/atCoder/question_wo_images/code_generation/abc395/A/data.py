def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:]))

    for i in range(n - 1):
        if a[i] >= a[i + 1]:
            print("No")
            return
    print("Yes")

if __name__ == "__main__":
    main()