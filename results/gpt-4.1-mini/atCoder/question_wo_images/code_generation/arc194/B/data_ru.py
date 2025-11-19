import sys
input = sys.stdin.readline

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)
    def add(self, i, x):
        while i <= self.n:
            self.data[i] += x
            i += i & (-i)
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & (-i)
        return s
    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l-1)

def main():
    N = int(input())
    P = list(map(int, input().split()))

    # We want to find the minimal total cost to sort P by swapping adjacent elements,
    # where swapping positions i and i+1 costs i.
    #
    # Key insight:
    # Each inversion (i < j and P[i] > P[j]) must be resolved by swapping P[i] and P[j].
    # The cost to swap adjacent elements at position k is k.
    #
    # The minimal total cost equals the sum over all inversions of the positions where swaps occur.
    #
    # We can think of the cost as sum over all inversions (i,j) with i<j and P[i]>P[j] of i.
    #
    # To compute this efficiently:
    # For each element P[j], count how many elements to the left are greater than P[j].
    # For each such inversion, add the position i of the greater element.
    #
    # So total cost = sum over all inversions of i (the index of the left element in the inversion).
    #
    # We can process elements from left to right:
    # For each P[j], we want sum of indices i < j where P[i] > P[j].
    #
    # Use a Fenwick tree to:
    # - Keep track of how many elements with value v have appeared and their indices sum.
    # - For current P[j], sum indices of elements with value > P[j].
    #
    # Since P is a permutation of 1..N, we can use Fenwick tree indexed by values.
    #
    # We'll maintain two Fenwicks:
    # 1) fenw_count: counts how many elements with value <= x have appeared
    # 2) fenw_index_sum: sum of indices of elements with value <= x
    #
    # For current P[j], number of elements with value > P[j] = total_count_so_far - fenw_count.sum(P[j])
    # sum of indices of elements with value > P[j] = total_index_sum_so_far - fenw_index_sum.sum(P[j])
    #
    # We add this sum to answer.
    #
    # Then add current element P[j] with index j+1 to fenwicks.
    #
    # This gives total cost.

    fenw_count = FenwickTree(N)
    fenw_index_sum = FenwickTree(N)

    total_cost = 0
    total_count = 0
    total_index_sum = 0

    for j, val in enumerate(P, 1):
        # sum of indices of elements with value > val
        sum_indices_greater = total_index_sum - fenw_index_sum.sum(val)
        total_cost += sum_indices_greater

        fenw_count.add(val, 1)
        fenw_index_sum.add(val, j)
        total_count += 1
        total_index_sum += j

    print(total_cost)

if __name__ == "__main__":
    main()