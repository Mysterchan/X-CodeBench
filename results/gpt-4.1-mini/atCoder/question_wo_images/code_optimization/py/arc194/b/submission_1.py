import sys
input = sys.stdin.readline

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

N = int(input())
P = list(map(int, input().split()))

fenw = FenwickTree(N)
ans = 0
for i, x in enumerate(P, 1):
    # Number of elements greater than x already processed
    greater_count = fenw.query(N) - fenw.query(x)
    # Each such element contributes cost equal to its position (i)
    # The cost for swapping x past these elements is sum of their positions
    # But we only know count, not positions. Instead, we accumulate cost as:
    # For each inversion (x,y) with x before y and x>y, cost is position of swap = position of smaller element
    # The problem cost is sum over all inversions of min(i,j)
    # Using Fenwick tree to accumulate sum of positions of elements processed so far
    # We maintain fenw for counts and fenw_pos for sum of positions
    # So we need two Fenwicks: one for counts, one for positions

# Re-implement with two Fenwicks
class Fenwick:
    def __init__(self,n):
        self.n = n
        self.bit = [0]*(n+1)
    def update(self,i,x):
        while i<=self.n:
            self.bit[i]+=x
            i+=i&(-i)
    def query(self,i):
        s=0
        while i>0:
            s+=self.bit[i]
            i-=i&(-i)
        return s

fenw_count = Fenwick(N)
fenw_pos = Fenwick(N)
ans = 0
for i,x in enumerate(P,1):
    # Number of elements greater than x processed so far
    cnt_greater = fenw_count.query(N) - fenw_count.query(x)
    # Sum of positions of elements greater than x processed so far
    sum_pos_greater = fenw_pos.query(N) - fenw_pos.query(x)
    # For each inversion (x,y) with x before y and x>y,
    # cost is min(i,j) = position of smaller element = position of y
    # Since y > x, and y processed before x, y's position is in fenw_pos
    # So add sum_pos_greater to answer
    ans += sum_pos_greater
    fenw_count.update(x,1)
    fenw_pos.update(x,i)

print(ans)