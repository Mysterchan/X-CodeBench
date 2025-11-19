def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    # The problem reduces to counting the number of distinct XOR sums
    # of subsets of A, because the operation allows merging stones arbitrarily,
    # so the final XOR values correspond to XOR sums of subsets of A.

    # We use a linear basis (XOR basis) to find the number of distinct XOR sums.
    basis = []
    for x in A:
        for b in basis:
            x = min(x, x ^ b)
        if x > 0:
            # Insert x into basis in sorted order (descending)
            # to keep basis minimal and consistent
            for i in range(len(basis)):
                if basis[i] < x:
                    basis.insert(i, x)
                    break
            else:
                basis.append(x)

    # Number of distinct XOR sums is 2^(size of basis)
    print(1 << len(basis))


if __name__ == "__main__":
    main()