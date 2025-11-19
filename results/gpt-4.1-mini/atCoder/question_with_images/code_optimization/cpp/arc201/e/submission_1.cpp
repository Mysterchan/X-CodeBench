#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int MOD = 998244353;
const int MAXN = 200000 + 10;

int n;
int Y[MAXN];
int pos[MAXN];
int pw[MAXN];

// Modular addition
inline void add(int &a, int b) {
    a += b;
    if (a >= MOD) a -= MOD;
}

// Modular subtraction
inline int sub(int a, int b) {
    a -= b;
    if (a < 0) a += MOD;
    return a;
}

// Modular multiplication
inline int mul(int a, int b) {
    return (int)((ll)a * b % MOD);
}

// Modular exponentiation
int modpow(int base, int exp) {
    int res = 1;
    while (exp > 0) {
        if (exp & 1) res = mul(res, base);
        base = mul(base, base);
        exp >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> Y[i];
        pos[Y[i]] = i;
    }

    // Precompute powers of 2 modulo MOD
    pw[0] = 1;
    for (int i = 1; i <= n; i++) {
        pw[i] = mul(pw[i - 1], 2);
    }

    // The key insight:
    // The sum of areas over all subsets with at least 2 points can be computed by:
    // sum over all pairs (minY, maxY) of (maxY - minY) * number_of_subsets_with_minY_and_maxY
    // number_of_subsets_with_minY_and_maxY = 2^(maxY - minY - 1) * (pos[maxY] - pos[minY]) (distance in x)
    // But we must sum over all pairs (minY < maxY)
    //
    // We can rewrite the sum as:
    // sum_{minY=1}^{N} sum_{maxY=minY+1}^{N} (maxY - minY) * (pos[maxY] - pos[minY]) * 2^{maxY - minY - 1}
    //
    // To compute efficiently, fix minY and accumulate over maxY > minY.
    // We'll precompute prefix sums to do this in O(N).

    // Precompute prefix sums for pos[i] * 2^i and i * pos[i] * 2^i
    // We'll shift indices by 1 to avoid confusion.

    // We'll use arrays:
    // S1[i] = sum_{k=1}^i pos[k] * pw[k]
    // S2[i] = sum_{k=1}^i k * pos[k] * pw[k]

    // But since the exponent is (maxY - minY - 1), we need to handle powers carefully.

    // Let's define:
    // For fixed minY = m,
    // sum over maxY = m+1 to N of (maxY - m) * (pos[maxY] - pos[m]) * 2^{maxY - m -1}
    //
    // = sum_{d=1}^{N - m} d * (pos[m + d] - pos[m]) * 2^{d - 1}
    //
    // = sum_{d=1}^{N - m} d * pos[m + d] * 2^{d - 1} - pos[m] * sum_{d=1}^{N - m} d * 2^{d - 1}

    // Precompute prefix sums of d * pos[m + d] * 2^{d - 1} for all m efficiently.

    // We'll precompute arrays:
    // For i in [1..N]:
    // A[i] = pos[i]
    // We'll precompute prefix sums of pos[i] * i * 2^{i} and pos[i] * 2^{i}

    // But since d starts from 1, and powers are 2^{d-1}, we can shift indices.

    // Let's precompute:
    // prefixPosPw[i] = sum_{k=1}^i pos[k] * pw[k]
    // prefixPosIdxPw[i] = sum_{k=1}^i k * pos[k] * pw[k]

    // Then for fixed m:
    // sum_{d=1}^{N - m} d * pos[m + d] * 2^{d - 1} 
    // = sum_{x = m+1}^N (x - m) * pos[x] * 2^{x - m - 1}
    //
    // We can rewrite 2^{x - m - 1} = pw[x - m - 1]
    //
    // But prefix sums are with pw[x], so we need to adjust.

    // To handle this, we can precompute arrays with shifted powers.

    // Instead, we can precompute arrays:
    // B[i] = pos[i] * pw[i]
    // C[i] = i * pos[i] * pw[i]

    // Then for fixed m:
    // sum_{x = m+1}^N (x - m) * pos[x] * 2^{x - m - 1}
    // = sum_{x = m+1}^N (x - m) * pos[x] * 2^{x - m - 1}
    // = sum_{x = m+1}^N (x - m) * pos[x] * 2^{x - 1} / 2^{m}
    // = (1 / 2^{m}) * sum_{x = m+1}^N (x - m) * pos[x] * 2^{x - 1}

    // So if we precompute prefix sums of pos[x] * 2^{x - 1} and x * pos[x] * 2^{x - 1}, we can get the sum.

    // Let's define:
    // P1[i] = sum_{k=1}^i pos[k] * 2^{k - 1}
    // P2[i] = sum_{k=1}^i k * pos[k] * 2^{k - 1}

    // Then:
    // sum_{x = m+1}^N (x - m) * pos[x] * 2^{x - 1} 
    // = sum_{x = m+1}^N x * pos[x] * 2^{x - 1} - m * sum_{x = m+1}^N pos[x] * 2^{x - 1}
    // = (P2[N] - P2[m]) - m * (P1[N] - P1[m])

    // Finally, multiply by inv_pw[m] = modular inverse of 2^m to get sum_{d=1}^{N-m} d * pos[m+d] * 2^{d-1}

    // Similarly, sum_{d=1}^{N-m} d * 2^{d-1} = ?

    // sum_{d=1}^L d * 2^{d-1} = 1 + 2*2 + 3*4 + ... + L*2^{L-1}
    // This is a known formula:
    // sum_{d=1}^L d * 2^{d-1} = (L - 1) * 2^L + 1

    // We'll use this formula.

    // So for fixed m:
    // sum_{d=1}^{N-m} d * 2^{d-1} = (N - m - 1) * 2^{N - m} + 1

    // Now we can compute the contribution for each m and sum over m.

    // We'll also need modular inverses of powers of two.

    // Precompute inverse powers of two:
    int inv2 = modpow(2, MOD - 2);
    int inv_pw[MAXN];
    inv_pw[0] = 1;
    for (int i = 1; i <= n; i++) {
        inv_pw[i] = mul(inv_pw[i - 1], inv2);
    }

    // Precompute P1 and P2
    static int P1[MAXN], P2[MAXN];
    P1[0] = 0;
    P2[0] = 0;
    for (int i = 1; i <= n; i++) {
        int val = mul(pos[i], pw[i - 1]); // pos[i] * 2^{i-1}
        P1[i] = P1[i - 1] + val;
        if (P1[i] >= MOD) P1[i] -= MOD;
        int val2 = mul(i, val); // i * pos[i] * 2^{i-1}
        P2[i] = P2[i - 1] + val2;
        if (P2[i] >= MOD) P2[i] -= MOD;
    }

    int ans = 0;
    for (int m = 1; m <= n - 1; m++) {
        // sum_{d=1}^{N-m} d * pos[m+d] * 2^{d-1} = ((P2[N] - P2[m]) - m * (P1[N] - P1[m])) * inv_pw[m] mod
        int part1 = sub(P2[n], P2[m]);
        int part2 = mul(m, sub(P1[n], P1[m]));
        int sum_d_pos = mul(sub(part1, part2), inv_pw[m]);

        // sum_{d=1}^{N-m} d * 2^{d-1} = (N - m - 1) * 2^{N - m} + 1
        int len = n - m;
        int sum_d_pw = 1;
        if (len >= 2) {
            int tmp = mul(len - 1, pw[len]);
            sum_d_pw = (tmp + 1) % MOD;
        } else if (len == 1) {
            sum_d_pw = 1;
        } else {
            sum_d_pw = 0;
        }

        // contribution = (sum_d_pos - pos[m] * sum_d_pw) * (maxY - minY) = (sum_d_pos - pos[m] * sum_d_pw) * (maxY - minY)
        // But maxY - minY = d, which is accounted in sum_d_pos and sum_d_pw already.
        // Actually, the formula is:
        // sum_{d=1}^{N-m} d * (pos[m+d] - pos[m]) * 2^{d-1} = sum_d_pos - pos[m] * sum_d_pw

        int contrib = sub(sum_d_pos, mul(pos[m], sum_d_pw));

        // multiply by (maxY - minY) = d is already included in sums, so no extra multiplication needed.

        // multiply by (j - i) = (pos[maxY] - pos[minY]) is inside pos[] terms.

        // But the problem requires sum over all pairs (i,j) of (j - i) * (maxY - minY) * 2^{maxY - minY -1}
        // We have computed sum over maxY for fixed minY.

        // Now multiply by (pos[maxY] - pos[minY]) is inside pos[] terms.

        // Actually, the formula is:
        // sum_{minY < maxY} (maxY - minY) * (pos[maxY] - pos[minY]) * 2^{maxY - minY -1}
        // = sum_{m=1}^{n-1} contrib

        // But we must multiply contrib by (pos[maxY] - pos[minY])? It's already inside sums.

        // Wait, we must multiply contrib by (pos[maxY] - pos[minY])? No, contrib already includes that.

        // Actually, the formula is:
        // sum_{m=1}^{n-1} contrib * (pos[maxY] - pos[minY]) is inside contrib.

        // So we just add contrib * (m - m) ??? No, m is minY, so no extra multiplication.

        // The problem requires sum over all subsets S with at least 2 points of area of bounding box:
        // area = (maxX - minX) * (maxY - minY)
        // Here, maxX = pos[maxY], minX = pos[minY]
        // So (maxX - minX) = pos[maxY] - pos[minY]
        // (maxY - minY) = maxY - minY

        // The sum over all pairs (minY, maxY) of (maxY - minY) * (pos[maxY] - pos[minY]) * 2^{maxY - minY -1}

        // We have computed sum over maxY for fixed minY of (maxY - minY) * pos[maxY] * 2^{maxY - minY -1}
        // and subtracted pos[minY] * sum_{d} d * 2^{d-1}

        // So contrib is exactly sum_{maxY} (maxY - minY) * (pos[maxY] - pos[minY]) * 2^{maxY - minY -1}

        // Now multiply contrib by (j - i) = (pos[maxY] - pos[minY]) is inside contrib.

        // So just add contrib to answer.

        // But the problem requires sum over all subsets S with at least 2 points of area bounding box modulo MOD.

        // So add contrib to ans.

        add(ans, contrib);
    }

    cout << ans << "\n";

    return 0;
}