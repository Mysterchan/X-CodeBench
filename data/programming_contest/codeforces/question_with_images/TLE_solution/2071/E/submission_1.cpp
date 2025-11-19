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
    ll f, s, P, S;
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
            nodes[i].P = 1;
            nodes[i].S = 0;
        }
        for (int i = 0; i < n - 1; ++i) {
            int u, v;
            cin >> u >> v;
            nodes[u].neighbors.push_back(v);
            nodes[v].neighbors.push_back(u);
        }

        for (int u = 1; u <= n; ++u) {
            for (int v : nodes[u].neighbors) {
                nodes[u].P = nodes[u].P * nodes[v].f % MOD;
            }
            for (int v : nodes[u].neighbors) {
                nodes[u].S = (nodes[u].S + nodes[v].s * inv(nodes[v].f)) % MOD;
            }
        }

        ll total = 0;

        for (int u = 1; u <= n; ++u) {
            for (int v : nodes[u].neighbors) {
                if (u > v) continue;
                ll term = nodes[u].s * nodes[v].s % MOD;
                term = term * nodes[u].P % MOD;
                term = term * nodes[v].P % MOD;
                term = term * inv(nodes[u].f) % MOD;
                term = term * inv(nodes[v].f) % MOD;
                total = (total + term) % MOD;
            }
        }

        for (int u = 1; u <= n; ++u) {
            for (int v = u + 1; v <= n; ++v) {
                if (find(nodes[u].neighbors.begin(), nodes[u].neighbors.end(), v) != nodes[u].neighbors.end()) {
                    continue;
                }

                vector<int> nu = nodes[u].neighbors;
                vector<int> nv = nodes[v].neighbors;
                sort(nu.begin(), nu.end());
                sort(nv.begin(), nv.end());
                vector<int> common;
                set_intersection(nu.begin(), nu.end(), nv.begin(), nv.end(), back_inserter(common));

                ll product_C = 1;
                ll sum_C = 0;
                for (int w : common) {
                    product_C = product_C * nodes[w].f % MOD;
                    sum_C = (sum_C + nodes[w].s * inv(nodes[w].f)) % MOD;
                }

                ll sum_A_minus_C = (nodes[u].S - sum_C + MOD) % MOD;
                ll sum_B_minus_C = (nodes[v].S - sum_C + MOD) % MOD;

                ll term = nodes[u].s * nodes[v].s % MOD;
                term = term * nodes[u].P % MOD;
                term = term * nodes[v].P % MOD;
                term = term * inv(product_C) % MOD;
                ll part = (sum_C + sum_A_minus_C * sum_B_minus_C % MOD) % MOD;
                term = term * part % MOD;
                total = (total + term) % MOD;
            }
        }

        cout << total << '\n';
    }

    return 0;
}