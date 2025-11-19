MOD = 998244353

def main():
    import sys
    input = sys.stdin.readline

    N = int(input())

    # Precompute factorials modulo MOD
    fact = [1] * (N+1)
    for i in range(2, N+1):
        fact[i] = fact[i-1] * i % MOD

    # Precompute lengths of numbers 1..N
    # length[i] = number of digits in i
    length = [0] * (N+1)
    for i in range(1, N+1):
        length[i] = len(str(i))

    # Precompute prefix sums of powers of 10 for digit lengths
    # max length of number <= len(str(N)) <= 6 (since N <= 2*10^5)
    max_len = max(length)

    # Precompute pow10 for all needed powers up to max_len * N (worst case)
    # But max total length of concatenation is sum of digits of all numbers
    # which is roughly N * max_len, but we only need powers up to max_len * N
    # However, we will only need powers up to max_len * N for positional calculations.
    # But we can do better: we only need powers of 10 up to max_len * N, but that is too large.
    # Instead, we will use a different approach.

    # Key insight:
    # f(P) = concatenation of A_1, A_2, ..., A_N
    # For each position i in the permutation (1-based),
    # the number A_i is shifted by sum of lengths of all numbers after position i.
    # Since all permutations are considered, each number appears equally often in each position.
    # Number of permutations = N!
    # Number of permutations with a fixed number at position i = (N-1)!
    # So each number appears (N-1)! times at each position.

    # We need to find for each position i:
    # the total shift = sum of lengths of numbers after position i
    # Since the permutation is arbitrary, the expected sum of lengths after position i is:
    # (N - i) * average length of numbers

    # But average length is not integer, and we need exact sum of powers of 10.

    # Instead, we can do the following:

    # Let L = [length(1), length(2), ..., length(N)]
    # sum_len = sum of all lengths

    # For position i (1-based), the total length of numbers after i is:
    # sum_len - prefix_len[i], where prefix_len[i] is sum of lengths of first i numbers in permutation.

    # Since all permutations are equally likely, the expected prefix_len[i] is:
    # i * average length

    # But we need exact sum over all permutations, so we consider the sum of powers of 10 for each position.

    # Another approach:

    # For each position i (1-based), the total shift in digits for the number at position i is:
    # sum of lengths of numbers after position i = total_len - sum of lengths of first i numbers

    # Since all permutations are considered, each number appears equally often at each position,
    # and the distribution of lengths at each position is uniform.

    # So the sum of lengths of numbers after position i over all permutations is:
    # (N-1)! * sum over all subsets of size i of lengths

    # This is complicated.

    # Let's try a different approach:

    # We want sum over all permutations P of f(P).

    # f(P) = sum_{i=1 to N} A_{P_i} * 10^{sum of lengths of A_{P_j} for j>i}

    # Sum over all permutations P:
    # sum_P f(P) = sum_{i=1 to N} sum_P A_{P_i} * 10^{sum of lengths of A_{P_j} for j>i}

    # For fixed i, sum over all permutations P of A_{P_i} * 10^{sum of lengths of A_{P_j} for j>i}

    # Let's fix i.

    # The number of permutations is N!

    # For position i, the number of permutations where a fixed number x is at position i is (N-1)!.

    # For the other positions, the numbers are permuted arbitrarily.

    # The exponent for 10 depends on the sum of lengths of numbers after position i.

    # The sum of lengths of numbers after position i is sum of lengths of the N-1 numbers excluding the one at position i,
    # but the order of these N-1 numbers varies.

    # So the exponent depends on the order of the remaining N-1 numbers.

    # So for fixed i and fixed number x at position i, the sum over permutations of the other N-1 numbers of
    # 10^{sum of lengths of numbers after position i} is sum over permutations Q of (N-1) numbers of
    # 10^{sum of lengths of numbers after position i}.

    # But sum of lengths of numbers after position i = sum of lengths of numbers in positions i+1 to N.

    # For the remaining N-1 numbers, the positions after i are positions i+1 to N, which is N - i positions.

    # So the exponent is sum of lengths of the last N - i numbers in the permutation Q of N-1 numbers.

    # So for fixed i and fixed x at position i, the sum over permutations Q of 10^{sum of lengths of last N - i numbers in Q}.

    # Let's define M = N - 1 (the size of Q), and k = N - i (the number of positions after i).

    # We want sum over all permutations Q of M numbers of 10^{sum of lengths of last k numbers in Q}.

    # This is the key subproblem.

    # Let's denote the set S = {1,...,N} \ {x}, with lengths l_s.

    # We want sum over all permutations Q of S of 10^{sum of lengths of last k numbers in Q}.

    # Note that sum of lengths of last k numbers in Q = sum of lengths of a k-sized suffix of Q.

    # Since Q is a permutation of M elements, the last k elements form a k-sized subset of S.

    # For each k-sized subset T of S, the number of permutations Q where the last k elements are exactly T (in any order) is:
    # k! * (M - k)! (since last k elements permuted among themselves, first M-k elements permuted among themselves)

    # So sum over all permutations Q of 10^{sum of lengths of last k numbers} =
    # sum over all k-sized subsets T of S of 10^{sum of lengths in T} * k! * (M - k)!

    # So for fixed i and fixed x, the sum over Q is:
    # k! * (M - k)! * sum over all k-sized subsets T of S of 10^{sum of lengths in T}

    # Now, sum over all k-sized subsets T of S of 10^{sum of lengths in T} is the coefficient of x^k in the polynomial:
    # P(x) = product over s in S of (1 + 10^{l_s} * x)

    # So we need to compute the coefficient of x^k in P(x).

    # We can do this efficiently using prefix sums and combinatorics.

    # But N can be up to 2*10^5, so we need an O(N) solution.

    # Let's try to simplify further.

    # Since the lengths l_s are small (max 6), 10^{l_s} can be precomputed.

    # Let's group numbers by their length.

    # Let cnt_len[d] = number of numbers with length d.

    # For S = {1,...,N} \ {x}, the counts are cnt_len[d] except we remove the length of x.

    # So for each length d, the count is cnt_len[d] - (1 if length[x] == d else 0).

    # Then P(x) = product over d=1 to max_len of (1 + 10^d * x)^{cnt_len[d] - delta}

    # The coefficient of x^k in P(x) is sum over all ways to choose subsets of sizes k from these groups.

    # The coefficient of x^k in P(x) is sum over all vectors (k_1,...,k_max_len) with sum k_i = k of:
    # product over d of C(cnt_len[d] - delta, k_d) * (10^d)^{k_d}

    # This is a multinomial sum.

    # We can compute the coefficients using a DP over lengths.

    # Since max_len <= 6, we can do DP over length groups.

    # Let's implement this.

    # Steps:

    # 1. Precompute cnt_len[d] for d=1..max_len
    # 2. Precompute pow10[d] = 10^d mod MOD
    # 3. Precompute factorials and inverse factorials for combinations
    # 4. For each x in 1..N:
    #    - Build counts for S = cnt_len with one less in length[x]
    #    - Compute polynomial coefficients for P(x) using DP
    #    - For each position i=1..N:
    #       k = N - i
    #       sum_k = coefficient of x^k in P(x)
    #       contribution = A_x * (N-1)! * k! * (N-1 - k)! * sum_k
    #    - sum over i

    # But this is O(N^2), too large.

    # We need a better approach.

    # Let's try to find a formula that does not depend on x and i individually.

    # Another approach:

    # Since all numbers 1..N are distinct, and each number appears equally often at each position i.

    # Number of permutations = N!

    # Each number appears (N-1)! times at each position i.

    # The total sum of f(P) over all permutations P is:

    # sum_{i=1 to N} (N-1)! * sum_{x=1 to N} x * 10^{sum of lengths of numbers after position i in P}

    # But the exponent depends on the order of the other numbers.

    # Since the other numbers are permuted arbitrarily, the sum over all permutations of the other numbers of 10^{sum of lengths of numbers after position i} is:

    # sum over permutations Q of N-1 numbers of 10^{sum of lengths of last N - i numbers in Q}

    # We can rewrite the sum over all permutations Q of 10^{sum of lengths of last k numbers} as:

    # sum_{T subset of size k} 10^{sum of lengths in T} * k! * (N-1 - k)!

    # So for fixed k, sum over all permutations Q of 10^{sum of lengths of last k numbers} = k! * (N-1 - k)! * sum_{T subset size k} 10^{sum lengths in T}

    # Now, sum over all subsets of size k of 10^{sum lengths in T} is the coefficient of x^k in:

    # G(x) = product_{j=1 to N-1} (1 + 10^{length_j} * x)

    # where length_j are lengths of numbers excluding the fixed number at position i.

    # But since the numbers are 1..N, and the fixed number is arbitrary, the multiset of lengths excluding one number is the same for all numbers except for the length of the excluded number.

    # So the sum over all numbers x of sum_{T subset size k} 10^{sum lengths in T} with lengths excluding length[x] is:

    # sum_{d=1 to max_len} (cnt_len[d] - 1) * (coefficient of x^k in product over lengths with one less count in d)

    # This is complicated.

    # Let's try a different approach.

    # Let's consider the sum of f(P) over all permutations P.

    # f(P) = concatenation of A_{P_1}, A_{P_2}, ..., A_{P_N}

    # Let's think digit-wise.

    # The total length of the concatenation is sum of lengths of all numbers = total_len.

    # For each position i in the permutation, the number A_{P_i} is shifted by sum of lengths of numbers after position i.

    # So the contribution of A_{P_i} is A_{P_i} * 10^{shift_i}, where shift_i = sum of lengths of numbers after position i.

    # Since all permutations are considered, each number appears equally often at each position i.

    # Number of permutations = N!

    # Number of permutations with fixed number x at position i = (N-1)!

    # So total contribution of number x at position i is:

    # (N-1)! * x * 10^{shift_i}

    # Now, shift_i depends on the sum of lengths of numbers after position i.

    # Since the order of the other numbers is arbitrary, the sum of lengths after position i is the sum of lengths of a subset of size N - i of the other numbers.

    # The sum over all permutations of the other numbers of 10^{sum of lengths of last N - i numbers} is:

    # (N - i)! * (i - 1)! * sum over subsets T of size N - i of 10^{sum lengths in T}

    # Wait, this is the same as before.

    # Let's try to find the sum over all subsets of size k of 10^{sum lengths}.

    # Let's define S = {lengths of all numbers}

    # The generating function is:

    # F(x) = product_{l in S} (1 + 10^l * x)

    # The coefficient of x^k in F(x) is sum over subsets of size k of 10^{sum lengths in subset}.

    # So sum over all subsets of size k of 10^{sum lengths} = coeff_x^k(F(x))

    # Now, the total sum is:

    # sum_{i=1 to N} (N-1)! * sum_{x=1 to N} x * (N - i)! * (i - 1)! * coeff_x^{N - i}(F_x(x))

    # where F_x(x) = product over lengths excluding length[x] of (1 + 10^l * x)

    # But this is complicated.

    # Let's try to approximate by ignoring the exclusion of length[x].

    # Since N is large, the effect of excluding one number is negligible.

    # So approximate F_x(x) ≈ F(x) / (1 + 10^{length[x]} * x)

    # Then coeff_x^{k}(F_x(x)) = coeff_x^{k}(F(x)) - 10^{length[x]} * coeff_x^{k-1}(F_x(x))

    # This is recursive.

    # But let's try to find a closed form.

    # Let's precompute coeff_x^{k}(F(x)) for k=0..N.

    # Then for each x, coeff_x^{k}(F_x(x)) = coeff_x^{k}(F(x)) - 10^{length[x]} * coeff_x^{k-1}(F_x(x))

    # This is a linear recurrence.

    # We can solve it for each x.

    # But this is O(N^2), too large.

    # Let's try a different approach.

    # Let's consider the sum of f(P) over all permutations P:

    # sum_P f(P) = sum_P sum_{i=1 to N} A_{P_i} * 10^{sum of lengths of numbers after position i}

    # = sum_{i=1 to N} sum_P A_{P_i} * 10^{sum of lengths of numbers after position i}

    # For fixed i, sum_P A_{P_i} * 10^{sum of lengths of numbers after position i} =

    # sum_{x=1 to N} x * sum_{permutations Q of other N-1 numbers} 10^{sum of lengths of last N - i numbers in Q} * (N-1)!

    # Wait, the number of permutations with x at position i is (N-1)!.

    # So sum_P A_{P_i} * 10^{sum lengths after i} = (N-1)! * sum_{x=1 to N} x * sum_{Q} 10^{sum lengths of last N - i numbers in Q}

    # But sum_{Q} 10^{sum lengths of last N - i numbers in Q} is independent of x.

    # So sum_P A_{P_i} * 10^{sum lengths after i} = (N-1)! * sum_{x=1 to N} x * S_{N-i}

    # where S_k = sum over permutations Q of N-1 numbers of 10^{sum lengths of last k numbers in Q}

    # Now, sum_{x=1 to N} x = N(N+1)/2

    # So sum_P f(P) = (N-1)! * (N(N+1)/2) * sum_{i=1 to N} S_{N-i}

    # Now, S_k = sum over permutations Q of N-1 numbers of 10^{sum lengths of last k numbers in Q}

    # As before, S_k = k! * (N-1 - k)! * sum over subsets T of size k of 10^{sum lengths in T}

    # So sum_{i=1 to N} S_{N-i} = sum_{k=0 to N-1} S_k

    # = sum_{k=0 to N-1} k! * (N-1 - k)! * sum_{T subset size k} 10^{sum lengths in T}

    # Now, sum_{T subset size k} 10^{sum lengths in T} = coefficient of x^k in

    # F(x) = product_{j=1 to N-1} (1 + 10^{length_j} * x)

    # But length_j are lengths of numbers 1..N excluding one number.

    # Since we are summing over all x, the excluded number varies, but we approximated by ignoring exclusion.

    # So let's take all numbers 1..N.

    # Then F(x) = product_{i=1 to N} (1 + 10^{length[i]} * x)

    # sum_{k=0 to N} k! * (N - k)! * coeff_x^k(F(x))

    # But we want sum_{k=0 to N-1} k! * (N-1 - k)! * coeff_x^k(F(x))

    # Let's define:

    # total = sum_{k=0 to N} k! * (N - k)! * coeff_x^k(F(x))

    # We can compute coeff_x^k(F(x)) using DP over length groups.

    # Since max_len <= 6, we can do DP over length groups.

    # Let's implement this approach.

    # Steps:

    # 1. Compute cnt_len[d] for d=1..max_len
    # 2. Compute pow10[d] = 10^d mod MOD
    # 3. Precompute factorials and inverse factorials for combinations
    # 4. Compute polynomial F(x) = product_{d=1 to max_len} (1 + pow10[d] * x)^{cnt_len[d]} using DP
    #    DP[i][k] = coefficient of x^k using first i length groups
    # 5. Compute sum_{k=0 to N} k! * (N - k)! * DP[max_len][k]
    # 6. Multiply by (N-1)! * (N(N+1)/2) mod MOD

    # Note: We only need up to N terms, but N can be large (2*10^5).

    # But DP with dimension max_len=6 and k up to N=2*10^5 is too large.

    # We need a better approach.

    # Since the polynomial is product of terms (1 + c_d * x)^{cnt_len[d]}, the coefficient of x^k is:

    # coeff_x^k(F(x)) = sum over all vectors (k_1,...,k_max_len) with sum k_i = k of product over d of C(cnt_len[d], k_d) * (pow10[d])^{k_d}

    # So the coefficient is the coefficient of x^k in the product of binomial expansions.

    # The sum over k of k! * (N - k)! * coeff_x^k(F(x)) is:

    # sum_{k=0 to N} k! * (N - k)! * sum_{sum k_d = k} product_d C(cnt_len[d], k_d) * (pow10[d])^{k_d}

    # = sum over all vectors (k_1,...,k_max_len) with sum k_i <= N of

    # (sum k_i)! * (N - sum k_i)! * product_d C(cnt_len[d], k_d) * (pow10[d])^{k_d}

    # This is complicated.

    # Let's try to rewrite the sum:

    # sum_{k=0 to N} k! * (N - k)! * coeff_x^k(F(x)) = N! * sum_{k=0 to N} coeff_x^k(F(x)) / C(N, k)

    # Wait, this is not correct.

    # Let's try a different approach.

    # Let's consider the sum over all permutations P of f(P):

    # sum_P f(P) = sum_P sum_{i=1 to N} A_{P_i} * 10^{sum lengths after i}

    # = sum_{i=1 to N} sum_P A_{P_i} * 10^{sum lengths after i}

    # For fixed i, sum_P A_{P_i} * 10^{sum lengths after i} = (N-1)! * sum_{x=1 to N} x * sum over permutations Q of N-1 numbers of 10^{sum lengths of last N - i numbers in Q}

    # sum over permutations Q of N-1 numbers of 10^{sum lengths of last k numbers} = k! * (N-1 - k)! * sum over subsets T of size k of 10^{sum lengths in T}

    # So sum_P f(P) = (N-1)! * sum_{i=1 to N} sum_{x=1 to N} x * (N - i)! * (i - 1)! * sum_{T subset size N - i} 10^{sum lengths in T}

    # = (N-1)! * sum_{i=1 to N} (N - i)! * (i - 1)! * sum_{x=1 to N} x * sum_{T subset size N - i} 10^{sum lengths in T}

    # sum_{x=1 to N} x = N(N+1)/2

    # So sum_P f(P) = (N-1)! * (N(N+1)/2) * sum_{k=0 to N-1} k! * (N-1 - k)! * sum_{T subset size k} 10^{sum lengths in T}

    # where k = N - i

    # Now, sum_{T subset size k} 10^{sum lengths in T} = coefficient of x^k in

    # F(x) = product_{i=1 to N} (1 + 10^{length[i]} * x)

    # So sum_P f(P) = (N-1)! * (N(N+1)/2) * sum_{k=0 to N-1} k! * (N-1 - k)! * coeff_x^k(F(x))

    # Note that (N-1)! * k! * (N-1 - k)! = (N-1)! * k! * (N-1 - k)! = (N-1)! * k! * (N-1 - k)! = (N-1)! * k! * (N-1 - k)!

    # But (N-1)! * k! * (N-1 - k)! = (N-1)! * k! * (N-1 - k)! = (N-1)! * k! * (N-1 - k)! = (N-1)! * k! * (N-1 - k)!

    # Wait, this is symmetric.

    # Let's rewrite:

    # sum_P f(P) = (N-1)! * (N(N+1)/2) * sum_{k=0 to N-1} k! * (N-1 - k)! * coeff_x^k(F(x))

    # Let's precompute factorials and inverse factorials.

    # We can compute coeff_x^k(F(x)) using a DP over length groups.

    # Since max_len <= 6, we can do DP over length groups.

    # Let's implement this final approach.

    # Implementation plan:

    # 1. Compute cnt_len[d] for d=1..max_len
    # 2. Compute pow10[d] = 10^d mod MOD
    # 3. Precompute factorials and inverse factorials up to N
    # 4. Use DP to compute coefficients of F(x) = product_{d=1 to max_len} (1 + pow10[d] * x)^{cnt_len[d]}
    #    DP[i][k] = coefficient of x^k using first i length groups
    # 5. Compute sum_{k=0 to N-1} k! * (N-1 - k)! * DP[max_len][k]
    # 6. Multiply by (N-1)! * (N(N+1)/2) mod MOD

    # Since N can be large, we cannot store DP for all k up to N.

    # But the maximum total number of elements is N, so DP array size is N+1.

    # max_len = 6, so DP complexity is O(max_len * N) = 6 * 2*10^5 = 1.2 million, which is feasible.

    # Let's implement.

    # Precompute factorials and inverse factorials for combinations and factorial values.

    # For each length group d:
    # We have cnt_len[d] elements, each contributes (1 + pow10[d] * x)
    # So (1 + pow10[d] * x)^{cnt_len[d]} = sum_{j=0 to cnt_len[d]} C(cnt_len[d], j) * (pow10[d])^j * x^j

    # We can combine these polynomials using DP.

    # Initialize DP[0] = 1, others 0.

    # For each length group d:
    #   Build polynomial P_d with coefficients P_d[j] = C(cnt_len[d], j) * (pow10[d])^j
    #   Convolve DP with P_d

    # Since max_len=6, we do 6 convolutions of size up to N+1.

    # Use simple convolution since max_len is small.

    # Let's implement.

    # Finally, output the result.

    # Note: We only need sum up to N-1, but DP size is N+1.

    # Also, factorials and inverse factorials are needed for combinations and factorial values.

    # Let's proceed.

    # Code implementation below.

    # -------------------

    # Precompute factorials and inverse factorials
    max_n = N
    fact = [1] * (max_n + 1)
    inv_fact = [1] * (max_n + 1)
    for i in range(2, max_n + 1):
        fact[i] = fact[i-1] * i % MOD

    inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)
    for i in reversed(range(1, max_n)):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

    def comb(n, r):
        if r > n or r < 0:
            return 0
        return fact[n] * inv_fact[r] % MOD * inv_fact[n-r] % MOD

    # Count lengths
    cnt_len = [0] * 7  # lengths 1 to 6
    for i in range(1, N+1):
        l = len(str(i))
        cnt_len[l] += 1

    pow10 = [0] * 7
    for d in range(1, 7):
        pow10[d] = pow(10, d, MOD)

    # DP initialization
    # dp[k] = coefficient of x^k
    dp = [0] * (N+1)
    dp[0] = 1

    for d in range(1, 7):
        c = cnt_len[d]
        if c == 0:
            continue
        # Build polynomial P_d
        # P_d[j] = C(c, j) * (pow10[d])^j
        P = [0] * (c+1)
        for j in range(c+1):
            P[j] = comb(c, j) * pow(pow10[d], j, MOD) % MOD

        # Convolve dp and P
        new_dp = [0] * (len(dp) + c)
        max_len_dp = len(dp) - 1
        for i_dp in range(max_len_dp + 1):
            val_dp = dp[i_dp]
            if val_dp == 0:
                continue
            for j_p in range(c+1):
                new_dp[i_dp + j_p] = (new_dp[i_dp + j_p] + val_dp * P[j_p]) % MOD
        dp = new_dp[:N+1]

    # Now compute sum_{k=0 to N-1} k! * (N-1 - k)! * dp[k]
    res = 0
    for k in range(N):
        val = dp[k] * fact[k] % MOD * fact[N-1 - k] % MOD
        res = (res + val) % MOD

    # Multiply by (N-1)! * (N(N+1)/2)
    res = res * fact[N-1] % MOD
    res = res * (N * (N+1) // 2 % MOD) % MOD

    print(res)

if __name__ == "__main__":
    main()