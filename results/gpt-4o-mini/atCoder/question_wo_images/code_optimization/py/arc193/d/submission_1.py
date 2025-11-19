def solve(N, A, B):
    a_pieces = [i for i in range(N) if A[i] == '1']
    b_meta = [i for i in range(N) if B[i] == '1']

    if len(a_pieces) < len(b_meta):
        return -1

    operations = 0
    j = 0

    for i in range(len(b_meta)):
        while j < len(a_pieces) and a_pieces[j] < b_meta[i]:
            j += 1
        if j >= len(a_pieces) or a_pieces[j] > b_meta[i]:
            if j == 0:
                return -1
            j -= 1
        operations += abs(a_pieces[j] - b_meta[i])
        j += 1

    return operations

T = int(input())
for _ in range(T):
    N = int(input())
    A = input().strip()
    B = input().strip()
    result = solve(N, A, B)
    print(result)