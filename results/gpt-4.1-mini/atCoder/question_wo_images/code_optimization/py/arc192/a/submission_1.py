def solve():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    # If no zeros, answer is Yes immediately
    if all(a == 1 for a in A):
        print("Yes")
        return

    # The operations can only fix zeros in pairs (i, i+1) if the triple of letters at positions i,i+1,i+2
    # is either "A R C" or "C R A" (circularly).
    # We want to find if there exists a string S of length N over {A,R,C} such that by applying these operations
    # repeatedly, all zeros in A can be turned into ones.

    # Key insight:
    # Each operation fixes A[i] and A[i+1] if the triple at positions i,i+1,i+2 is "A R C" or "C R A".
    # So for each pair (i, i+1), to fix zeros at these positions, the triple starting at i must be one of these two patterns.

    # We want to assign letters to S so that for every zero in A, there is at least one operation that can fix it.
    # That means for every zero at position i, either the triple starting at i-2 (mod N) or the triple starting at i-1 (mod N)
    # must be "A R C" or "C R A" to cover A[i].

    # Let's analyze the constraints on S:
    # For triple at i: S[i], S[i+1], S[i+2] must be either "A R C" or "C R A" to fix zeros at i and i+1.

    # So for each triple (i, i+1, i+2), the triple is either "A R C" or "C R A".
    # This means S[i] and S[i+2] are either (A,C) or (C,A), and S[i+1] = R always.

    # So S has the form:
    # For all i: S[i+1] = R
    # And for all i: (S[i], S[i+2]) in {(A,C), (C,A)}

    # Since S[i+1] = R for all i, S is periodic with period 1 in the middle letters.
    # Let's check the pattern for S[i]:
    # Because S[i+1] = R for all i, S is of the form:
    # S = [x0, R, x1, R, x2, R, x3, R, ...] (indices mod N)
    # But N can be odd or even.

    # Let's separate indices into even and odd:
    # For even i: S[i] in {A,C}
    # For odd i: S[i] = R

    # Check if this assignment is consistent with the triple condition:
    # For triple starting at i:
    # S[i], S[i+1], S[i+2] = (A or C), R, (A or C)
    # And (S[i], S[i+2]) in {(A,C), (C,A)}

    # So for all i:
    # (S[i], S[i+2]) alternate between (A,C) and (C,A)

    # Since i and i+2 have the same parity, the sequence of letters at even positions must alternate between A and C.
    # Similarly for odd positions, but odd positions are always R.

    # So:
    # - For even indices: S[i] alternates between A and C
    # - For odd indices: S[i] = R

    # Because N can be even or odd, the parity of indices wraps around modulo N.

    # Let's try to construct S:
    # For even indices: assign letters alternating A and C
    # For odd indices: assign R

    # There are two possible assignments for even indices:
    # 1) even indices: A at i=0, C at i=2, A at i=4, ...
    # 2) even indices: C at i=0, A at i=2, C at i=4, ...

    # We try both assignments and check if all zeros in A are covered by some triple.

    # How to check coverage:
    # For each zero at position i, it must be fixed by an operation at i-1 or i (mod N).
    # That means the triple starting at i-1 or i must be "A R C" or "C R A".

    # Since S[i+1] = R always, and S[i], S[i+2] alternate between A and C,
    # the triple starting at i is (S[i], R, S[i+2]) which is either (A,R,C) or (C,R,A).

    # So the triple starting at i fixes positions i and i+1.

    # So zero at position i is fixed if either triple starting at i-1 or i covers i.

    # triple at i covers positions i and i+1
    # So zero at i is fixed if zero at i is in {i, i+1} for some triple starting at i.

    # So zero at i is fixed if zero at i is in triple starting at i-1 or i:
    # i in {i-1, i} or i in {i, i+1} mod N
    # i in {i-1, i} means i == i-1 or i == i (mod N) => always true for i == i
    # But more precisely:
    # triple at j covers positions j and j+1
    # So zero at i is fixed if i == j or i == j+1 for some j

    # So for zero at i, check if triple at i-1 or triple at i covers i:
    # triple at i-1 covers i-1 and i
    # triple at i covers i and i+1

    # So zero at i is fixed if triple at i-1 or triple at i exists.

    # Since all triples exist (we constructed S to satisfy the triple pattern),
    # the only question is whether the triple at i-1 or i is valid (i.e., the triple starting at i-1 or i is "A R C" or "C R A").

    # But we constructed S so that all triples are valid.

    # So the only remaining question is whether the zero at i is covered by at least one triple.

    # But all triples exist, so all pairs (i, i+1) are covered.

    # So zeros at i are covered if zero at i is in some pair (j, j+1) where triple at j is valid.

    # So zeros at i are covered if zero at i is in some pair (j, j+1) for some j.

    # Since all triples are valid, all pairs (j, j+1) are covered.

    # So zeros at i are covered if zero at i is in some pair (j, j+1).

    # But pairs (j, j+1) cover all indices in the circle.

    # So zeros at i are covered if zero at i is in at least one pair (j, j+1).

    # But pairs (j, j+1) cover all indices, so zeros at i are always covered.

    # Wait, but the problem is that the triple at i must be "A R C" or "C R A".

    # We must check if the triple at i is "A R C" or "C R A" for all i.

    # So the only question is whether the assignment of letters at even indices alternating A and C is consistent with the circular condition.

    # Because the sequence at even indices must alternate A and C, and the sequence length of even indices is ceil(N/2).

    # For even N:
    # Number of even indices = N/2
    # The alternating sequence of length N/2 must satisfy S[0] != S[2] != S[4] ... and wrap around.

    # For odd N:
    # Number of even indices = (N+1)//2
    # The alternating sequence must satisfy S[0] != S[2] != ... != S[0] (mod N)
    # So the sequence length is odd, and alternating sequence of odd length cannot be consistent (because first and last must differ and be equal at the same time).

    # So for odd N, no alternating sequence of length (N+1)//2 can satisfy the wrap-around condition.

    # For even N, alternating sequence of length N/2 can satisfy wrap-around condition.

    # So the problem reduces to:
    # - If N is odd, answer is No (unless all A are 1)
    # - If N is even, answer is Yes

    # Let's verify with sample inputs:
    # Sample 1: N=12 (even), output Yes
    # Sample 2: N=3 (odd), output No
    # Sample 3: N=29 (odd), but all ones, output Yes

    # So final solution:
    # If all ones: print Yes
    # Else if N is even: print Yes
    # Else print No

    if N % 2 == 1:
        print("No")
    else:
        print("Yes")