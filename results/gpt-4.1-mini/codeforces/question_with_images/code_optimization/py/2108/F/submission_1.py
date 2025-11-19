import sys
input = sys.stdin.readline

def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        # The problem can be solved greedily:
        # We want to find the maximum MEX of the final array after all operations.
        # After knocking down all towers, the final array is non-decreasing.
        # Each tower is knocked down exactly once, and knocking down tower i adds a_i to the next a_i towers.
        #
        # The key insight:
        # We can simulate the process by trying to assign final heights from left to right.
        # For each tower, the minimal final height it can have is the maximum between the current "carry" and a_i.
        # We keep track of a "carry" which represents how many increments have been propagated to the current tower.
        #
        # The final height of tower i is max(carry, a[i]).
        # Then, carry = max(0, carry - 1) because the increments propagate forward but decrease by 1 each step.
        #
        # After processing all towers, the final array is non-decreasing by construction.
        # The MEX is the smallest non-negative integer not in the final array.
        #
        # This approach runs in O(n) per test case.

        carry = 0
        final = []
        for height in a:
            final_height = max(carry, height)
            final.append(final_height)
            carry = max(0, final_height - 1)

        # Compute MEX
        mex = 0
        for val in final:
            if val == mex:
                mex += 1
            elif val > mex:
                break

        results.append(str(mex))

    print("\n".join(results))

if __name__ == "__main__":
    main()