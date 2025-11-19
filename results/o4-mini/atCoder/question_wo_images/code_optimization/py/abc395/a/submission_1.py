import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:]))

    for i in range(n - 1):
        if arr[i] >= arr[i + 1]:
            print("No")
            return
    print("Yes")

if __name__ == "__main__":
    main()