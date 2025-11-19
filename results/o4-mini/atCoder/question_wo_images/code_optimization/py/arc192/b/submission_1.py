import sys
def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    A = list(map(int, data[1:]))
    cnt_odd = 0
    for a in A:
        cnt_odd += a & 1
    # Snuke wins only if N is even and the count of odd A_i is even.
    if N % 2 == 0 and cnt_odd % 2 == 0:
        print("Snuke")
    else:
        print("Fennec")

if __name__ == "__main__":
    main()