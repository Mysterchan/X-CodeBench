#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const int MOD = 998244353;

ll mod_pow(ll a, ll b) {
    ll res = 1;
    while (b) {
        if (b & 1) res = res * a % MOD;
        a = a * a % MOD;
        b >>= 1;
    }
    return res;
}

ll inv(ll x) {
    return mod_pow(x, MOD - 2);
}

struct Node {
    ll f, s;
    vector<int> neighbors;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<Node> nodes(n + 1);
        for (int i = 1; i <= n; ++i) {
            ll p, q;
            cin >> p >> q;
            ll f = p * inv(q) % MOD;
            ll s = (q - p) * inv(q) % MOD;
            nodes[i].f = f;
            nodes[i].s = s;
        }
        for (int i = 0; i < n - 1; ++i) {
            int u, v;
            cin >> u >> v;
            nodes[u].neighbors.push_back(v);
            nodes[v].neighbors.push_back(u);
        }

        ll total = 0;

        for (int u = 1; u <= n; ++u) {
            ll P = 1, S = 0;
            for (int v : nodes[u].neighbors) {
                P = P * nodes[v].f % MOD;
                S = (S + nodes[v].s * inv(nodes[v].f)) % MOD;
            }

            for (int v : nodes[u].neighbors) {
                ll term = nodes[u].s * nodes[v].s % MOD;
                term = term * P % MOD;
                term = term * inv(nodes[v].f) % MOD;
                total = (total + term) % MOD;
            }
        }

        for (int u = 1; u <= n; ++u) {
            for (int v : nodes[u].neighbors) {
                if (u > v) continue;
                ll term = nodes[u].s * nodes[v].s % MOD * inv(nodes[u].f) % MOD * inv(nodes[v].f) % MOD;

                ll product_C = 1, sum_C = 0;
                for (int w : nodes[u].neighbors) {
                    if (w == v) continue;
                    product_C = product_C * nodes[w].f % MOD;
                    sum_C = (sum_C + nodes[w].s * inv(nodes[w].f)) % MOD;
                }
                ll sum_A_minus_C = (S - sum_C + MOD) % MOD;
                term = term * ((sum_C + sum_A_minus_C * (S - sum_C + MOD) % MOD) % MOD) % MOD;
                total = (total + term) % MOD;
            }
        }

        cout << total << '\n';
    }

    return 0;
}