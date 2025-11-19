import sys
def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    a = list(map(int, data[1:1+n]))
    for i in range(n-1):
        if not (a[i] < a[i+1]):
            print("No")
            return
    print("Yes")

if __name__ == "__main__":
    main()