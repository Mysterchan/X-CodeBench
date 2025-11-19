import sys
sys.setrecursionlimit(10**7)
MOD = 998244353

def main():
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))

    # The problem is a known hard problem from AtCoder (AGC 033 F).
    # The key insight is that the sequence B must satisfy:
    # For every interval [l,r], there exists x in [l,r] such that
    # the graph formed by edges (i, B_i) for i in [l,r], i != x is a tree on vertices [l,r].
    #
    # This implies a very strong structural condition on B:
    # - For each interval, removing one vertex x, the rest form a tree.
    #
    # This condition is equivalent to B being a "functional graph" with a unique "root" in every interval,
    # and the edges form a rooted tree structure with some constraints.
    #
    # The problem is known to be solved by a divide-and-conquer DP approach:
    #
    # We define a recursive function f(l, r) = number of ways to fill A[l:r+1] to satisfy the condition.
    #
    # The key is to find a position m in [l,r] such that B_m = m (self-loop),
    # and the left and right parts are independent subproblems.
    #
    # If A[m] != -1 and A[m] != m+1, no solution.
    # If A[m] == -1, we set B_m = m+1.
    #
    # Then the edges in [l,r] \ {m} form a tree rooted at m.
    #
    # So the problem reduces to:
    # f(l,r) = sum over m in [l,r] where B_m = m+1 (or can be set to m+1)
    #          f(l,m-1) * f(m+1,r)
    #
    # We can implement this with segment DP.
    #
    # To speed up, we use a stack-based approach to find valid partitions.
    #
    # The main challenge is to handle the constraints from A:
    # - If A[i] != -1 and A[i] != i+1, then i cannot be the root of the interval containing i.
    #
    # We will implement a DP with a stack to find the number of ways.

    # Preprocessing:
    # We want to find all intervals [l,r] where the root is at position m with B_m = m+1.
    # For each position i, if A[i] != -1 and A[i] != i+1, then i cannot be root.
    # If A[i] == -1, we can set B_i = i+1 (root).
    # So root candidates are positions i where A[i] == -1 or A[i] == i+1.

    # We will use a stack to simulate the construction of the tree.
    # The approach is similar to the editorial of AGC033F:
    #
    # We process from left to right, maintaining a stack of intervals.
    # Each interval corresponds to a subtree.
    #
    # When we find a root candidate, we try to merge intervals on the stack.
    #
    # The DP state is the number of ways to form a subtree for the interval.

    # dp_stack will hold tuples (start, ways)
    # start: start index of the interval
    # ways: number of ways to form the subtree on [start, current_position]

    dp_stack = []

    def modmul(a,b):
        return (a*b) % MOD

    for i in range(N):
        # Check if i can be root
        can_be_root = (A[i] == -1 or A[i] == i+1)

        if not can_be_root:
            # If cannot be root, push interval [i,i] with ways=0 (no subtree)
            dp_stack.append((i, 0))
            continue

        # If can be root, start a new interval [i,i] with ways=1 (single node tree)
        ways = 1
        start = i

        # Try to merge intervals on the stack to the left
        while dp_stack:
            prev_start, prev_ways = dp_stack[-1]
            # The intervals must be contiguous
            if prev_start == start - 1:
                # Merge intervals [prev_start, start-1] and [start, i]
                ways = modmul(prev_ways, ways)
                start = prev_start
                dp_stack.pop()
            else:
                break

        dp_stack.append((start, ways))

    # After processing all positions, we should have one interval [0, N-1]
    # If not, no valid ways
    if len(dp_stack) != 1 or dp_stack[0][0] != 0:
        print(0)
        return

    print(dp_stack[0][1] % MOD)

if __name__ == "__main__":
    main()