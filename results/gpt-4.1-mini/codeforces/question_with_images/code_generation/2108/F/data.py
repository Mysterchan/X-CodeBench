import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # The problem can be solved by simulating the process in a greedy manner:
    # We want the final array to be non-decreasing.
    # After knocking down tower i, a_i becomes 0 and the next a_i towers increase by 1.
    #
    # The key insight:
    # We can think of the final array as starting from all zeros,
    # and each tower i contributes a_i increments to the next a_i towers.
    #
    # Since the order of knocking down towers is fixed (each tower exactly once),
    # but the order can be chosen arbitrarily,
    # the best way to maximize MEX is to knock down towers in order from left to right,
    # applying increments as we go.
    #
    # We keep track of how many increments are "carried over" to each position.
    # For each tower i:
    #   - The current height is increments carried over so far.
    #   - We want the final height at i to be at least the current increments.
    #   - We add a_i increments to the next towers.
    #
    # After processing all towers, the final array is non-decreasing by construction.
    #
    # Then, the MEX is the smallest non-negative integer not in the final array.
    #
    # Implementation:
    # Use a variable "carry" to track increments to be added to current tower.
    # For each tower i:
    #   - The final height at i is max(carry, current height)
    #   - Then carry = max(carry, current height) - 1 (because we "use" one increment to move forward)
    #   - Add a_i increments to carry for the next towers.
    #
    # But since increments only affect next towers, we can simulate carry as:
    #   carry = max(carry, a[i])
    #   carry = max(carry - 1, 0)
    #
    # Finally, the maximum MEX is the maximum value of carry + 1.
    #
    # This approach is from editorial and known solutions.

    carry = 0
    for x in a:
        carry = max(carry, x)
        if carry > 0:
            carry -= 1
    print(carry + 1)