import sys
input = sys.stdin.readline

# Fenwick Tree (BIT) implementation for sum queries and point updates
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.fw = [0]*(n+1)
    def update(self, i, delta=1):
        while i <= self.n:
            self.fw[i] += delta
            i += i & (-i)
    def query(self, i):
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & (-i)
        return s
    def query_range(self, l, r):
        return self.query(r) - self.query(l-1)

def main():
    N, M = map(int, input().split())
    segments = []
    for _ in range(M):
        A, B = map(int, input().split())
        # Ensure A < B
        if A > B:
            A, B = B, A
        segments.append((A, B))
    # Sort segments by their left endpoint A ascending
    segments.sort(key=lambda x: x[0])

    # We want to count pairs of segments (i,j), i<j, that intersect.
    # Two chords (A_i,B_i) and (A_j,B_j) with A_i < B_i and A_j < B_j intersect iff:
    # A_i < A_j < B_i < B_j or A_j < A_i < B_j < B_i
    # Since we sort by A ascending, we only need to count pairs (i<j) with:
    # A_i < A_j and B_i > B_j (the first condition)
    # So for each segment in order of increasing A, count how many previously processed segments have B > current B.

    # We'll process segments in order of increasing A.
    # For each segment, count how many previous segments have B > current B.
    # Since B <= N, we can use Fenwick tree to count how many B's are greater than current B.

    # Fenwick tree will store counts of B's encountered so far.
    # To count how many B_i > B_j, we do:
    # total processed so far - fenw.query(B_j)
    # where fenw.query(B_j) gives count of B_i <= B_j

    fenw = FenwickTree(N)
    result = 0
    processed = 0
    for A, B in segments:
        # count how many B_i > B
        greater_count = processed - fenw.query(B)
        result += greater_count
        fenw.update(B)
        processed += 1

    print(result)

if __name__ == "__main__":
    main()