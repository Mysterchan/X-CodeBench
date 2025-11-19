import sys
input = sys.stdin.readline

# Directions mapping to (dr, dc)
dir_map = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

def main():
    R_t, C_t, R_a, C_a = map(int, input().split())
    N, M, L = map(int, input().split())

    S = []
    for _ in range(M):
        ch, cnt = input().split()
        cnt = int(cnt)
        S.append((ch, cnt))

    T = []
    for _ in range(L):
        ch, cnt = input().split()
        cnt = int(cnt)
        T.append((ch, cnt))

    # We want to count the number of times after a move that Takahashi and Aoki are at the same cell.
    # Let diff = (R_t - R_a, C_t - C_a)
    # Each move changes diff by (dr_t - dr_a, dc_t - dc_a)
    # We want to count how many i in [1..N] satisfy:
    # diff + sum_{j=1}^i (delta_j) = (0,0)
    # where delta_j = move difference at step j.

    # Since N can be huge, we cannot simulate all moves.
    # But S and T are given in run-length encoded form.
    # We can process the moves in blocks.

    # We'll process the moves in a merged manner:
    # Both S and T are sequences of (char, count).
    # We'll iterate over these sequences simultaneously,
    # processing min(count_S, count_T) moves at a time.

    # For each block of moves, the difference delta is constant per move.
    # So difference changes linearly in that block.

    # For each block:
    # diff_i = diff + i * delta (i from 1 to length_of_block)
    # We want to count i where diff_i == (0,0)
    # => diff + i * delta = 0
    # => i * delta = -diff
    # If delta == (0,0):
    #   if diff == (0,0), all i in block satisfy
    #   else none
    # else:
    #   check if there exists i in [1, length_of_block] integer satisfying above.

    # We'll accumulate the answer.

    # Initialize pointers and counts
    pS = 0
    pT = 0
    cS = S[0][1]
    cT = T[0][1]
    chS = S[0][0]
    chT = T[0][0]

    diff_r = R_t - R_a
    diff_c = C_t - C_a

    ans = 0

    while pS < M and pT < L:
        length = min(cS, cT)

        drS, dcS = dir_map[chS]
        drT, dcT = dir_map[chT]

        delta_r = drS - drT
        delta_c = dcS - dcT

        # We want to find i in [1..length] such that:
        # diff_r + i*delta_r == 0 and diff_c + i*delta_c == 0

        if delta_r == 0 and delta_c == 0:
            # difference does not change in this block
            if diff_r == 0 and diff_c == 0:
                # all positions in this block are equal
                ans += length
            # else no positions equal
        else:
            # Solve for i:
            # i = -diff_r / delta_r (if delta_r != 0)
            # i = -diff_c / delta_c (if delta_c != 0)
            # Both must be equal and integer and in [1,length]

            # Check consistency
            i_r = None
            i_c = None

            if delta_r != 0:
                if (-diff_r) % delta_r != 0:
                    i_r = None
                else:
                    i_r = (-diff_r) // delta_r
            else:
                # delta_r == 0, so diff_r must be 0 for equality
                if diff_r == 0:
                    i_r = None  # no restriction from r
                else:
                    i_r = -1  # impossible

            if delta_c != 0:
                if (-diff_c) % delta_c != 0:
                    i_c = None
                else:
                    i_c = (-diff_c) // delta_c
            else:
                # delta_c == 0, so diff_c must be 0 for equality
                if diff_c == 0:
                    i_c = None  # no restriction from c
                else:
                    i_c = -1  # impossible

            # Now check if i_r and i_c are consistent
            # If both defined, must be equal
            # If one is None, use the other
            # If both None, means any i satisfies (should not happen here)

            if i_r == -1 or i_c == -1:
                # no solution
                pass
            else:
                if i_r is not None and i_c is not None:
                    if i_r == i_c and 1 <= i_r <= length:
                        ans += 1
                elif i_r is not None:
                    if 1 <= i_r <= length:
                        ans += 1
                elif i_c is not None:
                    if 1 <= i_c <= length:
                        ans += 1
                else:
                    # both None means delta_r=0 and diff_r=0 and delta_c=0 and diff_c=0
                    # all positions equal
                    ans += length

        # Update diff for next block
        diff_r += delta_r * length
        diff_c += delta_c * length

        # Update counts and pointers
        cS -= length
        cT -= length
        if cS == 0:
            pS += 1
            if pS < M:
                chS, cS = S[pS]
        if cT == 0:
            pT += 1
            if pT < L:
                chT, cT = T[pT]

    print(ans)

if __name__ == "__main__":
    main()