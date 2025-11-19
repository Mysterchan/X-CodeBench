def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    # Any sequence of length 2 is trivially a geometric progression
    if N <= 2:
        print("Yes")
        return

    # Check for each triple whether A[i]/A[i-1] == A[i-1]/A[i-2],
    # i.e., A[i] * A[i-2] == A[i-1] * A[i-1]
    for i in range(2, N):
        if A[i] * A[i-2] != A[i-1] * A[i-1]:
            print("No")
            return

    print("Yes")

if __name__ == "__main__":
    main()