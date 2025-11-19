def main():
    import sys
    input = sys.stdin.readline
    mod = 998244353

    N = int(input())

    # Precompute factorials and inverse factorials for permutations count
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % mod

    # Precompute length of each number and count how many numbers have that length
    # Also precompute sum of numbers in each length group modulo mod
    length_counts = []
    length_sums = []
    max_d = len(str(N))
    pow10 = [1] * (max_d + 2)
    for i in range(1, max_d + 2):
        pow10[i] = pow10[i - 1] * 10 % mod

    low = 1
    for d in range(1, max_d + 1):
        high = min(N, pow(10, d) - 1)
        if low > high:
            break
        cnt = high - low + 1
        s = (low + high) * cnt // 2 % mod
        length_counts.append(cnt)
        length_sums.append(s)
        low = high + 1

    # Precompute prefix sums of counts for positions
    # We want to find sum of 10^{length} for all numbers in the permutation
    # The key insight:
    # For each position i (0-based), the digit contribution is:
    # sum over all numbers of 10^{length} * number * (number of permutations with that number at position i)
    # Number of permutations with fixed number at position i is (N-1)!
    # The total sum over all permutations is sum over positions i of (N-1)! * sum over numbers of number * 10^{length * (N-1 - i)}

    # But since concatenation is sequential, the total power of 10 for a number at position i depends on the sum of lengths of numbers after position i.

    # So we need to find sum of 10^{sum of lengths of numbers after position i} over all permutations.

    # Since all permutations are symmetric, the expected sum of lengths after position i is the same for all positions.

    # Let's precompute prefix sums of counts and lengths to get total length sum
    total_len = 0
    lens = []
    for d, cnt in enumerate(length_counts, 1):
        total_len += d * cnt
        lens.extend([d] * cnt)

    # Precompute prefix sums of lengths
    # But lens is large (up to N=2e5), so we avoid building lens explicitly.

    # Instead, we precompute prefix sums of counts and lengths:
    prefix_counts = [0]
    prefix_len_sum = [0]
    for d, cnt in enumerate(length_counts, 1):
        prefix_counts.append(prefix_counts[-1] + cnt)
        prefix_len_sum.append(prefix_len_sum[-1] + d * cnt)

    # Precompute factorial inverse for modular inverse
    inv_fact = [1] * (N + 1)
    inv_fact[N] = pow(fact[N], mod - 2, mod)
    for i in range(N - 1, -1, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

    # Precompute pow10 for all possible lengths up to total_len
    max_len = total_len
    pow10_len = [1] * (max_len + 1)
    for i in range(1, max_len + 1):
        pow10_len[i] = pow10_len[i - 1] * 10 % mod

    # Precompute prefix sums of pow10_len for lengths
    # We'll need to compute sum of pow10^{lengths after position i}

    # The main idea:
    # For each position i (0-based), the total length of numbers after i is total_len - prefix_len_of_first_i_numbers
    # Since permutations are uniform, the expected sum of lengths of first i numbers is i * average length
    # But average length is total_len / N, so sum of lengths after i is total_len - i * average_length

    # But we need exact sums, so we use linearity and symmetry:
    # The sum over all permutations of 10^{sum of lengths after position i} is:
    # (N-1)! * sum over all subsets of size i of lengths, sum of pow10^{total_len - sum_of_lengths_in_subset}

    # This is complicated, but can be simplified by the following approach:

    # Let's define a polynomial P(x) = product over all numbers of (1 + x^{length_of_number})
    # The coefficient of x^k in P(x) is the number of subsets of numbers with total length k.

    # Then sum over subsets of size i of pow10^{total_len - k} = pow10^{total_len} * coefficient of x^k in P(x) * pow10^{-k}

    # So sum over subsets of size i of pow10^{total_len - k} = pow10^{total_len} * coefficient of x^k in P(x * pow10^{-1})

    # So we can build polynomial Q(x) = product over all numbers of (1 + x^{length_of_number} * pow10^{-length_of_number})

    # Since numbers with same length are identical, we can group by length:
    # Q(x) = product over lengths d of (1 + x * pow10^{-d})^{count_d}

    # The coefficient of x^i in Q(x) is sum over subsets of size i of pow10^{-sum_of_lengths_in_subset}

    # Then sum over subsets of size i of pow10^{total_len - sum_of_lengths_in_subset} = pow10^{total_len} * coefficient of x^i in Q(x)

    # We can compute Q(x) as product of binomial expansions:
    # For each length d:
    # (1 + x * pow10^{-d})^{count_d} = sum_{j=0}^{count_d} C(count_d, j) * (pow10^{-d})^j * x^j

    # So Q(x) = convolution of these polynomials for all d.

    # After computing Q(x), coefficient of x^i is q_i.

    # Then for position i (0-based), sum of pow10^{sum of lengths after position i} over all subsets of size i is pow10^{total_len} * q_i

    # Now, the total sum over all permutations is:
    # sum_{i=0}^{N-1} (N-1)! * fact[i] * fact[N-1 - i] * sum_of_numbers * pow10^{total_len} * q_i

    # sum_of_numbers = sum_{k=1}^N k = N*(N+1)//2

    # So final answer = (N-1)! * sum_of_numbers * pow10^{total_len} * sum_{i=0}^{N-1} fact[i] * fact[N-1 - i] * q_i mod

    # Let's implement this.

    # Precompute inverse powers of 10 for each length d
    inv_pow10 = [pow(pow10[d], mod - 2, mod) for d in range(max_d + 1)]

    # Build polynomials for each length group
    # Each polynomial is (1 + x * inv_pow10[d])^{count_d}
    # We'll represent polynomials as lists of coefficients

    # To multiply polynomials efficiently, we use iterative convolution with FFT/NTT
    # But since max_d is small (<=6), and counts can be large, we use binomial coefficients and pow

    # For each length group:
    # poly_d[j] = C(count_d, j) * (inv_pow10[d])^j mod

    # We'll multiply all these polynomials together to get Q(x)

    # Precompute factorials and inverse factorials up to max count
    max_cnt = max(length_counts) if length_counts else 0
    max_cnt = max(max_cnt, N)  # just in case

    fact2 = [1] * (max_cnt + 1)
    inv_fact2 = [1] * (max_cnt + 1)
    for i in range(1, max_cnt + 1):
        fact2[i] = fact2[i - 1] * i % mod
    inv_fact2[max_cnt] = pow(fact2[max_cnt], mod - 2, mod)
    for i in range(max_cnt - 1, -1, -1):
        inv_fact2[i] = inv_fact2[i + 1] * (i + 1) % mod

    def comb(n, r):
        if r > n or r < 0:
            return 0
        return fact2[n] * inv_fact2[r] % mod * inv_fact2[n - r] % mod

    # Polynomial multiplication (naive since max degree is up to N)
    # But degree can be up to N, so naive O(N^2) is too slow.
    # Instead, we use iterative multiplication with FFT/NTT.

    # Implement NTT for convolution
    def ntt(a, inv=False):
        n = len(a)
        j = 0
        for i in range(1, n):
            bit = n >> 1
            while j & bit:
                j ^= bit
                bit >>= 1
            j |= bit
            if i < j:
                a[i], a[j] = a[j], a[i]
        length = 2
        root = 3
        if inv:
            root = pow(root, mod - 2, mod)
        while length <= n:
            wlen = pow(root, (mod - 1) // length, mod)
            for i in range(0, n, length):
                w = 1
                for j in range(i, i + length // 2):
                    u = a[j]
                    v = a[j + length // 2] * w % mod
                    a[j] = (u + v) % mod
                    a[j + length // 2] = (u - v) % mod
                    w = w * wlen % mod
            length <<= 1
        if inv:
            inv_n = pow(n, mod - 2, mod)
            for i in range(n):
                a[i] = a[i] * inv_n % mod

    def conv(a, b):
        n = len(a) + len(b) - 1
        size = 1
        while size < n:
            size <<= 1
        A = a[:] + [0] * (size - len(a))
        B = b[:] + [0] * (size - len(b))
        ntt(A)
        ntt(B)
        for i in range(size):
            A[i] = A[i] * B[i] % mod
        ntt(A, inv=True)
        return A[:n]

    # Build polynomials for each length group
    polys = []
    for d, cnt in enumerate(length_counts, 1):
        poly = [0] * (cnt + 1)
        inv_p = pow(pow10[d], mod - 2, mod)
        inv_p_pow = 1
        for j in range(cnt + 1):
            c = comb(cnt, j)
            poly[j] = c * inv_p_pow % mod
            inv_p_pow = inv_p_pow * inv_p % mod
        polys.append(poly)

    # Multiply all polynomials
    from functools import reduce
    from operator import mul

    def multiply_all(polys):
        from collections import deque
        q = deque(polys)
        while len(q) > 1:
            a = q.popleft()
            b = q.popleft()
            q.append(conv(a, b))
        return q[0] if q else [1]

    Q = multiply_all(polys)

    # Now Q[i] = sum over subsets of size i of pow10^{-sum_of_lengths_in_subset}

    # Precompute sum_of_numbers
    sum_numbers = N * (N + 1) // 2 % mod

    # Precompute (N-1)!
    fact_n_1 = fact[N - 1]

    # Precompute pow10^{total_len}
    pow10_total_len = pow10_len[total_len]

    # Precompute fact[i] * fact[N-1 - i] for i in [0, N-1]
    fact_pairs = [fact[i] * fact[N - 1 - i] % mod for i in range(N)]

    # Compute final answer
    res = 0
    for i in range(N):
        val = fact_pairs[i] * Q[i] % mod
        res += val
    res %= mod

    res = res * fact_n_1 % mod
    res = res * sum_numbers % mod
    res = res * pow10_total_len % mod

    print(res)


if __name__ == "__main__":
    main()