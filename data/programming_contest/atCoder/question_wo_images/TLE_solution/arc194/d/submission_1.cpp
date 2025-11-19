#include <bits/stdc++.h>
using namespace std;

#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

template<typename T>
using V = vector<T>;
using ll = long long;

const ll mod = 998244353LL;

int n, d;
string s;

V<V<int>> adj;

V<int> st;
V<ll> f, inv;

V<string> sub;

ll sum, ans;

map<string, ll> mp;

ll exp(ll b, ll e) {
    ll res = 1;
    b %= mod;
    while (e > 0) {
        if (e & 1) res = (res * b) % mod;
        b = (b * b) % mod;
        e >>= 1;
    }
    return res;
}

string dfs(int l, int r, string& s) {
    if (l + 1 == r) return "()";

    int cur_d = 0, occ = 0, last;
    for (int i = l; i <= r; i++) {
        cur_d += (s[i] == '(') ? 1 : -1;

        if (cur_d == 0) occ++;
    }

    if (occ == 1) return "(" + dfs(l + 1, r - 1, s) + ")";

    cur_d = 0, last = l;
    V<string> res;
    for (int i = l; i <= r; i++) {
        cur_d += (s[i] == '(') ? 1 : -1;

        if (cur_d == 0) {
            res.push_back(dfs(last, i, s));
            last = i + 1;
        }
    }

    sort(res.begin(), res.end());

    string ret = "";
    for (auto& it : res) {
        ret += it;
    }

    return ret;
    
}

int main() {
    cin >> n;
    cin >> s;


    f = inv = V<ll>(n + 1);
    f[0] = 1;
    inv[0] = 1;
    for (int i = 1; i <= n; i++) {
        f[i] = (f[i - 1] * i) % mod;

        inv[i] = exp(f[i], mod - 2);
    }

    s = " " + s;

    adj = V<V<int>>(n + 1);
    sub = V<string>(n + 1, " ");
    st.push_back(0);
    for (int i = 1; i <= n; i++) {
        d += (s[i] == '(') ? 1 : -1;

        if (s[i] == '(') {
            if (st.empty()) {
                adj[0].push_back(i);
            }
            else {
                adj[st.back()].push_back(i);
            }
            st.push_back(i);
            for (auto& it : st) {
                sub[it] = sub[it] + '(';
            }
        } else {
            for (auto& it : st) {
                sub[it] = sub[it] + ')';
            }
            st.pop_back();
        }
    }

    ans = 1;
    for (int i = 0; i <= n; i++) {
        mp = map<string, ll>();
        sum = 0;
        for (auto& it : adj[i]) {
            mp[dfs(1, sub[it].size() - 1, sub[it])]++;
            sum++;
        }

        ans = (ans * f[sum]) % mod;
        for (auto& it : mp) {
            ans = (ans * inv[it.second]) % mod;
        }
    }

    cout << ans << endl;
}
