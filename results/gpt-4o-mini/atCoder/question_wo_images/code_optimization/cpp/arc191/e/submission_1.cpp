#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define MOD 998244353

void solve() {
    int n;
    ll x, y;
    cin >> n >> x >> y;
    
    vector<ll> A(n), B(n);
    for(int i = 0; i < n; i++) {
        cin >> A[i] >> B[i];
    }

    int even = 0, odd = 0;
    if (x % 2 == y % 2 || all_of(A.begin(), A.end(), [](ll a) { return a == 0; })) {
        for (int i = 0; i < n; i++) {
            if (A[i] == 0 && B[i] % 2 == 0)
                even++;
            else if (A[i] == 0 && B[i] % 2 == 1)
                odd++;
            else {
                odd++;
            }
        }

        // Calculate the total number of valid combinations where Takahashi can win
        ll ans = 0;
        for (int i = 0; i <= odd; i++) {
            if (i > odd - i) continue;
            ll choose = 1; // This would be binomial coefficient C(odd, i).
            for (int j = 0; j < i; j++)
                choose = (choose * (odd - j) % MOD) * ((MOD + 1) / (j + 1)) % MOD;
            ans = (ans + choose) % MOD;
        }

        ans = (ans * pow(2, even, MOD)) % MOD; // Multiply by 2^even
        cout << ans << '\n';
        return;
    }

    if (x % 2 != y % 2) {
        int ta = 0, ao = 0, fi = 0, se = 0;
        for (int i = 0; i < n; i++) {
            if (A[i] == 0) {
                if (B[i] % 2 == 1) fi++;
                else se++;
            } else if (A[i] == 1) {
                if (B[i] % 2 == 0) {
                    ta++;
                    ao++;
                } else {
                    fi++;
                }
            } else {
                if (x % 2 == 0) ta++;
                if (y % 2 == 0) ao++;
            }
        }
        
        // Fast way of computing the number of combinations
        ll ans = 0;
        for (int k = ao + fi + 1; k <= (ao + fi + 1); k++) {
            ll choose = 1;
            for (int j = 0; j < k; j++)
                choose = (choose * (ao + fi - j) % MOD) * ((MOD + 1) / (j + 1)) % MOD;
            ans = (ans + choose) % MOD;
        }
        ans = (ans * pow(2, se, MOD)) % MOD; // Multiply by 2^se
        cout << ans << '\n';
    }
}

ll pow(ll base, ll exp, ll mod) {
    ll result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) 
            result = result * base % mod;
        base = base * base % mod;
        exp /= 2;
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    while (t--) {
        solve();
    }
    return 0;
}
