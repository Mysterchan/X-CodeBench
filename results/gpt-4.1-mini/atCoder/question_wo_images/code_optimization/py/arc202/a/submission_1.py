import sys
input = sys.stdin.readline

def solve(N, A):
    # Add sentinel values at both ends
    A = [10**18] + A + [10**18]
    prev = [i-1 for i in range(N+2)]
    nxt = [i+1 for i in range(N+2)]
    prev[0] = 0
    nxt[N+1] = N+1

    # We'll maintain a stack of indices representing a "compressed" sequence
    # Each element in the stack corresponds to a value and its position
    # We simulate merges greedily from left to right
    ans = 0
    stack = []

    for i in range(1, N+1):
        val = A[i]
        pos = i
        # Try to merge with top of stack if values equal
        while stack and stack[-1][0] == val:
            # Merge operation: remove top, increment val
            val += 1
            stack.pop()
        stack.append((val, pos))

    # Now we have a compressed sequence in stack
    # We need to merge it down to length 1 by inserting minimal elements
    # The minimal insertions needed is sum of differences between consecutive elements
    # because to merge two different values x < y, we need to insert (y - x) elements to raise x to y
    # Then merge them to x+1, and so on until one element remains.

    # We'll simulate merges from left to right on the stack
    # Each merge reduces length by 1, so total merges = len(stack) - 1
    # For each adjacent pair, we add (next_val - current_val) to ans

    for i in range(len(stack)-1):
        ans += stack[i+1][0] - stack[i][0]

    return ans

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))