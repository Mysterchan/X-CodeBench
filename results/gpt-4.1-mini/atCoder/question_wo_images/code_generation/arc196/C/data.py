MOD = 998244353

def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    S = input().strip()

    # The problem:
    # We have 2N vertices, edges i->i+1 for i=1..2N-1
    # Each vertex colored W or B, with exactly N Ws and N Bs.
    # We add N edges from white to black vertices, pairing them one-to-one.
    # Count the number of ways to pair so that the final graph is strongly connected.

    # Key observations and known result from editorial:
    # The graph is strongly connected iff the pairing corresponds to a "non-crossing matching"
    # between the white and black vertices when arranged in order.
    #
    # The problem reduces to counting the number of ways to pair Ws and Bs in order,
    # such that the pairs form a non-crossing matching.
    #
    # This is a classic problem related to counting valid bracket sequences or Dyck paths,
    # but here the sequence is given with Ws and Bs.
    #
    # We can use a stack-based DP or a combinational approach:
    #
    # The number of ways to pair the sequence so that the graph is strongly connected
    # equals the number of ways to match Ws and Bs in order without crossing.
    #
    # The approach:
    # - We scan the sequence from left to right.
    # - Maintain a stack of unmatched W vertices.
    # - When we see a W, push it.
    # - When we see a B, we must pair it with a W from the stack.
    #   The number of ways to pair depends on how many Ws are currently unmatched.
    #
    # The number of ways is the product of the number of choices at each B.
    #
    # More precisely:
    # - At each B, the number of choices is the number of unmatched Ws currently on the stack.
    #
    # If at any point the stack is empty when we see a B, no valid pairing is possible.
    #
    # The final answer is the product of these choices modulo 998244353.

    stack = []
    ans = 1
    for c in S:
        if c == 'W':
            stack.append(c)
        else:  # c == 'B'
            if not stack:
                # No W to pair with this B
                print(0)
                return
            # Number of choices = size of stack
            ans = (ans * len(stack)) % MOD
            stack.pop()

    # At the end, stack should be empty (all Ws matched)
    if stack:
        print(0)
        return

    print(ans % MOD)

if __name__ == "__main__":
    main()