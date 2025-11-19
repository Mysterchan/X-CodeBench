#include <iostream>
#include <vector>
using namespace std;

using ll = long long;

ll mod_pow(ll x, ll n, ll p) {
    ll result = 1;
    x %= p;
    while (n > 0) {
        if (n & 1) result = (result * x) % p;
        x = (x * x) % p;
        n >>= 1;
    }
    return result;
}

vector<vector<ll>> solve(const ll n, const ll p, const vector<vector<ll>>& mat) {
    vector<vector<ll>> result(n, vector<ll>(n, 0));
    ll zero_count = 0;

    // Precompute constant contribution and count zeros.
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (mat[i][j] == 0) {
                zero_count++;
            } else {
                result[i][j] = mat[i][j];
            }
        }
    }

    ll const_mul = mod_pow(p - 1, zero_count, p);
    ll var_mul = mod_pow(p - 1, zero_count - 1, p);

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            // Every entry contributes the number of combinations for zeros
            result[i][j] = (result[i][j] * const_mul) % p;
        }
    }
    
    // Reduce counts of zero replacements
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (mat[i][j] == 0) {
                result[i][j] = (result[i][j] - var_mul + p) % p;
            }
        }
    }

    return result;
}

int main() {
    ll n, p;
    cin >> n >> p;
    vector<vector<ll>> mat(n, vector<ll>(n));
  
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> mat[i][j];
        }
    }

    vector<vector<ll>> ans = solve(n, p, mat);
    for (const auto& row : ans) {
        for (const int val : row) {
            cout << val << " ";
        }
        cout << endl;
    }
    return 0;
}
