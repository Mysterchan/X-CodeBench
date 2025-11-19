#include "bits/stdc++.h"

using namespace std;

constexpr int mod = 998244353;

int normalize(int x) {
    if (x >= mod) {
        x -= mod;
    }
    if (x < 0) {
        x += mod;
    }
    return x;
}

template<typename T>
T power(T a, long long n) {
    T res = 1;
    for (; n; n /= 2, a *= a) {
        if (n % 2) {
            res *= a;
        }
    }
    return res;
}

class Mint {
public:
    int x;

    Mint(int x = 0) : x(normalize(x)) {}
    Mint(long long x) : x(normalize(x % mod)) {}

    int val() const {
        return x;
    }

    Mint operator-() const {
        return Mint(normalize(mod - x));
    }

    Mint inv() const {
        return power(*this, mod - 2);
    }

    Mint& operator*=(const Mint& rhs) {
        x = x * 1ll * rhs.x % mod;
        return *this;
    }

    Mint& operator+=(const Mint& rhs) {
        x = normalize(x + rhs.x);
        return *this;
    }

    Mint& operator-=(const Mint& rhs) {
        x = normalize(x - rhs.x);
        return *this;
    }

    Mint& operator/=(const Mint& rhs) {
        return *this *= rhs.inv();
    }

    friend Mint operator*(const Mint& lhs, const Mint& rhs) {
        Mint res = lhs;
        res *= rhs;
        return res;
    }

    friend Mint operator+(const Mint& lhs, const Mint& rhs) {
        Mint res = lhs;
        res += rhs;
        return res;
    }

    friend Mint operator-(const Mint& lhs, const Mint& rhs) {
        Mint res = lhs;
        res -= rhs;
        return res;
    }

    friend Mint operator/(const Mint& lhs, const Mint& rhs) {
        Mint res = lhs;
        res /= rhs;
        return res;
    }

    bool operator==(const Mint& rhs) const {
        return x == rhs.x;
    }
};

using mint = Mint;

vector<mint> fact(1, 1);
vector<mint> inv_fact(1, 1);

void fast(int n) {
    while ((int) fact.size() < n + 1) {
        fact.push_back(fact.back() * (int) fact.size());
    }
    inv_fact.resize(n + 1, 1);
    inv_fact[n] = 1 / fact[n];
    for (int i = n - 1; i >= 2; i--) {
        inv_fact[i] = inv_fact[i + 1] * (i + 1);
    }
}

mint C(int n, int k) {
    if (k < 0 || k > n) {
        return 0;
    }
    while ((int) fact.size() < n + 1) {
        fact.push_back(fact.back() * (int) fact.size());
        inv_fact.push_back(fact.back().inv());
    }
    return fact[n] * inv_fact[k] * inv_fact[n - k];
}

string to_string(mint x) {
    return to_string(x.x);
}


void solve () {
    int n;
    cin >> n;
    vector<int> p(n), c(n), ip(n);
    for (int i = 0; i < n; i++) {
        cin >> p[i];
        ip[p[i] - 1] = i;
    }
    set<array<int, 4>> st;
    for (int i = 0; i < n; i++) {
        cin >> c[i];
    }
    for (int i = 0; i < n; ) {
        int j = i;
        while (j < n && c[i] == c[j]) {
            j++;
        }
        st.insert({i, j - 1, j - i, c[i]});
        i = j;
    }
    C(2 * n, n);
    mint ans = 1;
    for (auto& ind : ip) {
        auto it = st.lower_bound({ind + 1, -1, -1, -1});
        it = prev(it);
        auto [l, r, cnt, color] = *it;
        ans = ans * cnt;
        st.erase(it);
        cnt--;
        if (cnt) {
            st.insert({l, r, cnt, color});
        } else {
            auto it = st.lower_bound({ind, -1, -1, -1});
            if (it != st.end() && it != st.begin() && (*it)[3] == (*prev(it))[3]) {
                auto [l1, r1, cnt1, color1] = *prev(it);
                auto [l2, r2, cnt2, color2] = *it;
                st.erase({l1, r1, cnt1, color1});
                st.erase({l2, r2, cnt2, color2});
                st.insert({l1, r2, cnt1 + cnt2, color1});
            }
        }
    }
    cout << ans.x << '\n';
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }
}
