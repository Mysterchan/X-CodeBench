import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    # We want to find X such that:
    # (X XOR N) == (X mod N)
    #
    # Let r = X mod N, q = X // N
    # Then X = q*N + r
    #
    # Condition:
    # (X XOR N) == r
    # => (q*N + r) XOR N == r
    # => (q*N) XOR (r XOR N) == r
    # => (q*N) XOR (r XOR N) == r
    #
    # Rearranged:
    # (q*N) XOR (r XOR N) = r
    #
    # Let's analyze bitwise:
    #
    # Since q*N is multiple of N, its lower bits (less than bit length of N) are zero.
    # r < N, so r fits in bits less than bit length of N.
    #
    # Let M = bit length of N
    # For bits < M:
    #   (q*N) has 0 bits
    #   So (q*N) XOR (r XOR N) = r
    #   => (r XOR N) = r
    #   => N & bits < M = 0
    # But N has bit M-1 set, so bits < M are bits 0..M-1
    #
    # Actually, let's try to find all r in [0, N-1] satisfying:
    # (r XOR N) XOR (q*N) = r
    # Since q*N has zeros in bits < M, the lower M bits of (q*N) are zero.
    #
    # So lower M bits:
    # (r XOR N) = r
    # => N & ((1<<M)-1) = 0
    # But N has bit M-1 set, so this is impossible unless r XOR N = r
    #
    # So (r XOR N) = r
    # => N & r = 0
    #
    # So for r in [0, N-1], condition is:
    # N & r == 0
    #
    # For such r, the condition reduces to:
    # (q*N) XOR (r XOR N) = r
    # => (q*N) XOR (r XOR N) = r
    # => (q*N) = r XOR (r XOR N) = N
    #
    # So (q*N) = N
    # => q*N = N
    # => q = 1
    #
    # But q can be any integer >= 0, so let's check the original condition again:
    #
    # (X XOR N) = r
    # X = q*N + r
    # (q*N + r) XOR N = r
    # => (q*N) XOR (r XOR N) = r
    #
    # Since q*N is multiple of N, and r < N,
    # bits of q*N and r are disjoint in lower M bits.
    #
    # Let's try to find all r such that:
    # (r XOR N) < N and (r XOR N) == r
    # This implies N & r == 0
    #
    # So r must satisfy N & r == 0
    #
    # For such r, let's check:
    # (q*N + r) XOR N = r
    # => (q*N) XOR (r XOR N) = r
    # => (q*N) XOR (r XOR N) = r
    #
    # Since r XOR N = r XOR N, and q*N is multiple of N,
    # Let's test q=0:
    # (0) XOR (r XOR N) = r
    # => r XOR N = r
    # => N & r = 0
    #
    # So for q=0, condition holds if N & r == 0
    #
    # For q>0:
    # (q*N) XOR (r XOR N) = r
    # => (q*N) = r XOR (r XOR N) = N
    # So q*N = N => q=1
    #
    # So q can only be 0 or 1 for condition to hold.
    #
    # Let's test q=1:
    # (N) XOR (r XOR N) = r
    # => N XOR r XOR N = r
    # => r = r
    # So q=1 also works for any r with N & r == 0
    #
    # For q>1:
    # q*N XOR (r XOR N) = r
    # q*N XOR (r XOR N) = r
    # => q*N = r XOR (r XOR N) = N
    # So q*N = N => q=1
    #
    # So q can only be 0 or 1.
    #
    # So all X = q*N + r with q in {0,1} and r in [0,N-1] with N & r == 0 satisfy condition.
    #
    # But X must be positive integer.
    #
    # So possible X are:
    # For q=0: X = r, r in [1, N-1], N & r == 0
    # For q=1: X = N + r, r in [0, N-1], N & r == 0
    #
    # Note: For q=0, r=0 => X=0 (not positive), exclude.
    #
    # So the set of compatible X is:
    # S = {r | 1 <= r < N, N & r == 0} ∪ {N + r | 0 <= r < N, N & r == 0}
    #
    # Let's count how many such r exist:
    # The number of r in [0, N-1] with N & r == 0 is 2^(number of zero bits in N)
    #
    # Because for each bit where N has 0, r can be 0 or 1, for bits where N has 1, r must be 0.
    #
    # Let zero_bits = number of zero bits in N in its binary representation (up to highest set bit)
    #
    # So total count of r in [0, N-1] with N & r == 0 is 2^zero_bits
    #
    # So total compatible X count:
    # For q=0: exclude r=0 => 2^zero_bits - 1
    # For q=1: all r => 2^zero_bits
    #
    # Total = (2^zero_bits - 1) + 2^zero_bits = 2^(zero_bits+1) - 1
    #
    # We want to find the K-th smallest compatible X.
    #
    # The compatible X sorted ascending:
    # First all r with q=0, r in [1, N-1], N & r == 0, sorted ascending
    # Then all N + r with r in [0, N-1], N & r == 0, sorted ascending
    #
    # So:
    # If K <= 2^zero_bits - 1:
    #   The K-th smallest is the K-th smallest r with N & r == 0 and r >= 1
    # Else if K <= 2^(zero_bits+1) - 1:
    #   The (K - (2^zero_bits - 1))-th smallest in the second group:
    #   That is the (K - (2^zero_bits - 1))-th smallest r with N & r == 0 (including 0)
    #   Then X = N + r
    # Else:
    #   Output -1
    #
    # To find the K-th smallest r with N & r == 0:
    # We can think of r as a number formed by bits only in positions where N has 0.
    # The bits where N has 1 must be zero in r.
    #
    # So we can map the bits of r to the zero bits of N.
    #
    # For example:
    # Let zero_positions = list of bit positions where N has 0 (from LSB to MSB)
    # Then r's bits correspond to bits of an integer idx in [0, 2^len(zero_positions)-1]
    #
    # So the idx-th number r with N & r == 0 is:
    # r = sum_{i} ((idx >> i) & 1) << zero_positions[i]
    #
    # For the first group (q=0), r >= 1, so idx in [1, 2^zero_bits - 1]
    # For the second group (q=1), idx in [0, 2^zero_bits - 1]
    #
    # Implementation plan:
    # 1. Find zero_positions of N
    # 2. Calculate total_count = 2^(zero_bits+1) - 1
    # 3. If K > total_count: print -1
    # 4. Else if K <= 2^zero_bits - 1:
    #    idx = K (since idx starts from 1)
    #    r = construct_r(idx)
    #    print r
    # 5. Else:
    #    idx = K - (2^zero_bits - 1) - 1 (since idx starts from 0)
    #    r = construct_r(idx)
    #    print N + r

    # Step 1: find zero_positions
    zero_positions = []
    bit_len = N.bit_length()
    for i in range(bit_len):
        if (N & (1 << i)) == 0:
            zero_positions.append(i)
    zero_bits = len(zero_positions)

    total_count = (1 << (zero_bits + 1)) - 1
    if K > total_count:
        print(-1)
        continue

    def construct_r(idx):
        r = 0
        for i, pos in enumerate(zero_positions):
            if (idx >> i) & 1:
                r |= (1 << pos)
        return r

    first_group_count = (1 << zero_bits) - 1
    if K <= first_group_count:
        # K-th smallest in first group, idx = K (1-based)
        r = construct_r(K)
        print(r)
    else:
        # In second group
        idx = K - first_group_count - 1  # zero-based
        r = construct_r(idx)
        print(N + r)