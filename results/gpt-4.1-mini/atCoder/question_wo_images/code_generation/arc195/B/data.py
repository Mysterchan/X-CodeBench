def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # We want to find if there exists a value S such that after filling -1s and rearranging A,
    # for all i: A_i + B_i = S, with A_i, B_i >= 0.

    # Key observations:
    # - We can rearrange A arbitrarily.
    # - We can assign any non-negative integer to positions where A_i or B_i = -1.
    # - After rearrangement, the pairs (A_i, B_i) correspond to some permutation of A and original B.
    # - We want all sums A_i + B_i = S for some S.

    # Let's analyze the problem:

    # For each i, define:
    #   If A_i != -1 and B_i != -1, then sum_i = A_i + B_i is fixed.
    #   If one of them is -1, sum_i can be any value >= the known part (since the unknown can be assigned).
    #   If both are -1, sum_i can be any non-negative integer.

    # Since we can rearrange A arbitrarily, the sums after rearrangement correspond to pairing elements of A and B.

    # Let's separate A into known and unknown:
    known_A = [a for a in A if a != -1]
    unknown_A_count = A.count(-1)

    # Similarly for B:
    known_B = [b for b in B if b != -1]
    unknown_B_count = B.count(-1)

    # We want to find if there exists S and assignments to unknowns and a permutation of A such that:
    # For all i, A_i + B_i = S, A_i >= 0, B_i >= 0.

    # Let's consider the sums for pairs where both A_i and B_i are known:
    fixed_sums = []
    for i in range(N):
        if A[i] != -1 and B[i] != -1:
            fixed_sums.append(A[i] + B[i])

    # If there are fixed sums, they must all be equal to the same S.
    if fixed_sums:
        S = fixed_sums[0]
        if any(s != S for s in fixed_sums):
            print("No")
            return
    else:
        # No fixed sums, so S can be any non-negative integer.
        # Let's try S = 0 as a candidate (minimum sum).
        S = 0

    # Now, for each i, we want to check if it's possible to assign values to unknowns and rearrange A to get sum S.

    # Let's analyze the constraints for each position i:

    # Case 1: A_i != -1, B_i != -1
    # sum_i = A_i + B_i = S (already checked above)

    # Case 2: A_i != -1, B_i == -1
    # We want B_i = S - A_i >= 0
    # So S >= A_i

    # Case 3: A_i == -1, B_i != -1
    # We want A_i = S - B_i >= 0
    # So S >= B_i

    # Case 4: A_i == -1, B_i == -1
    # We can assign A_i and B_i such that A_i + B_i = S, both >= 0
    # Always possible for S >= 0

    # So for all i where one side is known and the other is -1, S must be >= known value.

    # Let's find the minimal S that satisfies these constraints:
    min_S = S
    for i in range(N):
        if A[i] != -1 and B[i] == -1:
            if S < A[i]:
                print("No")
                return
        elif A[i] == -1 and B[i] != -1:
            if S < B[i]:
                print("No")
                return

    # Now, we must check if we can rearrange A to satisfy the sums.

    # Since we can rearrange A arbitrarily, let's consider the known A values and unknown A values.

    # We have known_A values fixed, unknown_A_count unknowns to assign.

    # We want to pair A and B so that A_i + B_i = S for all i.

    # Let's consider the B array fixed (no rearrangement allowed on B).

    # For each i:
    # If B_i != -1, then A_i = S - B_i (must be >= 0)
    # If B_i == -1, then A_i can be any non-negative integer (since B_i can be assigned)

    # So the required A values after rearrangement are:
    required_A = []
    for i in range(N):
        if B[i] != -1:
            val = S - B[i]
            if val < 0:
                print("No")
                return
            required_A.append(val)
        else:
            # B_i == -1, so A_i can be any non-negative integer
            # We can assign A_i = 0 here (minimum)
            required_A.append(0)

    # Now, we want to check if we can rearrange A to match required_A.

    # We have known_A values fixed, unknown_A_count unknowns to assign.

    # The unknown A values can be assigned any non-negative integer.

    # So, the problem reduces to:
    # Can we assign unknown_A_count non-negative integers to unknown A positions,
    # and rearrange the entire A array (known + assigned unknowns) to match required_A?

    # Since we can rearrange A arbitrarily, the order doesn't matter.

    # Let's sort known_A and required_A.

    known_A.sort()
    required_A.sort()

    # We want to check if we can assign unknown_A_count values to unknown A positions,
    # so that the multiset of known_A + assigned unknowns equals required_A.

    # Let's try to match known_A to required_A:

    # For each known_A[i], it must be <= required_A[i], because we can only assign unknowns to fill the gap.

    # If known_A[i] > required_A[i], it's impossible.

    # The difference required_A[i] - known_A[i] must be covered by unknown A assignments.

    # Sum of all differences must be <= sum of unknown A assignments.

    # Since unknown A assignments can be any non-negative integers, sum of unknown A assignments can be any non-negative integer.

    # So, if for all i, known_A[i] <= required_A[i], then we can assign unknown A values to fill the gaps.

    # Also, the number of unknown A values is unknown_A_count.

    # We must ensure that the number of required_A elements that are greater than known_A elements is at least unknown_A_count.

    # Actually, the unknown A values can be assigned arbitrarily, so the only constraint is that known_A[i] <= required_A[i] for all i < len(known_A).

    # The remaining required_A elements correspond to unknown A positions, which we can assign freely.

    # So, if len(known_A) > len(required_A), impossible (should not happen since both length N).

    # Let's check the condition:

    for i in range(len(known_A)):
        if known_A[i] > required_A[i]:
            print("No")
            return

    # If all checks passed, print Yes
    print("Yes")


if __name__ == "__main__":
    main()