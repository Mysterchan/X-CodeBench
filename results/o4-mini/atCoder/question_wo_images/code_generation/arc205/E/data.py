import sys
input = sys.stdin.readline

MOD = 998244353

N = int(input())
A = list(map(int, input().split()))

# max bit length is 20 (0 <= A_i < 2^20)
MAX_BIT = 20
MAX_MASK = 1 << MAX_BIT

# freq[mask] = product of all A_i with value = mask (mod MOD)
freq = [1] * MAX_MASK
count = [0] * MAX_MASK

for x in A:
    count[x] += 1

for mask in range(MAX_MASK):
    if count[mask] > 0:
        # freq[mask] = (mask)^(count[mask]) mod MOD
        # We need product of all A_i with value = mask
        # Since all A_i are equal to mask, product = mask^count[mask] mod MOD
        # But mask can be zero, zero^count = 0 if count>0, product is zero
        # So handle zero separately
        if mask == 0:
            freq[mask] = 0 if count[mask] > 0 else 1
        else:
            # pow(mask, count[mask], MOD)
            freq[mask] = pow(mask, count[mask], MOD)
    else:
        freq[mask] = 1

# We want for each k:
# product of A_i for i in [1..k] such that (A_i OR A_k) == A_k
# i.e. A_i is subset of A_k in bits (A_i & A_k == A_i)
# So for each prefix k, we want product of all A_i in prefix with A_i subset of A_k

# We will process prefix products for each mask:
# prefix_freq[mask] = product of all A_i in prefix with value = mask

prefix_freq = [1] * MAX_MASK

res = []

for k in range(N):
    x = A[k]
    # Update prefix_freq for A[k]
    # multiply prefix_freq[x] by A[k]
    prefix_freq[x] = (prefix_freq[x] * A[k]) % MOD

    # Now we want product of prefix_freq[mask] for all mask subset of x
    # i.e. all mask where (mask & x) == mask

    # Enumerate all subsets of x
    # subset enumeration: subset = x
    # while True:
    #   process subset
    #   subset = (subset - 1) & x
    #   break if subset == x again

    product = 1
    subset = x
    while True:
        product = (product * prefix_freq[subset]) % MOD
        if subset == 0:
            break
        subset = (subset - 1) & x

    res.append(product)

print('\n'.join(map(str, res)))