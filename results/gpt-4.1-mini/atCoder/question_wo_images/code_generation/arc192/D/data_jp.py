import sys
sys.setrecursionlimit(10**7)
MOD = 998244353

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# A_i = f(S_i / S_{i+1}) = P*Q where S_i/S_{i+1} = P/Q in lowest terms
# So for each i, S_i/S_{i+1} = P_i/Q_i with gcd(P_i,Q_i)=1 and P_i*Q_i = A_i

# We want sequences S_1,...,S_N with gcd=1 and for all i, f(S_i/S_{i+1})=A_i
# and sum of product of all S_i over all such sequences modulo MOD.

# Key observations:
# - For each A_i, factorize into pairs (p,q) with p*q = A_i and gcd(p,q)=1
# - Then S_i/S_{i+1} = p/q
# - From this, S_i = p * k_i, S_{i+1} = q * k_i for some integer k_i
# - The k_i relate as k_{i+1} = p_i * k_i / q_{i+1} but we must be consistent.

# Instead, consider the chain of fractions:
# S_1/S_2 = p_1/q_1
# S_2/S_3 = p_2/q_2
# ...
# S_{N-1}/S_N = p_{N-1}/q_{N-1}

# Then:
# S_1 = S_1
# S_2 = S_1 * q_1 / p_1
# S_3 = S_2 * q_2 / p_2 = S_1 * q_1 * q_2 / (p_1 * p_2)
# ...
# S_N = S_1 * (product of q_i) / (product of p_i)

# Since S_i must be integers, S_1 must be divisible by denominators.

# To handle gcd(S_1,...,S_N)=1, we can fix S_1 = 1 and then scale by a factor d later.

# But we want to find all sequences (p_i,q_i) with p_i*q_i = A_i, gcd(p_i,q_i)=1,
# and then find all integer multiples d such that all S_i = d * (product of q_j for j<i) / (product of p_j for j<i) are integers,
# and gcd(S_1,...,S_N) = 1.

# The problem reduces to:
# - For each i, find all coprime pairs (p_i,q_i) with p_i*q_i = A_i
# - For the sequence of pairs, find the minimal integer d making all S_i integers
# - Then scale by all positive integers dividing gcd(S_1,...,S_N) to get all sequences with gcd=1
# - Sum over all such sequences the product of S_i

# But the problem states the number of good sequences is finite, so the scaling factor d is fixed by minimal integer making all S_i integers.
# Then gcd(S_1,...,S_N) = d, so to have gcd=1, we must divide all S_i by d.
# So the minimal integer d is the gcd of the S_i before dividing.

# So the sequences correspond to choosing (p_i,q_i) for each i, then computing the minimal d, then dividing S_i by d to get gcd=1 sequence.

# The product of S_i is then (product of S_i before dividing) / d^N

# But since S_i before dividing = d * (product of q_j for j<i) / (product of p_j for j<i)
# and d is the gcd of these numbers, dividing by d makes gcd=1.

# So the product of S_i after dividing by d is (product of S_i before dividing) / d^N

# We want sum over all sequences of (product of S_i after dividing by d) modulo MOD.

# Approach:
# 1. For each A_i, find all pairs (p,q) with p*q=A_i and gcd(p,q)=1
# 2. For each position i, store these pairs
# 3. We want to consider all sequences of pairs (p_1,q_1),...,(p_{N-1},q_{N-1})
# 4. For each sequence, compute:
#    - S_1 = d (unknown)
#    - S_i = S_1 * (product of q_j for j=1 to i-1) / (product of p_j for j=1 to i-1)
# 5. The minimal d is the lcm of denominators of S_i when S_1=1, i.e., the lcm of denominators of fractions (product q_j)/(product p_j)
# 6. Then actual S_i = d * (product q_j)/(product p_j)
# 7. gcd(S_1,...,S_N) = d
# 8. Dividing all S_i by d gives gcd=1 sequence
# 9. Product of S_i after dividing by d is (product of S_i before dividing) / d^N
# 10. product of S_i before dividing = d^N * product over i of (product q_j / product p_j) = d^N * (product q_j)^{N-i} / (product p_j)^{N-i} (complicated)
# Actually, product of S_i = S_1 * S_2 * ... * S_N
# = d * (d * q_1/p_1) * (d * q_1 q_2 / p_1 p_2) * ... * (d * product q_j / product p_j)
# = d^N * product_{i=1}^N (product_{j=1}^{i-1} q_j / product_{j=1}^{i-1} p_j)
# = d^N * product_{i=1}^N (product_{j=1}^{i-1} q_j) / (product_{j=1}^{i-1} p_j)
# = d^N * product_{j=1}^{N-1} q_j^{N-j} / p_j^{N-j}

# So product of S_i after dividing by d is:
# (product of S_i before dividing) / d^N = product_{j=1}^{N-1} q_j^{N-j} / p_j^{N-j}

# So the product of S_i for gcd=1 sequence depends only on the chosen pairs (p_j,q_j).

# Therefore, the sum over all good sequences of product of S_i is:
# sum over all sequences of product_{j=1}^{N-1} q_j^{N-j} / p_j^{N-j}

# But S_i must be integers, so the minimal d is the lcm of denominators of S_i when S_1=1.
# The gcd=1 condition means we only count sequences where minimal d=1, i.e., all S_i are integers with S_1=1.

# So we want sequences of pairs (p_j,q_j) with p_j*q_j=A_j, gcd(p_j,q_j)=1, such that for all i,
# (product_{j=1}^{i-1} q_j) / (product_{j=1}^{i-1} p_j) is integer.

# Define prefix fractions:
# For i=1: fraction = 1 (empty product)
# For i>1: fraction = (product q_j for j=1 to i-1) / (product p_j for j=1 to i-1)

# All these fractions must be integers.

# So the problem reduces to:
# Find all sequences of pairs (p_j,q_j) with p_j*q_j=A_j, gcd(p_j,q_j)=1,
# such that for all i=1..N, prefix fraction is integer.

# Then sum over all such sequences of product_{j=1}^{N-1} q_j^{N-j} / p_j^{N-j} modulo MOD.

# We can solve this by dynamic programming over prime factorizations.

# Implementation plan:
# - Precompute prime factorizations of all A_i
# - For each A_i, find all pairs (p,q) with p*q=A_i, gcd(p,q)=1
#   - p and q are divisors of A_i with gcd=1 and p*q=A_i
# - Represent fractions as exponent vectors of primes
# - Maintain DP over the current exponent vector of the prefix fraction (product q_j / product p_j)
# - For each position i, for each possible exponent vector in DP,
#   try all pairs (p,q) for A_i:
#     new exponent vector = old exponent vector + exponent(q) - exponent(p)
#     only keep if all exponents >= 0 (integer fraction)
#     update DP[new exponent vector] += DP[old exponent vector] * (q^{N-i} * p^{-(N-i)} mod MOD)
# - At the end, sum all DP values

# To handle exponents efficiently, we can map prime exponents to tuples.

# Since A_i <= 1000, prime factorization is fast.

# The number of primes up to 1000 is small (~168), but each A_i has few prime factors.

# We'll only track primes appearing in any A_i.

# To keep DP manageable, we use a dictionary keyed by exponent tuples.

# Let's implement.

from math import gcd
from collections import defaultdict

# Prime factorization for numbers up to 1000
def prime_factorization(x):
    res = {}
    d = 2
    while d*d <= x:
        while x % d == 0:
            res[d] = res.get(d,0)+1
            x //= d
        d += 1 if d==2 else 2
    if x > 1:
        res[x] = res.get(x,0)+1
    return res

# Get all divisors of n
def get_divisors(n):
    divs = []
    def dfs(i, cur):
        if i == len(factors):
            divs.append(cur)
            return
        p, cnt = factors[i]
        for c in range(cnt+1):
            dfs(i+1, cur*(p**c))
    factors = list(prime_factorization(n).items())
    dfs(0,1)
    return divs

# Precompute primes appearing in all A_i
prime_set = set()
A_factors = [prime_factorization(a) for a in A]
for f in A_factors:
    prime_set |= f.keys()
primes = sorted(prime_set)
prime_index = {p:i for i,p in enumerate(primes)}
K = len(primes)

# Convert factor dict to exponent tuple
def factor_to_exp(f):
    exp = [0]*K
    for p,v in f.items():
        exp[prime_index[p]] = v
    return tuple(exp)

# Add two exponent tuples
def add_exp(a,b):
    return tuple(x+y for x,y in zip(a,b))

# Subtract two exponent tuples
def sub_exp(a,b):
    return tuple(x-y for x,y in zip(a,b))

# Check if all exponents >= 0
def is_nonneg(exp):
    return all(x>=0 for x in exp)

# Precompute all pairs (p,q) for each A_i with gcd(p,q)=1 and p*q=A_i
pairs_list = []
for i in range(N-1):
    a = A[i]
    divs = get_divisors(a)
    pairs = []
    for p in divs:
        q = a//p
        if gcd(p,q) == 1:
            # Store exponent vectors of p and q
            p_exp = factor_to_exp(prime_factorization(p))
            q_exp = factor_to_exp(prime_factorization(q))
            pairs.append((p,q,p_exp,q_exp))
    pairs_list.append(pairs)

# Precompute pow_mod for q^{N-i} and p^{N-i}
def modpow(base, exp):
    res = 1
    b = base % MOD
    e = exp
    while e > 0:
        if e & 1:
            res = res * b % MOD
        b = b * b % MOD
        e >>= 1
    return res

# DP: key = exponent tuple of prefix fraction (product q_j / product p_j)
# value = sum of product of S_i for sequences leading here
dp = defaultdict(int)
dp[(0,)*K] = 1  # initial fraction = 1

for i in range(N-1):
    ndp = defaultdict(int)
    power = N - i - 1
    for exp_vec, val in dp.items():
        for p, q, p_exp, q_exp in pairs_list[i]:
            new_exp = add_exp(exp_vec, sub_exp(q_exp, p_exp))
            if is_nonneg(new_exp):
                # product factor = q^{power} * p^{-power} mod MOD
                # p^{-power} mod MOD = pow(p, MOD-2)^{power} mod MOD
                # Compute inverse of p mod MOD
                inv_p = pow(p, MOD-2, MOD)
                mul = val * modpow(q, power) % MOD * modpow(inv_p, power) % MOD
                ndp[new_exp] = (ndp[new_exp] + mul) % MOD
    dp = ndp

# Sum all dp values
ans = sum(dp.values()) % MOD
print(ans)