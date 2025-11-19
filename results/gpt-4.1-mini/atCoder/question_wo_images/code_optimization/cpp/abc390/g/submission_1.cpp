#include <bits/stdc++.h>
using namespace std;

const int Mod = 998244353;

inline int add(int a, int b) {
    a += b;
    if (a >= Mod) a -= Mod;
    return a;
}

inline int sub(int a, int b) {
    a -= b;
    if (a < 0) a += Mod;
    return a;
}

inline int mul(int a, int b) {
    return int((long long)a * b % Mod);
}

int binPow(int a, int b) {
    int res = 1;
    while (b > 0) {
        if (b & 1) res = mul(res, a);
        a = mul(a, a);
        b >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n; cin >> n;

    // Precompute factorials and inverse factorials
    vector<int> fact(n + 1, 1), invFact(n + 1, 1);
    for (int i = 1; i <= n; i++) fact[i] = mul(fact[i - 1], i);
    invFact[n] = binPow(fact[n], Mod - 2);
    for (int i = n - 1; i >= 0; i--) invFact[i] = mul(invFact[i + 1], i + 1);

    // Count how many numbers have each digit length
    // max digit length for n <= 2*10^5 is 6
    vector<int> countLen(7, 0);
    for (int x = 1; x <= n; x++) {
        int len = 0, tmp = x;
        while (tmp > 0) {
            tmp /= 10;
            len++;
        }
        countLen[len]++;
    }

    // Precompute powers of 10 up to max length * n (max length is 6)
    // max total length of concatenation is at most 6*n digits, but we only need up to 6*n
    // But we only need powers of 10 up to 6*n, which is too large.
    // Instead, we use a formula to compute contribution per position.

    // Key insight:
    // The sum over all permutations of f(P) can be computed by linearity and symmetry:
    // Each number x appears in each position equally many times.
    // The total number of permutations is n!
    // For each position i (0-based from left), the contribution of number x at position i is:
    // x * 10^{sum of lengths of numbers after position i} * (number of permutations with x at position i)
    // Number of permutations with x fixed at position i is (n-1)!
    // The sum of lengths of numbers after position i depends on which numbers are placed after i.
    // Because all permutations are considered, the expected sum of lengths after position i is:
    // (n - 1 - i) * average length of numbers (since all permutations are uniform)
    // But lengths vary, so we must consider all lengths.

    // Instead, we use a known formula:
    // The sum over all permutations of f(P) = (n-1)! * sum over all positions i=0..n-1 of
    // sum over all numbers x of x * 10^{sum of lengths of numbers after position i}

    // But sum of lengths after position i varies depending on which numbers are after i.
    // Since all permutations are considered, the distribution is uniform.

    // So, the total sum = (n-1)! * sum_{i=0}^{n-1} (sum over all x of x) * (sum over all lengths of numbers after i of 10^{lengths})

    // This is complicated, but the problem can be solved by the following approach:

    // Let's define:
    // - total factorial: fact[n]
    // - For each digit length d, countLen[d] numbers have length d
    // - sumX = sum of all numbers from 1 to n = n*(n+1)/2 mod Mod

    // The sum of all numbers:
    int64_t sumX = (int64_t)n * (n + 1) / 2 % Mod;

    // Precompute prefix sums of countLen for convenience
    // But we need to compute the sum of 10^{length} * countLen[length]
    // For each position, the total power of 10 contributed by numbers after position i is:
    // sum over all lengths l of countLen[l] * l * 10^{l}

    // Actually, the problem is known and the formula is:

    // sum over all permutations P of f(P) = fact[n-1] * sum_{x=1}^n x * sum_{i=0}^{n-1} 10^{total_length_after_i}

    // The total length after position i is sum of lengths of n-1-i numbers.

    // Since all permutations are symmetric, the expected sum of lengths after position i is (n-1 - i) * average length.

    // But we need exact sum, so we do the following:

    // Let's precompute prefix sums of countLen and total length:
    // total length of all numbers = sum_{d=1}^6 countLen[d] * d

    int totalLen = 0;
    for (int d = 1; d <= 6; d++) totalLen += countLen[d] * d;

    // Precompute powers of 10 up to totalLen
    // max totalLen <= 6 * n <= 1.2e6, which is too large for direct precomputation.

    // Instead, we use the following approach:

    // The sum over all permutations of f(P) can be computed as:
    // sum_{k=0}^{n-1} fact[k] * fact[n-1-k] * sum over all numbers x of x * 10^{sum of lengths of numbers after position k}

    // But sum of lengths of numbers after position k is variable.

    // The problem editorial (known from similar problems) gives a formula:

    // sum over all permutations P of f(P) = fact[n-1] * sum_{x=1}^n x * sum_{k=0}^{n-1} 10^{sum of lengths of numbers after position k}

    // The sum of lengths of numbers after position k is sum of lengths of n-1-k numbers.

    // Since all permutations are considered, the sum of lengths of numbers after position k is the sum of lengths of any subset of size n-1-k.

    // The average sum of lengths of subsets of size s is s * average length.

    // But we need exact sum of 10^{sum of lengths}, which is complicated.

    // The original code uses a convolution approach to handle this.

    // We can optimize by precomputing the count of numbers by length and the sum of numbers by length.

    // Let's precompute sum of numbers by length:
    vector<int64_t> sumByLen(7, 0);
    for (int x = 1; x <= n; x++) {
        int len = 0, tmp = x;
        while (tmp > 0) {
            tmp /= 10;
            len++;
        }
        sumByLen[len] = (sumByLen[len] + x) % Mod;
    }

    // Precompute factorials and inverse factorials already done.

    // Precompute powers of 10 up to 6*n (max total length)
    // This is too large, so we use a different approach.

    // The key is to realize that the sum over all permutations of f(P) equals:
    // fact[n-1] * sum_{x=1}^n x * sum_{k=0}^{n-1} 10^{sum of lengths of numbers after position k}

    // The sum of lengths of numbers after position k is sum of lengths of n-1-k numbers.

    // Since all permutations are considered, the sum over all subsets of size s of lengths is:
    // sum over all subsets of size s of lengths = C(n, s) * average length * s

    // But we need sum of 10^{sum of lengths}, which is the sum over all subsets of size s of product of 10^{lengths}.

    // This is equivalent to sum over all subsets of size s of product of 10^{length} = sum over all subsets of size s of product of 10^{length} = sum over all subsets of size s of product of 10^{length} = sum over all subsets of size s of product of 10^{length}.

    // This is the coefficient of x^s in the polynomial:
    // P(x) = product over all numbers (1 + 10^{length} * x)

    // Since numbers with same length have same 10^{length}, we can group by length:

    // P(x) = product_{d=1}^6 (1 + 10^d * x)^{countLen[d]}

    // The coefficient of x^s in P(x) is sum over all subsets of size s of product of 10^{lengths}.

    // So, sum over k=0 to n-1 of coefficient of x^{n-1-k} in P(x) = sum over k=0 to n-1 of coefficient of x^{k} in P(x) (reindexing).

    // We want sum over k=0 to n-1 of coefficient of x^k in P(x) * fact[k] * fact[n-1-k]

    // So the answer is:
    // ans = sum_{k=0}^{n-1} fact[k] * fact[n-1-k] * coeff_x^k(P(x)) * sum_{x=1}^n x

    // We can compute P(x) = product_{d=1}^6 (1 + 10^d * x)^{countLen[d]} modulo x^{n} (only up to degree n-1)

    // Since countLen[d] can be large, we use fast exponentiation of polynomials.

    // Each (1 + 10^d * x)^{countLen[d]} is a binomial expansion:
    // sum_{i=0}^{countLen[d]} C(countLen[d], i) * (10^d)^i * x^i

    // So P(x) = product over d of these polynomials.

    // We multiply these 6 polynomials to get P(x).

    // Then compute sum_{k=0}^{n-1} fact[k] * fact[n-1-k] * coeff_x^k(P(x)).

    // Finally multiply by sumX.

    // Implementation:

    // Precompute factorials and inverse factorials done.

    // Precompute powers of 10^d for d=1..6
    vector<int> pow10(7, 1);
    for (int i = 1; i <= 6; i++) pow10[i] = mul(pow10[i - 1], 10);

    // Build polynomials for each length d:
    // poly_d(x) = sum_{i=0}^{countLen[d]} C(countLen[d], i) * (10^d)^i * x^i

    // We'll multiply these 6 polynomials to get P(x).

    // Since countLen[d] can be large (up to n), we cannot build full polynomials naively.

    // But each polynomial is a binomial expansion, so we can use the formula for binomial coefficients and do polynomial multiplication via NTT or FFT.

    // However, since we only have 6 polynomials, we can multiply them one by one using NTT.

    // We'll implement NTT for fast polynomial multiplication.

    // Implement NTT:

    // NTT implementation (from standard templates):

    const int root = 15311432; // primitive root for 998244353
    const int root_1 = 469870224;
    const int root_pw = 1 << 23;

    auto ntt = [&](vector<int> &a, bool invert) {
        int n = (int)a.size();
        for (int i = 1, j = 0; i < n; i++) {
            int bit = n >> 1;
            for (; j & bit; bit >>= 1)
                j ^= bit;
            j |= bit;
            if (i < j) swap(a[i], a[j]);
        }
        for (int len = 2; len <= n; len <<= 1) {
            int wlen = invert ? root_1 : root;
            for (int i = len; i < root_pw; i <<= 1)
                wlen = int((1LL * wlen * wlen) % Mod);
            for (int i = 0; i < n; i += len) {
                int w = 1;
                for (int j = 0; j < len / 2; j++) {
                    int u = a[i + j], v = int((1LL * a[i + j + len / 2] * w) % Mod);
                    a[i + j] = u + v < Mod ? u + v : u + v - Mod;
                    a[i + j + len / 2] = u - v >= 0 ? u - v : u - v + Mod;
                    w = int((1LL * w * wlen) % Mod);
                }
            }
        }
        if (invert) {
            int nrev = binPow(n, Mod - 2);
            for (int &x : a)
                x = int((1LL * x * nrev) % Mod);
        }
    };

    auto multiply = [&](const vector<int> &a, const vector<int> &b) {
        int n = 1;
        while (n < (int)(a.size() + b.size() - 1)) n <<= 1;
        vector<int> fa(a.begin(), a.end()), fb(b.begin(), b.end());
        fa.resize(n);
        fb.resize(n);
        ntt(fa, false);
        ntt(fb, false);
        for (int i = 0; i < n; i++) {
            fa[i] = int((1LL * fa[i] * fb[i]) % Mod);
        }
        ntt(fa, true);
        fa.resize(a.size() + b.size() - 1);
        return fa;
    };

    // Build polynomials for each length d
    // poly_d[i] = C(countLen[d], i) * (10^d)^i mod
    // We'll precompute factorials and inverse factorials for binomial coefficients

    auto C = [&](int n, int r) -> int {
        if (r > n || r < 0) return 0;
        return mul(fact[n], mul(invFact[r], invFact[n - r]));
    };

    vector<int> P = {1}; // start with polynomial 1

    for (int d = 1; d <= 6; d++) {
        if (countLen[d] == 0) continue;
        int c = countLen[d];
        vector<int> poly(c + 1);
        int p10 = 1;
        for (int i = 0; i <= c; i++) {
            poly[i] = mul(C(c, i), p10);
            p10 = mul(p10, pow10[d]);
        }
        P = multiply(P, poly);
        if ((int)P.size() > n) P.resize(n);
    }

    // Now compute sum_{k=0}^{n-1} fact[k] * fact[n-1-k] * P[k]
    int64_t ans = 0;
    for (int k = 0; k < n; k++) {
        int64_t val = (int64_t)P[k] * fact[k] % Mod * fact[n - 1 - k] % Mod;
        ans += val;
    }
    ans %= Mod;

    // Multiply by sumX
    ans = ans * sumX % Mod;

    cout << ans << "\n";

    return 0;
}