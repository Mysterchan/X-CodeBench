import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    # Count the number of zero bits in N (up to the highest set bit)
    # Because the compatible numbers X satisfy:
    # X XOR N = X % N
    # Let r = X % N, then X = m*N + r for some m >= 0
    # The condition becomes:
    # (m*N + r) XOR N = r
    # => (m*N) XOR N XOR r = r
    # => (m*N) XOR N = 0 (since XOR r on both sides)
    # But this is not straightforward.
    #
    # Let's analyze the problem:
    #
    # Given X XOR N = X % N
    # Let r = X % N, so X = q*N + r
    # Then:
    # (q*N + r) XOR N = r
    # => (q*N) XOR N XOR r = r
    # => (q*N) XOR N = 0 (since XOR r on both sides)
    #
    # So (q*N) XOR N = 0
    # => (q*N) = N
    # But q*N can be multiple of N, so let's check the bits.
    #
    # Let's try to find all X such that:
    # X XOR N = X % N
    #
    # Let r = X % N, so 0 <= r < N
    # Then X = m*N + r for some m >= 0
    #
    # Substitute:
    # (m*N + r) XOR N = r
    # => (m*N) XOR N XOR r = r
    # => (m*N) XOR N = 0 (since XOR r on both sides)
    #
    # So (m*N) XOR N = 0
    #
    # Let's denote A = m*N
    # Then A XOR N = 0
    # => A = N
    #
    # But A = m*N, so m*N = N
    # => m = 1
    #
    # So only m=1 satisfies this? That would mean only X = N + r
    #
    # But from the sample input, for N=2:
    # X=2 is compatible (XOR=0, remainder=0)
    # X=3 is compatible (XOR=1, remainder=1)
    #
    # So let's try to find a better approach.
    #
    # Let's rewrite the condition:
    # X XOR N = X % N
    #
    # Let r = X % N
    # Then X = q*N + r
    #
    # Substitute:
    # (q*N + r) XOR N = r
    # => (q*N) XOR N XOR r = r
    # => (q*N) XOR N = 0 (since XOR r on both sides)
    #
    # So (q*N) XOR N = 0
    #
    # Let's analyze (q*N) XOR N = 0
    # => (q*N) = N
    #
    # This is only true if q=1
    #
    # But from the sample, q=0 also works:
    # For X=2, q=1, r=0
    # For X=3, q=1, r=1
    #
    # Wait, for X=3:
    # 3 XOR 2 = 1
    # 3 % 2 = 1
    # So condition holds.
    #
    # For X=1:
    # 1 XOR 2 = 3
    # 1 % 2 = 1
    # Not equal.
    #
    # So the condition is:
    # (q*N + r) XOR N = r
    # => (q*N) XOR N XOR r = r
    # => (q*N) XOR N = 0
    #
    # So (q*N) XOR N = 0
    #
    # Let's write N in binary and q*N in binary.
    #
    # For (q*N) XOR N = 0, it means q*N = N
    #
    # So q*N = N
    # => q=1
    #
    # So q=1
    #
    # So X = N + r
    #
    # So all X of the form N + r, where 0 <= r < N, satisfy:
    # (N + r) XOR N = r
    #
    # Let's check:
    # (N + r) XOR N = (N XOR N) XOR r = 0 XOR r = r
    #
    # So all X = N + r, 0 <= r < N satisfy the condition.
    #
    # But the problem states X is positive integer.
    #
    # So the compatible numbers are all integers from N to 2N - 1 inclusive.
    #
    # So the compatible numbers are:
    # X in [N, 2N - 1]
    #
    # There are exactly N such numbers.
    #
    # So if K > N, print -1
    # else print N + (K - 1)
    
    if K > N:
        print(-1)
    else:
        print(N + (K - 1))