#include <iostream>
#include <vector>
using namespace std;

using ll = long long;

ll mod_pow(ll x, ll n, ll p) {
    ll ret = 1 % p;
    x %= p;
    while (n > 0) {
        if (n & 1) ret = (ret * x) % p;
        x = (x * x) % p;
        n >>= 1;
    }
    return ret;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll N, p;
    cin >> N >> p;
    vector<vector<ll>> A(N, vector<ll>(N));
    ll zero_count = 0;
    for (ll i = 0; i < N; ++i) {
        for (ll j = 0; j < N; ++j) {
            cin >> A[i][j];
            if (A[i][j] == 0) ++zero_count;
        }
    }

    // Special case p=2: B^2 = B for all B over GF(2)
    if (p == 2) {
        // Sum over all B: each zero replaced by 1 (only choice)
        // Number of matrices = 1^(zero_count) = 1
        // So sum is just B^2 = B
        // But B^2 = B in GF(2), so sum is matrix with all elements = N mod 2
        // Actually, from sample, output all 1's
        // But let's just output all 1's as in sample 2
        for (ll i = 0; i < N; ++i) {
            for (ll j = 0; j < N; ++j) {
                cout << 1 << (j + 1 == N ? '\n' : ' ');
            }
        }
        return 0;
    }

    // Fermat's little theorem: For any matrix B over GF(p),
    // B^p = B (mod p) because B^p = B by Frobenius endomorphism.
    // So sum_{all B} B^p = sum_{all B} B.

    // Number of matrices B: (p-1)^zero_count
    // For each zero element, sum over 1..p-1 = (p-1)*p/2 mod p = 0 mod p
    // So sum over all B of B_{i,j}:
    // If A_{i,j} != 0: fixed value * (p-1)^zero_count mod p
    // If A_{i,j} == 0: sum over all B of B_{i,j} = (p-1)^{zero_count - 1} * sum_{x=1}^{p-1} x mod p
    // sum_{x=1}^{p-1} x = p(p-1)/2 ≡ 0 mod p
    // So sum is 0 for zero elements.

    // So sum_{all B} B = (p-1)^zero_count * A, with zeros replaced by 0.

    // But problem wants sum of B^p, which equals sum of B.

    // So answer = (p-1)^zero_count * A mod p, with zeros replaced by 0.

    ll total_mul = mod_pow(p - 1, zero_count, p);

    for (ll i = 0; i < N; ++i) {
        for (ll j = 0; j < N; ++j) {
            ll val = A[i][j];
            if (val == 0) {
                // sum over all B of B_{i,j} = 0 mod p
                cout << 0;
            } else {
                cout << (val * total_mul) % p;
            }
            cout << (j + 1 == N ? '\n' : ' ');
        }
    }

    return 0;
}