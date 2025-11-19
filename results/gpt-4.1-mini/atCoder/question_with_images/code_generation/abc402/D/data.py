import sys
input = sys.stdin.readline

# Fenwick Tree (BIT) implementation for range sum queries and point updates
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(n+1)
    def update(self, i, v):
        while i <= self.n:
            self.bit[i] += v
            i += i & (-i)
    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & (-i)
        return s
    def range_query(self, l, r):
        return self.query(r) - self.query(l-1)

def main():
    N, M = map(int, input().split())
    chords = []
    for _ in range(M):
        A, B = map(int, input().split())
        # Ensure A < B
        if A > B:
            A, B = B, A
        chords.append((A, B))
    
    # Sort chords by their first endpoint
    chords.sort(key=lambda x: x[0])
    
    # We want to count pairs of chords (i,j) with i<j that intersect.
    # Two chords (a,b) and (c,d) with a < b and c < d intersect iff:
    # a < c < b < d or c < a < d < b
    # Since chords are sorted by a, we only need to check for pairs (i,j) with i<j:
    # chords[i] = (a,b), chords[j] = (c,d), a < c
    # They intersect if a < c < b < d
    
    # So for each chord in order of a, we want to count how many chords with c > a have d < b but d > c.
    # Actually, since a < c, intersection condition reduces to c < b < d is false, so intersection is:
    # a < c < b < d
    
    # We can process chords in order of a, and for each chord (a,b), count how many chords with c > a have d < b.
    # We can do this by iterating chords in order of a, and for each chord, count how many chords with second endpoint less than b have appeared.
    # But we need to be careful to count pairs (i,j) with i<j.
    
    # Approach:
    # - Sort chords by a ascending.
    # - Iterate chords in order.
    # - For each chord (a,b), count how many chords processed so far have second endpoint > b (to find intersections).
    # Actually, the intersection condition is a < c < b < d.
    # Since chords are sorted by a, for current chord (a,b), chords processed so far have a' < a.
    # So we want to count how many chords with a' < a have b' > b.
    # Because for chords (a',b') and (a,b), with a' < a, they intersect if a' < a < b' < b or a < a' < b < b'.
    # Wait, we need to be careful.
    
    # Let's restate:
    # For chords (a,b) and (c,d) with a < b and c < d, sorted by a:
    # They intersect iff a < c < b < d.
    # So for i<j, chords[i] = (a,b), chords[j] = (c,d), a < c < b < d.
    # So for each chord j, count how many chords i with a_i < a_j and b_i > b_j.
    # Because a_i < a_j < b_i < b_j would not satisfy intersection.
    # But a_i < a_j < b_j < b_i means chords do not intersect.
    # So intersection is a_i < a_j < b_i < b_j.
    # So for each chord j, count how many chords i with a_i < a_j and b_i < b_j and b_i > a_j.
    # This is complicated.
    
    # Alternative approach:
    # Since chords are on a circle, and endpoints are labeled 1..N clockwise,
    # and chords are (A_i, B_i) with A_i < B_i,
    # two chords (a,b) and (c,d) intersect iff one endpoint of one chord lies strictly between the endpoints of the other chord on the circle.
    # More concretely, chords (a,b) and (c,d) intersect iff:
    # (a < c < b < d) or (c < a < d < b)
    
    # Since chords are sorted by a, for each chord (a,b), we want to count how many chords (c,d) with c > a satisfy c < b < d.
    # So for each chord in order, we want to count how many chords with c in (a,b) have d > b.
    
    # Let's process chords sorted by a.
    # For each chord (a,b), we want to count how many chords with c in (a,b) have d > b.
    # We can do this by:
    # - For each chord, we will process chords in order of a.
    # - We keep track of chords by their c (which is a) and d (which is b).
    # - For each chord (a,b), we want to count how many chords with c in (a,b) have d > b.
    # - We can use a Fenwick tree indexed by d to count how many chords have d > b.
    
    # Implementation:
    # - Sort chords by a.
    # - We will iterate chords in order of a.
    # - For each chord (a,b), we query Fenwick tree for count of chords with d > b and c in (a,b).
    # - But we only have chords with c < a processed so far.
    # - So we need to process chords in order of a, and for each chord, before inserting it into Fenwick tree, query how many chords with d > b and c in (a,b).
    # - But c in (a,b) means c > a, which is not possible since we process chords in ascending order of a.
    # - So this approach is not straightforward.
    
    # Alternative approach:
    # Let's consider the problem as counting the number of inversions in the sequence of second endpoints when chords are sorted by first endpoint.
    # But intersection condition is more complex.
    
    # Another known approach:
    # The number of intersecting pairs of chords on a circle is equal to the number of inversions in the sequence of second endpoints when chords are sorted by first endpoints.
    # Because two chords (a,b) and (c,d) with a < c intersect iff b > d.
    # So if we sort chords by a ascending, then count pairs (i,j) with i<j and b_i > b_j, that count is the number of intersecting pairs.
    
    # So the problem reduces to counting inversions in the array of b's after sorting chords by a.
    
    # We can count inversions using Fenwick tree.
    
    # Steps:
    # 1. Sort chords by a ascending.
    # 2. Extract array B = [b_i for each chord in sorted order].
    # 3. Count number of pairs (i,j) with i<j and B[i] > B[j].
    # 4. Use Fenwick tree to count inversions efficiently.
    
    # Fenwick tree will be indexed by b values.
    # Since b can be up to N (<= 10^6), Fenwick tree size = N.
    
    fenw = FenwickTree(N)
    result = 0
    
    for _, b in chords:
        # Count how many b_j < b have appeared so far
        # We want to count how many b_i > b_j for i<j
        # So for current b, number of b_i > b is total inserted - number of b_i <= b
        # total inserted = number of chords processed so far
        total = fenw.query(N)
        less_equal_b = fenw.query(b)
        result += total - less_equal_b
        fenw.update(b, 1)
    
    print(result)

if __name__ == "__main__":
    main()