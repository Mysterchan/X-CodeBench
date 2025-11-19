import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(n+1)
    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i & (-i)
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & (-i)
        return s
    def find_kth(self, k):
        # Find smallest i such that sum(i) >= k
        pos = 0
        bit_mask = 1 << (self.n.bit_length())
        while bit_mask > 0:
            next_pos = pos + bit_mask
            if next_pos <= self.n and self.bit[next_pos] < k:
                k -= self.bit[next_pos]
                pos = next_pos
            bit_mask >>= 1
        return pos + 1

def main():
    N = int(input())
    P = list(map(int, input().split()))

    bit = BIT(N)
    for i in range(1, N+1):
        bit.add(i, 1)  # all positions initially free

    ans = [0]*N
    # We process from i = N down to 1
    # Because inserting i at position P_i means that at the time of insertion,
    # the array length is i-1, and we want to place i at P_i-th position.
    # To reconstruct final array, we place numbers from N down to 1,
    # finding the P_i-th free position in the final array.

    for i in range(N-1, -1, -1):
        pos = bit.find_kth(P[i])
        ans[pos-1] = i+1
        bit.add(pos, -1)  # mark position as occupied

    print(*ans)

if __name__ == "__main__":
    main()