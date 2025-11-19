import sys

def solve():
    n = int(sys.stdin.readline())
    s_str = sys.stdin.readline().strip()
    t_str = sys.stdin.readline().strip()

    s_list = [int(c) for c in s_str]
    t_list = [int(c) for c in t_str]

    q = n
    if q == 0:
        sys.stdout.write("Yes\n" if s_str == t_str else "No\n")
        return

    while q % 2 == 0:
        q //= 2

    num_blocks = n // q

    s_blocks_rows = []
    for i in range(num_blocks):
        s_blocks_rows.append(s_list[i*q : (i+1)*q])

    t_blocks_rows = []
    for i in range(num_blocks):
        t_blocks_rows.append(t_list[i*q : (i+1)*q])


    def get_rref_basis(matrix_rows_orig, K, M):
        if K == 0:
             return []

        matrix = [list(row) for row in matrix_rows_orig]

        pivot_row_idx = 0
        for col_idx in range(M):
            if pivot_row_idx >= K:
                break

            i = pivot_row_idx
            while i < K and matrix[i][col_idx] == 0:
                i += 1

            if i < K:
                matrix[pivot_row_idx], matrix[i] = matrix[i], matrix[pivot_row_idx]

                for k_row_iter_idx in range(K):
                    if k_row_iter_idx != pivot_row_idx and matrix[k_row_iter_idx][col_idx] == 1:
                        for j_col_iter_idx in range(col_idx, M):
                            matrix[k_row_iter_idx][j_col_iter_idx] ^= matrix[pivot_row_idx][j_col_iter_idx]
                pivot_row_idx += 1

        basis = []
        for r_idx in range(pivot_row_idx):
            basis.append(tuple(matrix[r_idx]))

        basis.sort()
        return basis

    basis_s = get_rref_basis(s_blocks_rows, num_blocks, q)
    basis_t = get_rref_basis(t_blocks_rows, num_blocks, q)

    if basis_s == basis_t:
        sys.stdout.write("Yes\n")
    else:
        sys.stdout.write("No\n")

num_test_cases = int(sys.stdin.readline())
for _ in range(num_test_cases):
    solve()
