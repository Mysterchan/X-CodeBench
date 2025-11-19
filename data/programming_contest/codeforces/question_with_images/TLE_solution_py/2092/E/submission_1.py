def solve():
    n, m, k = map(int, input().split())
    cells = []
    for _ in range(k):
        cells.append(list(map(int, input().split())))

    def calculate_diff_pairs(board):
        count = 0
        for i in range(n):
            for j in range(m):
                if i > 0 and board[i][j] != board[i-1][j]:
                    count += 1
                if j > 0 and board[i][j] != board[i][j-1]:
                    count += 1
        return count

    def generate_board(painted_cells):
        board = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                painted = False
                for cell in cells:
                    if cell[0] == i + 1 and cell[1] == j + 1:
                        board[i][j] = cell[2]
                        painted = True
                        break
                if not painted:
                    board[i][j] = -1

        idx = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == -1:
                    board[i][j] = painted_cells[idx]
                    idx += 1

        return board


    unpainted_cells = n * m - k

    count = 0

    for i in range(2**unpainted_cells):
        painted_cells = []
        binary_representation = bin(i)[2:].zfill(unpainted_cells)

        for bit in binary_representation:
            painted_cells.append(int(bit))

        board = generate_board(painted_cells)

        diff_pairs = calculate_diff_pairs(board)

        if diff_pairs % 2 == 0:
            count += 1

    print(count % (10**9 + 7))


t = int(input())
for _ in range(t):
    solve()
