def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    P = list(map(int, data[1:N+1]))
    Q = list(map(int, data[N+1:2*N+1]))

    # Create mapping from person to their bib number
    bib_map = {}
    for i in range(N):
        bib_map[P[i]] = Q[i]

    # Prepare the result using the mapping
    result = [0] * N
    for i in range(1, N + 1):
        person_staring_at = P[i - 1]
        result[i - 1] = bib_map[person_staring_at]

    print(" ".join(map(str, result)))