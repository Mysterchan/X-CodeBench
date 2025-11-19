import sys
input = sys.stdin.readline

# Fenwick Tree (BIT) for sum queries and updates
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(n+1)
    def update(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i & (-i)
    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & (-i)
        return s

def main():
    N = int(input())
    P = list(map(int, input().split()))

    # We want to find the minimal total cost to sort P by adjacent swaps,
    # where swapping positions i and i+1 costs i.
    #
    # Key insight:
    # Each inversion (i < j and P[i] > P[j]) must be resolved by swapping P[i] and P[j].
    # The cost to move an element from position j to i (j > i) by adjacent swaps is:
    # sum of positions of swaps = i + (i+1) + ... + (j-1) = (j-1)*j/2 - (i-1)*i/2
    #
    # The minimal total cost is sum over all inversions of (j - i) weighted by the swap positions.
    #
    # We can compute the cost by processing elements in ascending order of their values.
    # For each element, we calculate how many elements with smaller values are to the right,
    # and sum their positions to compute the cost.
    #
    # Implementation:
    # - Process elements in ascending order of their values.
    # - Use two Fenwicks:
    #   1) fenw_count: counts how many elements have been processed at positions <= x
    #   2) fenw_pos: sum of positions of processed elements
    #
    # For current element at position pos:
    #   - count_right = fenw_count.query(N) - fenw_count.query(pos)
    #   - sum_pos_right = fenw_pos.query(N) - fenw_pos.query(pos)
    #   - cost contribution = sum_pos_right - count_right * pos
    #
    # Add this to total cost and update fenwicks with current position.

    # Create array of (value, position)
    arr = [(val, i+1) for i, val in enumerate(P)]
    arr.sort()  # sort by value ascending

    fenw_count = FenwickTree(N)
    fenw_pos = FenwickTree(N)

    total_cost = 0
    for val, pos in arr:
        count_right = fenw_count.query(N) - fenw_count.query(pos)
        sum_pos_right = fenw_pos.query(N) - fenw_pos.query(pos)
        total_cost += sum_pos_right - count_right * pos
        fenw_count.update(pos, 1)
        fenw_pos.update(pos, pos)

    print(total_cost)

if __name__ == "__main__":
    main()