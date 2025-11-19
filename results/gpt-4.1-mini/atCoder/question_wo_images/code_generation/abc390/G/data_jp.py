MOD = 998244353

import sys
input = sys.stdin.readline

N = int(input())

# f(P) = concatenation of permutation P of (1..N)
# We want sum of f(P) over all permutations P of (1..N), mod 998244353.

# Key observations:
# - Each number i (1 <= i <= N) is represented as string T_i without leading zeros.
# - Length of T_i = len(str(i))
# - When concatenated, the position of each number in the permutation affects the place values.
# - We want sum over all permutations P of f(P).

# Let's analyze the problem:

# Let L_i = length of str(i)
# For permutation P = (p_1, p_2, ..., p_N),
# f(P) = sum_{k=1 to N} p_k * 10^{sum_{j=k+1 to N} L_{p_j}}

# We want sum_{all permutations P} f(P).

# Number of permutations = N!

# For each position k (1-based), the digit p_k is equally likely to be any of the N numbers,
# but the place value depends on the sum of lengths of numbers after position k.

# The problem is complicated because the place value depends on the order of the numbers after position k.

# However, since all permutations are considered, the distribution of lengths after position k is uniform over all permutations of the remaining numbers.

# Let's define:
# - For position k, the sum of lengths of numbers after position k is sum of lengths of a random permutation of N-k numbers.

# The sum of lengths of all numbers is S = sum_{i=1 to N} L_i

# For position k:
# sum of lengths after position k = sum of lengths of N-k numbers chosen in some order.

# Since all permutations are equally likely, the expected sum of lengths after position k is the sum of lengths of any subset of size N-k.

# But we need the sum over all permutations, so we consider all permutations and sum the place values.

# Let's try to find a formula for the sum of 10^{sum of lengths after position k} over all permutations.

# Instead of dealing with the complicated place values, let's consider the problem from a different angle.

# Alternative approach:

# Each permutation corresponds to concatenation of numbers in some order.

# The sum over all permutations of f(P) is equal to sum over all permutations of the concatenated number.

# Let's consider the contribution of each number i at each position k.

# Number i appears at position k in (N-1)! permutations (since the other N-1 numbers permute freely).

# For each such permutation, the place value of i is 10^{sum of lengths of numbers after position k}.

# The sum of lengths of numbers after position k depends on which numbers are after position k.

# Since all permutations are considered, the set of numbers after position k is any subset of size N-k of the other numbers.

# So for fixed i and position k, the sum over all permutations where i is at position k of 10^{sum of lengths of numbers after position k} is:

# sum over all subsets S of size N-k of [other numbers] of 10^{sum_{j in S} L_j} * (N-k)! (permutations of S) * (k-1)! (permutations before position k)

# Because the order of numbers after position k is permuted in (N-k)! ways, and order before position k is (k-1)! ways.

# So total permutations with i at position k is (N-1)! = (k-1)! * (N-k)! * C(N-1, N-k)

# Wait, the number of permutations with i at position k and subset S after position k is (k-1)! * (N-k)! (orderings before and after), and the subset S is chosen from N-1 numbers.

# So total permutations with i at position k and subset S after position k is (k-1)! * (N-k)!.

# The total sum over all permutations with i at position k is:

# (k-1)! * (N-k)! * sum_{S subset of size N-k of [N]\{i}} 10^{sum_{j in S} L_j}

# Since i is fixed, the other numbers are N-1 numbers.

# So for each position k, we need sum over all subsets S of size N-k of 10^{sum of lengths in S}.

# Let's define:

# For the multiset of lengths L_j (j != i), define:

# F(m) = sum over all subsets S of size m of 10^{sum of lengths in S}

# We want F(N-k) for each k.

# Since i varies from 1 to N, but the lengths L_j are the same for all i except excluding i.

# But since N is large, we cannot exclude i each time.

# However, the difference is negligible because the sum over all i of the same function excluding i is complicated.

# Let's try to approximate by including all numbers.

# Let's consider the generating function:

# G(x) = product_{j=1 to N} (1 + x * 10^{L_j})

# The coefficient of x^m in G(x) is sum over all subsets of size m of 10^{sum of lengths in subset}.

# So F(m) = coefficient of x^m in G(x).

# But we want sum over subsets excluding i.

# But since the problem is symmetric, and the difference is small, let's try to find a formula that works.

# Let's try to find the sum over all permutations of f(P):

# sum_{P} f(P) = sum_{k=1 to N} sum_{i=1 to N} i * (k-1)! * (N-k)! * F_{-i}(N-k)

# where F_{-i}(m) is sum over subsets of size m of [N]\{i} of 10^{sum of lengths}.

# But this is complicated.

# Let's try a different approach.

# Let's consider the problem from the perspective of digits.

# Since the numbers are concatenated, the total length of the concatenated number is sum_{i=1 to N} L_i.

# Each permutation corresponds to a unique concatenation.

# The sum over all permutations of f(P) is sum over all permutations of the concatenated number.

# Let's consider the contribution of each digit position in the concatenated number.

# The concatenated number has total length S = sum L_i.

# Each position in the concatenated number corresponds to a digit from some number i.

# The problem is to find the sum of digits at each position over all permutations.

# But the digits of each number are fixed.

# The position of each digit depends on the order of the numbers in the permutation.

# Let's consider the problem in terms of digits:

# For each number i, with length L_i, its digits are d_{i,1}, d_{i,2}, ..., d_{i,L_i}.

# When number i is placed at position k in the permutation, its digits occupy positions:

# pos_start = sum_{j=1 to k-1} L_{p_j} + 1

# pos_end = pos_start + L_i - 1

# The place value of digit d_{i,m} is 10^{S - (pos_start + m - 1)}.

# We want sum over all permutations of sum over k=1 to N of sum over m=1 to L_i of d_{i,m} * 10^{S - (pos_start + m - 1)}.

# Since the order of numbers is permuted, the position pos_start depends on the sum of lengths of numbers before position k.

# The problem is complicated.

# Let's try to find a simpler approach.

# Let's consider the problem in terms of the contribution of each number i at each position k.

# The place value of number i at position k is 10^{sum of lengths of numbers after position k}.

# So the contribution of number i at position k is i * 10^{sum of lengths after position k}.

# The number of permutations with i at position k is (N-1)!.

# The sum over all permutations of f(P) is:

# sum_{k=1 to N} sum_{i=1 to N} i * (N-1)! * E_k

# where E_k = average of 10^{sum of lengths after position k} over all permutations with i at position k.

# Since the set of numbers after position k is any subset of size N-k of [N]\{i}, and all permutations are equally likely,

# E_k = average of 10^{sum of lengths of subsets of size N-k of [N]\{i}}.

# Since the problem is symmetric, and the difference of excluding i is negligible for large N,

# Let's approximate by including i as well.

# So define:

# For m = 0 to N, let

# S_m = sum over all subsets of size m of 10^{sum of lengths in subset}.

# Then E_k = S_{N-k} / C(N, N-k) = S_{N-k} / C(N, N-k)

# Because the average over subsets of size N-k.

# Then sum over i=1 to N of i = N(N+1)/2

# So sum over all permutations of f(P) = (N-1)! * sum_{k=1 to N} (sum_{i=1 to N} i) * E_k

# = (N-1)! * (N(N+1)/2) * sum_{k=1 to N} E_k

# = (N-1)! * (N(N+1)/2) * sum_{k=1 to N} S_{N-k} / C(N, N-k)

# = (N-1)! * (N(N+1)/2) * sum_{m=0 to N-1} S_m / C(N, m)

# Now, we need to compute S_m = sum over subsets of size m of 10^{sum of lengths in subset}.

# Let's compute the generating function:

# G(x) = product_{i=1 to N} (1 + x * 10^{L_i})

# Then coefficient of x^m in G(x) = S_m

# We can compute G(x) modulo MOD using polynomial multiplication.

# But N is up to 2*10^5, so polynomial multiplication is not feasible.

# Alternative approach:

# Since the exponents are large, but the base is 10, and lengths L_i are small (max length of N is up to 6 digits for 2*10^5), but length of i can be up to 6.

# Let's group numbers by their length.

# For each length l, let c_l = count of numbers with length l.

# Then G(x) = product over l of (1 + x * 10^l)^{c_l}

# So G(x) = product over l of (1 + x * 10^l)^{c_l}

# We want coefficient of x^m in G(x).

# Since the factors are independent, the coefficient of x^m in G(x) is sum over all vectors (m_l) with sum m_l = m of product over l of C(c_l, m_l) * (10^l)^{m_l}

# So:

# S_m = sum_{m_l} [product_l C(c_l, m_l) * 10^{l * m_l}] where sum_l m_l = m

# This is a convolution over the counts c_l.

# Since the number of distinct lengths is small (max length of numbers up to 6 digits, so max length is 6), we can do DP over lengths.

# Let's implement DP:

# Let lengths = sorted list of distinct lengths

# For each length l, we have c_l numbers.

# For each length l, the generating function is (1 + x * 10^l)^{c_l}.

# We can compute the coefficients of this polynomial using binomial coefficients:

# Coefficients for (1 + x * a)^c are C(c, k) * a^k for k=0..c

# So for each length l, we have polynomial P_l(x) = sum_{k=0 to c_l} C(c_l, k) * (10^l)^k * x^k

# We want to multiply all P_l(x) to get G(x).

# Since c_l can be large, but the degree is c_l, which can be large (up to N), we cannot multiply polynomials directly.

# But since the number of distinct lengths is small (up to 6), we can do DP over m=0..N:

# Initialize dp array of size N+1 with dp[0] = 1

# For each length l:

# For k=1 to c_l:

# dp2[m+k] += dp[m] * C(c_l, k) * (10^l)^k

# But c_l can be large, so we need a fast way.

# We can use the fact that (1 + x * a)^c = sum_{k=0}^c C(c,k) a^k x^k

# So we can do polynomial multiplication of dp and P_l(x).

# Since number of distinct lengths is small, and max degree is N, we can do DP with prefix sums.

# But N is large (2*10^5), so O(N^2) is not feasible.

# Alternative approach:

# Since the polynomials are of the form (1 + x * a)^c, we can use the binomial theorem and do DP with combinatorics.

# Let's precompute factorials and inverse factorials modulo MOD.

# Then for each length l, we can compute the polynomial P_l(x) coefficients on the fly.

# Then we can multiply dp by P_l(x) using convolution.

# Since number of distinct lengths is small (up to 6), and max degree is N, we can do DP with O(N * number_of_lengths) complexity.

# Let's implement dp as a list of length N+1, initialized with dp[0] = 1.

# For each length l:

# We compute P_l(x) coefficients: P_l[k] = C(c_l, k) * (10^l)^k mod MOD for k=0..c_l

# Then dp = dp * P_l (polynomial multiplication)

# Since c_l can be large, but number_of_lengths is small, we can do polynomial multiplication using FFT or NTT.

# But since external libraries are not allowed, and N is large, we cannot do FFT.

# So we need a better approach.

# Alternative approach:

# Since the polynomials are of the form (1 + x * a)^c, the product is:

# G(x) = product_l (1 + x * 10^l)^{c_l} = sum_{m=0}^N x^m * sum over all subsets of size m of 10^{sum lengths}

# But the coefficient of x^m is sum over all subsets of size m of 10^{sum lengths}.

# Let's consider the sum over all subsets of size m of 10^{sum lengths}.

# Let's define S = sum_{i=1}^N 10^{L_i}

# Then sum over all subsets of size m of 10^{sum lengths} is equal to the coefficient of x^m in the expansion of:

# product_{i=1}^N (1 + x * 10^{L_i})

# But we cannot compute this directly.

# Let's consider the sum over all subsets (not fixed size):

# sum_{subset} 10^{sum lengths} = product_{i=1}^N (1 + 10^{L_i}) = total_sum

# But we need subsets of fixed size m.

# Let's consider the sum over all subsets of all sizes:

# sum_{m=0}^N S_m = total_sum

# Let's consider the sum over all subsets weighted by size:

# sum_{m=0}^N m * S_m = sum over all subsets of size m of m * 10^{sum lengths}

# But this is complicated.

# Let's try a different approach.

# Let's consider the sum over all permutations of f(P):

# sum_{P} f(P) = sum_{P} sum_{k=1}^N p_k * 10^{sum of lengths after position k}

# = sum_{k=1}^N sum_{P} p_k * 10^{sum of lengths after position k}

# For fixed k, sum_{P} p_k * 10^{sum of lengths after position k} = sum_{i=1}^N i * sum_{P: p_k = i} 10^{sum of lengths after position k}

# Number of permutations with p_k = i is (N-1)!.

# For fixed i and k, sum over permutations with p_k = i of 10^{sum of lengths after position k} is:

# (k-1)! * (N-k)! * sum over subsets S of size N-k of [N]\{i} of 10^{sum lengths in S}

# So sum_{P} f(P) = sum_{k=1}^N (k-1)! * (N-k)! * sum_{i=1}^N i * sum_{S subset of size N-k of [N]\{i}} 10^{sum lengths in S}

# Now, sum_{i=1}^N i * sum_{S subset of size m of [N]\{i}} 10^{sum lengths in S} = ?

# Let's define:

# For each i, define A_i(m) = sum_{S subset of size m of [N]\{i}} 10^{sum lengths in S}

# Then sum_{i=1}^N i * A_i(m) = ?

# Note that A_i(m) = sum over subsets of size m of [N]\{i}.

# The difference between A_i(m) and S_m (sum over subsets of size m of [N]) is that A_i(m) excludes subsets containing i.

# So S_m = A_i(m) + sum over subsets of size m containing i of 10^{sum lengths in subset}

# So sum over subsets of size m containing i = 10^{L_i} * A_i(m-1)

# Because subsets containing i can be written as {i} union subset of size m-1 of [N]\{i}.

# So:

# S_m = A_i(m) + 10^{L_i} * A_i(m-1)

# => A_i(m) = S_m - 10^{L_i} * A_i(m-1)

# For m=0, A_i(0) = 1 (empty subset)

# So we can compute A_i(m) recursively.

# But this is complicated.

# Since N is large, we cannot do this for all i and m.

# Let's try to find sum_{i=1}^N i * A_i(m).

# sum_{i=1}^N i * A_i(m) = sum_{i=1}^N i * (S_m - 10^{L_i} * A_i(m-1))

# = S_m * sum_{i=1}^N i - sum_{i=1}^N i * 10^{L_i} * A_i(m-1)

# But A_i(m-1) depends on i.

# This is complicated.

# Let's try to approximate by ignoring the exclusion of i.

# Then A_i(m) ~ S_m

# So sum_{i=1}^N i * A_i(m) ~ S_m * sum_{i=1}^N i = S_m * N(N+1)/2

# Then sum_{P} f(P) ~ sum_{k=1}^N (k-1)! * (N-k)! * S_{N-k} * N(N+1)/2

# = N(N+1)/2 * (N-1)! * sum_{m=0}^{N-1} S_m

# Because (k-1)! * (N-k)! = (N-1)! / C(N-1, k-1)

# Wait, this is not exact.

# Let's check the sample input 1:

# N=3

# Numbers: 1,2,3

# Lengths: 1,1,1

# So 10^{L_i} = 10 for all i

# S_0 = 1 (empty subset)

# S_1 = sum 10^{L_i} = 10 + 10 + 10 = 30

# S_2 = sum over subsets of size 2: 10^{1+1} = 10^2=100

# Number of subsets size 2: C(3,2)=3

# So S_2 = 3 * 100 = 300

# S_3 = 10^{3} = 1000

# sum_{m=0}^{2} S_m = 1 + 30 + 300 = 331

# N(N+1)/2 = 3*4/2=6

# (N-1)! = 2

# sum_{P} f(P) ~ 6 * 2 * 331 = 6 * 662 = 3972

# But sample output is 1332, so approximation is off.

# So approximation is not good.

# Let's try a different approach.

# Let's consider the problem from the perspective of digits.

# Since the problem is complicated, let's look at the editorial approach (known from similar problems):

# The sum over all permutations of f(P) is:

# sum_{i=1}^N i * (N-1)! * sum_{k=1}^N 10^{sum of lengths of numbers after position k}

# For fixed k, the sum over all subsets of size N-k of 10^{sum lengths} is:

# sum_{S subset of size N-k} 10^{sum lengths in S} = coefficient of x^{N-k} in product_{i=1}^N (1 + x * 10^{L_i})

# So sum_{k=1}^N sum_{S subset size N-k} 10^{sum lengths in S} = sum_{m=0}^{N-1} coefficient of x^m in G(x)

# So sum_{k=1}^N sum_{S subset size N-k} 10^{sum lengths in S} = sum_{m=0}^{N-1} S_m

# Then sum_{P} f(P) = (N-1)! * sum_{i=1}^N i * sum_{k=1}^N sum_{S subset size N-k} 10^{sum lengths in S}

# = (N-1)! * sum_{i=1}^N i * sum_{m=0}^{N-1} S_m

# = (N-1)! * (N(N+1)/2) * sum_{m=0}^{N-1} S_m

# But this is the same as previous approximation, which was off for sample input.

# So the problem is that the place value depends on the sum of lengths after position k, but the number i is at position k, so the subsets after position k exclude i.

# So the subsets are from [N]\{i}.

# So for each i, sum over subsets of size m of [N]\{i} of 10^{sum lengths} = S_m^{(-i)}

# So sum_{P} f(P) = (N-1)! * sum_{i=1}^N i * sum_{m=0}^{N-1} S_m^{(-i)}

# Now, S_m^{(-i)} = coefficient of x^m in G^{(-i)}(x) = product_{j != i} (1 + x * 10^{L_j})

# So sum_{i=1}^N i * S_m^{(-i)} = ?

# Let's define:

# G(x) = product_{i=1}^N (1 + x * 10^{L_i}) = sum_{m=0}^N S_m x^m

# G^{(-i)}(x) = G(x) / (1 + x * 10^{L_i}) = sum_{m=0}^{N-1} S_m^{(-i)} x^m

# So S_m^{(-i)} = coefficient of x^m in G(x) / (1 + x * 10^{L_i})

# So sum_{i=1}^N i * S_m^{(-i)} = coefficient of x^m in sum_{i=1}^N i * G(x) / (1 + x * 10^{L_i})

# So sum_{P} f(P) = (N-1)! * sum_{m=0}^{N-1} coefficient of x^m in sum_{i=1}^N i * G(x) / (1 + x * 10^{L_i})

# Since G(x) is known, we can write:

# sum_{i=1}^N i / (1 + x * 10^{L_i}) = ?

# Let's define H(x) = sum_{i=1}^N i / (1 + x * 10^{L_i})

# Then sum_{P} f(P) = (N-1)! * coefficient of x^m in G(x) * H(x)

# But this is complicated.

# Let's try to compute sum_{i=1}^N i / (1 + x * 10^{L_i}) modulo x^{N}.

# Since 1/(1 + x * a) = sum_{k=0}^\infty (-1)^k (x a)^k

# So:

# i / (1 + x * 10^{L_i}) = i * sum_{k=0}^\infty (-1)^k x^k 10^{L_i k}

# So sum_{i=1}^N i / (1 + x * 10^{L_i}) = sum_{k=0}^\infty (-1)^k x^k sum_{i=1}^N i * 10^{L_i k}

# Then:

# sum_{P} f(P) = (N-1)! * coefficient of x^m in G(x) * sum_{k=0}^\infty (-1)^k x^k sum_{i=1}^N i * 10^{L_i k}

# = (N-1)! * sum_{m=0}^{N-1} sum_{k=0}^m (-1)^k S_{m-k} * sum_{i=1}^N i * 10^{L_i k}

# So sum_{P} f(P) = (N-1)! * sum_{m=0}^{N-1} sum_{k=0}^m (-1)^k S_{m-k} * sum_{i=1}^N i * 10^{L_i k}

# Now, we can swap sums:

# sum_{P} f(P) = (N-1)! * sum_{k=0}^{N-1} (-1)^k sum_{m=k}^{N-1} S_{m-k} * sum_{i=1}^N i * 10^{L_i k}

# = (N-1)! * sum_{k=0}^{N-1} (-1)^k sum_{m=0}^{N-1-k} S_m * sum_{i=1}^N i * 10^{L_i k}

# But this is complicated.

# Since time is limited, let's implement the following approach:

# 1. Precompute factorials and inverse factorials.

# 2. Group numbers by length l, count c_l.

# 3. Precompute binomial coefficients C(c_l, k) for k=0..c_l.

# 4. Compute dp array of size N+1, dp[m] = sum over subsets of size m of 10^{sum lengths}.

#    dp is initialized as [1] + [0]*N

# 5. For each length l:

#    - Compute polynomial P_l(x) = sum_{k=0}^{c_l} C(c_l, k) * (10^l)^k * x^k

#    - Multiply dp by P_l(x) to update dp.

# Since number of distinct lengths is small (max 6), and c_l sum to N, we can do this with O(N * number_of_lengths) complexity.

# Multiplying dp by P_l(x) is a convolution, but since P_l(x) is a binomial expansion, we can do it efficiently:

# For each length l:

#   For m from N down to 0:

#     For k from 1 to c_l:

#       if m - k >= 0:

#         dp[m] += dp[m-k] * C(c_l, k) * (10^l)^k

# We can optimize by using prefix sums and precomputed powers.

# Finally, sum_{P} f(P) = (N-1)! * sum_{i=1}^N i * sum_{m=0}^{N-1} dp[m] excluding i?

# Since excluding i is complicated, we approximate by including all numbers.

# sum_{i=1}^N i = N(N+1)/2

# sum_{m=0}^{N-1} dp[m] = sum over subsets of size <= N-1 of 10^{sum lengths}

# But dp[N] corresponds to subset of size N, which is the full set.

# So sum_{m=0}^{N-1} dp[m] = total_sum - dp[N]

# So answer = (N-1)! * (N(N+1)/2) * (total_sum - dp[N]) mod MOD

# Let's check sample input 1:

# N=3

# Numbers: 1,2,3

# Lengths: all 1

# c_1 = 3

# P_1(x) = (1 + 10 x)^3 = 1 + 3*10 x + 3*100 x^2 + 1000 x^3

# dp after processing length 1:

# dp = [1, 30, 300, 1000]

# total_sum = sum dp = 1 + 30 + 300 + 1000 = 1331

# sum_{m=0}^{N-1} dp[m] = 1 + 30 + 300 = 331

# (N-1)! = 2

# sum_{i=1}^N i = 6

# answer = 2 * 6 * 331 = 3972 mod 998244353

# But sample output is 1332, so approximation is off.

# So the problem requires exact exclusion of i.

# Since time is limited, let's implement the exact solution:

# For each length l, we compute P_l(x) = (1 + x * 10^l)^{c_l}

# Then G(x) = product P_l(x)

# For each i, G^{(-i)}(x) = G(x) / (1 + x * 10^{L_i})

# So coefficient of x^m in G^{(-i)}(x) = S_m^{(-i)}

# sum_{P} f(P) = (N-1)! * sum_{i=1}^N i * sum_{m=0}^{N-1} S_m^{(-i)}

# So we need to compute sum_{m=0}^{N-1} S_m^{(-i)} for each i.

# Since G^{(-i)}(x) = G(x) / (1 + x * 10^{L_i})

# So sum_{m=0}^{N-1} S_m^{(-i)} = sum_{m=0}^{N-1} coefficient of x^m in G(x) / (1 + x * 10^{L_i})

# = sum_{m=0}^{N-1} coefficient of x^m in G(x) * sum_{k=0}^\infty (-1)^k x^k (10^{L_i})^k

# = sum_{m=0}^{N-1} sum_{k=0}^m (-1)^k (10^{L_i})^k * coefficient of x^{m-k} in G(x)

# = sum_{m=0}^{N-1} sum_{k=0}^m (-1)^k (10^{L_i})^k * S_{m-k}

# = sum_{t=0}^{N-1} S_t * sum_{k=0}^{N-1 - t} (-1)^k (10^{L_i})^k

# = sum_{t=0}^{N-1} S_t * (1 - ( - (10^{L_i}) )^{N - t}) / (1 + 10^{L_i})

# But since N is large, (10^{L_i})^{N - t} mod MOD can be computed by fast exponentiation.

# So sum_{m=0}^{N-1} S_m^{(-i)} = sum_{t=0}^{N-1} S_t * (1 - (-10^{L_i})^{N - t}) * inv(1 + 10^{L_i}) mod MOD

# Let's precompute:

# inv_1_plus_10L = inverse of (1 + 10^{L_i}) mod MOD

# pow_neg_10L = (-10^{L_i})^{k} mod MOD for k=0..N

# Then for each i, sum_{m=0}^{N-1} S_m^{(-i)} = inv_1_plus_10L * sum_{t=0}^{N-1} S_t * (1 - pow_neg_10L[N - t])

# Then sum_{P} f(P) = (N-1)! * sum_{i=1}^N i * sum_{m=0}^{N-1} S_m^{(-i)} mod MOD

# We can precompute sum_{t=0}^{N-1} S_t and prefix sums.

# Since N is large, we cannot sum over t=0..N-1 for each i.

# But since numbers with same length share 10^{L_i}, we can group by length.

# For each length l:

# - Compute inv_1_plus_10l = inverse of (1 + 10^l)

# - Precompute pow_neg_10l[k] = (-10^l)^k mod MOD for k=0..N

# Then for each length l:

# sum_{i with length l} i = sum_i_l

# Then sum over i with length l of i * sum_{m=0}^{N-1} S_m^{(-i)} = sum_i_l * inv_1_plus_10l * sum_{t=0}^{N-1} S_t * (1 - pow_neg_10l[N - t])

# So total sum = (N-1)! * sum over lengths l of above

# Now, sum_{t=0}^{N-1} S_t * (1 - pow_neg_10l[N - t]) = sum_{t=0}^{N-1} S_t - sum_{t=0}^{N-1} S_t * pow_neg_10l[N - t]

# sum_{t=0}^{N-1} S_t = total_sum - S_N

# sum_{t=0}^{N-1} S_t * pow_neg_10l[N - t] = sum_{k=1}^N S_{N - k} * pow_neg_10l[k]

# We can precompute prefix sums of S_m and do this efficiently.

# Let's implement this final approach.

# Steps:

# 1. Precompute factorials and inverse factorials.

# 2. Compute counts c_l and sum_i_l for each length l.

# 3. Compute dp = coefficients S_m of G(x) = product_l (1 + x * 10^l)^{c_l} using DP.

# 4. Precompute pow_neg_10l for each length l.

# 5. Compute total_sum = sum_{m=0}^N S_m

# 6. Compute answer = (N-1)! * sum over l of sum_i_l * inv(1 + 10^l) * ( (total_sum - S_N) - sum_{k=1}^N S_{N-k} * pow_neg_10l[k] ) mod MOD

# 7. Output answer mod MOD.

# Let's implement now.

def modinv(a):
    return pow(a, MOD - 2, MOD)

maxN = N

# Precompute factorials and inverse factorials
fact = [1] * (maxN + 1)
inv_fact = [1] * (maxN + 1)
for i in range(1, maxN + 1):
    fact[i] = fact[i - 1] * i % MOD
inv_fact[maxN] = modinv(fact[maxN])
for i in range(maxN - 1, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

def comb(n, r):
    if r > n or r < 0:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

# Compute lengths and group by length
from collections import defaultdict

length_count = defaultdict(int)
length_sum_i = defaultdict(int)

for i in range(1, N + 1):
    l = len(str(i))
    length_count[l] += 1
    length_sum_i[l] = (length_sum_i[l] + i) % MOD

lengths = sorted(length_count.keys())

# Compute