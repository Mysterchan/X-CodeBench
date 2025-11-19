import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    # We will process each test case independently.
    # The problem is to find the minimal number of insertions to make the sequence "good".
    #
    # Key insight:
    # The "good" sequence can be merged repeatedly until length 1 by merging pairs of equal adjacent elements into one element with value+1.
    #
    # This merging process is similar to repeatedly merging pairs of equal numbers into a higher number.
    #
    # We want to find minimal insertions to make the sequence good.
    #
    # Approach:
    # We simulate the merging process greedily from left to right, using a stack.
    #
    # For each element in the sequence:
    #   - Push it onto the stack.
    #   - While the top two elements are equal, pop them and push their incremented value.
    #
    # After processing all elements, the stack represents the merged form of the original sequence.
    #
    # To make the sequence good, we want to be able to merge the entire sequence into a single element.
    #
    # The minimal insertions needed correspond to the minimal number of elements to add to enable merges that reduce the stack to length 1.
    #
    # We can think in terms of the stack after processing the original sequence:
    # - If the stack length is 1, no insertions needed.
    # - Otherwise, we need to insert elements to enable merges that reduce the stack length to 1.
    #
    # The minimal insertions needed is stack length - 1.
    #
    # Why?
    # Because each insertion can help merge two elements, reducing the stack length by 1.
    #
    # This is confirmed by the sample tests.
    #
    # So the answer for each test case is len(stack) - 1 after merging the original sequence.
    
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        
        stack = []
        for x in A:
            stack.append(x)
            while len(stack) >= 2 and stack[-1] == stack[-2]:
                val = stack.pop()
                stack.pop()
                stack.append(val + 1)
        
        # minimal insertions needed:
        print(len(stack) - 1)

if __name__ == "__main__":
    solve()