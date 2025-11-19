MOD = 998244353

# We will use a DP approach with states representing the relation of the king's position to the target position.
# Define four states based on whether the current position's row and column match the target row and column:
# State 0: row != target_row and col != target_col
# State 1: row != target_row and col == target_col
# State 2: row == target_row and col != target_col
# State 3: row == target_row and col == target_col (the target state)

# Transitions between states depend on the king's moves and the board boundaries.
# We precompute the number of ways to move from each state to another state in one step.

def main():
    import sys
    input = sys.stdin.readline

    H, W, T, A, B, C, D = map(int, input().split())

    # Initial state
    # Determine initial state based on (A,B) vs (C,D)
    def state(r, c):
        return (r == C) * 2 + (c == D)

    # But we use a different encoding for convenience:
    # Let's define states as:
    # 0: row != C and col != D
    # 1: row != C and col == D
    # 2: row == C and col != D
    # 3: row == C and col == D

    # So:
    def get_state(r, c):
        return (0 if r != C else 2) + (0 if c != D else 1)

    # Initial DP vector
    dp = [0, 0, 0, 0]
    dp[get_state(A, B)] = 1

    # Precompute counts for transitions:
    # For each state, we calculate how many moves lead to each other state.

    # Number of rows not equal to C: H-1
    # Number of columns not equal to D: W-1

    # For each state, we consider the king's possible moves (8 directions),
    # and count how many moves lead to each state.

    # To do this, we consider the possible moves from a position in each state,
    # and count how many moves lead to each state.

    # Let's define the counts of neighbors in each state from a position in each state.

    # For a position in state 0 (row != C, col != D):
    # The king can move to 8 adjacent squares.
    # Among these, how many have row == C? How many have col == D?

    # But since the king moves only one step, the row can change by -1,0,1 and col by -1,0,1 (except (0,0)).

    # Let's define:
    # For a position in state 0:
    # - Moves to state 3 (row == C and col == D): if (row ±1 == C) and (col ±1 == D)
    # - Moves to state 1 (row != C and col == D): if (col ±1 == D) and (row ±1 != C)
    # - Moves to state 2 (row == C and col != D): if (row ±1 == C) and (col ±1 != D)
    # - Moves to state 0 (row != C and col != D): otherwise

    # But we must consider board boundaries.

    # To handle boundaries, we consider the counts of neighbors in each state from a position in each state.

    # Let's define variables for counts of neighbors in each state from each state:

    # For state 0:
    # From a position in state 0, the number of neighbors in each state is:
    # - state 3 neighbors: number of neighbors with row == C and col == D
    # - state 1 neighbors: row != C and col == D
    # - state 2 neighbors: row == C and col != D
    # - state 0 neighbors: row != C and col != D

    # Similarly for other states.

    # To compute these counts, we consider the possible moves and the board size.

    # Let's define helper variables:

    # For rows:
    # - If current row == C: row_state = 2
    # - else: row_state = 0

    # For columns:
    # - If current col == D: col_state = 1
    # - else: col_state = 0

    # So state = row_state + col_state

    # We will compute the number of neighbors in each state from a position in each state.

    # Let's define the number of neighbors in each state from each state as a 4x4 matrix.

    # To do this, we consider the possible moves and count how many neighbors fall into each state.

    # We consider the possible moves: 8 directions
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

    # For each state s in [0..3], we consider a position (r,c) in that state.
    # We count how many neighbors are in each state.

    # To do this, we consider the possible rows and columns for the position in state s:
    # For row:
    # - if s in {0,1}: row != C
    # - if s in {2,3}: row == C
    # For col:
    # - if s in {0,2}: col != D
    # - if s in {1,3}: col == D

    # For each state s, we pick a representative position (r,c) satisfying the state conditions.
    # For example:
    # s=0: r != C, c != D
    # s=1: r != C, c == D
    # s=2: r == C, c != D
    # s=3: r == C, c == D

    # We then count neighbors in each state by checking the conditions on (r+dr, c+dc).

    # But we must consider board boundaries:
    # For each move, (r+dr, c+dc) must be within [1,H] x [1,W].

    # To handle this, we consider the number of valid neighbors in each state from a position in each state.

    # Since the board is large, and we only need counts, we can compute the number of neighbors in each state from a position in each state as follows:

    # For each state s:
    # - Determine possible r and c for that state:
    #   For r:
    #     if row == C: r = C
    #     else: r can be any row except C, but for counting neighbors, we just pick a representative r != C (e.g., C-1 if C>1 else C+1)
    #   For c:
    #     similarly.

    # Then for each direction, check if (r+dr, c+dc) is inside the board.
    # If yes, determine the state of (r+dr, c+dc) and increment count.

    # Implement this logic:

    def neighbors_count(r, c):
        counts = [0,0,0,0]
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 1 <= nr <= H and 1 <= nc <= W:
                ns = get_state(nr, nc)
                counts[ns] += 1
        return counts

    # For each state s, pick representative (r,c):
    # For row:
    # if s in {0,1}: row != C
    # if s in {2,3}: row == C
    # For col:
    # if s in {0,2}: col != D
    # if s in {1,3}: col == D

    # Choose representative rows and columns:
    def rep_row(s):
        return C if s & 2 else (C-1 if C > 1 else C+1)
    def rep_col(s):
        return D if s & 1 else (D-1 if D > 1 else D+1)

    # Build transition matrix M: M[from_state][to_state] = number of ways to move from from_state to to_state in one step
    M = [[0]*4 for _ in range(4)]
    for s in range(4):
        r = rep_row(s)
        c = rep_col(s)
        counts = neighbors_count(r, c)
        for ns in range(4):
            M[s][ns] = counts[ns]

    # Now we do DP for T steps:
    # dp_next = dp * M
    # We can do this efficiently by repeated multiplication.

    # Since T can be large, we do repeated multiplication using fast exponentiation of the matrix M.

    # Implement matrix multiplication and exponentiation modulo MOD

    def matmul(A, B):
        n = len(A)
        m = len(B[0])
        p = len(B)
        res = [[0]*m for _ in range(n)]
        for i in range(n):
            ai = A[i]
            for j in range(m):
                s = 0
                for k in range(p):
                    s += ai[k]*B[k][j]
                res[i][j] = s % MOD
        return res

    def matpow(mat, power):
        result = [[0]*4 for _ in range(4)]
        for i in range(4):
            result[i][i] = 1
        base = mat
        while power > 0:
            if power & 1:
                result = matmul(result, base)
            base = matmul(base, base)
            power >>= 1
        return result

    M_T = matpow(M, T)

    # dp is a vector of length 4
    # dp_final = dp * M_T
    dp_final = [0]*4
    for j in range(4):
        s = 0
        for i in range(4):
            s += dp[i]*M_T[i][j]
        dp_final[j] = s % MOD

    # The answer is dp_final[state 3] (row == C and col == D)
    print(dp_final[3])

if __name__ == "__main__":
    main()