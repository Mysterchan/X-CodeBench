def main():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # Forward pass: for each B[i], find the earliest position in A where B[i] can be matched in order
    fpos = [-1] * M
    idx = 0
    for i in range(N):
        if idx < M and A[i] == B[idx]:
            fpos[idx] = i
            idx += 1
    if idx < M:
        # B is not a subsequence of A at all
        print("No")
        return

    # Backward pass: for each B[i], find the latest position in A where B[i] can be matched in order
    bpos = [-1] * M
    idx = M - 1
    for i in range(N - 1, -1, -1):
        if idx >= 0 and A[i] == B[idx]:
            bpos[idx] = i
            idx -= 1
    if idx >= 0:
        # B is not a subsequence of A at all (should not happen since forward pass succeeded)
        print("No")
        return

    # If there are at least two subsequences matching B, then there must be some position i
    # where fpos[i] < bpos[i], meaning we can choose different positions for B[i].
    # Because fpos is earliest positions and bpos is latest positions.
    for i in range(M - 1):
        if fpos[i] < bpos[i + 1]:
            print("Yes")
            return

    # If no such pair found, then only one subsequence matches B
    print("No")


if __name__ == "__main__":
    main()