def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    H, W = map(int, data[0].split())
    board = data[1:H + 1]

    min_row, max_row = H, -1
    min_col, max_col = W, -1

    # Find the boundary of black cells
    for i in range(H):
        for j in range(W):
            if board[i][j] == '#':
                min_row = min(min_row, i)
                max_row = max(max_row, i)
                min_col = min(min_col, j)
                max_col = max(max_col, j)

    # Check if all cells in the found rectangle can be either black or white
    for i in range(H):
        for j in range(W):
            if (min_row <= i <= max_row and min_col <= j <= max_col) and board[i][j] != '#':
                print("No")
                return
            if not (min_row <= i <= max_row and min_col <= j <= max_col) and board[i][j] == '#':
                print("No")
                return

    print("Yes")

if __name__ == "__main__":
    main()