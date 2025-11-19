import sys
input = sys.stdin.readline

def solve():
    H, W = map(int, input().split())
    rows = [int(input().strip(), 2) for _ in range(H)]

    # Precompute bit counts for all possible W-bit numbers
    # Since W <= 18, max number is < 2^18 = 262144
    max_mask = 1 << W
    bit_count = [0] * max_mask
    for i in range(1, max_mask):
        bit_count[i] = bit_count[i >> 1] + (i & 1)

    min_total = float('inf')

    # For each possible column flip pattern
    for col_flip in range(max_mask):
        total = 0
        # For each row, decide whether to flip the row or not
        # cost_no_flip = number of zeros after column flips
        # cost_with_flip = number of zeros after column flips and row flip
        for r in rows:
            flipped = r ^ col_flip
            ones = bit_count[flipped]
            zeros = W - ones
            # row flip toggles all bits, so zeros become ones and vice versa
            total += min(zeros, ones)
            # Early pruning if total already exceeds min_total
            if total >= min_total:
                break
        if total < min_total:
            min_total = total

    print(min_total)

solve()