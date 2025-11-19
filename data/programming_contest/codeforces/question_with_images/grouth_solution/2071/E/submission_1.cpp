#include <bits/stdc++.h>
using namespace std;

template <int MOD_> struct modnum {
    static constexpr int MOD = MOD_;
    static_assert(MOD_ > 0, "MOD must be positive");

private:
    int v;

public:
    modnum() : v(0) {}
    modnum(int64_t v_) : v(int(v_ % MOD)) { if (v < 0) v += MOD; }
    explicit operator int() const { return v; }
    friend std::istream& operator >> (std::istream& in, modnum& n) { int64_t v_; in >> v_; n = modnum(v_); return in; }

    modnum inv() const {
        int x = v, y = MOD, vx = 1, vy = 0;
        while (x) {
            int k = y / x;
            y %= x;
            vy -= k * vx;
            std::swap(x, y);
            std::swap(vx, vy);
        }
        return modnum(vy < 0 ? MOD + vy : vy);
    }

    modnum& operator *= (const modnum& o) {
        v = int(int64_t(v) * int64_t(o.v) % MOD);
        return *this;
    }
    modnum& operator /= (const modnum& o) {
        return *this *= o.inv();
    }
    friend modnum operator * (const modnum& a, const modnum& b) { return modnum(a) *= b; }
    friend modnum operator / (const modnum& a, const modnum& b) { return modnum(a) /= b; }
};

using num = modnum<998244353>;
using S = array<num, 3>;

S operator += (S &a, S b) {
    a[0] += b[0];
    a[1] += b[1];
    a[2] += b[2];
    return a;
}

S operator *(S a, S b) {
    return {a[0] * b[0], a[0] * b[1] + a[1] * b[0], a[0] * b[2] + a[1] * b[1] + a[2] * b[0]};
}

void solve() {
    int N;
    cin >> N;
    vector<num> pfall(N);
    for (int i = 0; i < N; i++) {
        int p, q;
        cin >> p >> q;
        pfall[i] = num(p) / num(q);
    }
    vector<vector<int>> tree(N);
    for (int i = 0; i < N - 1; i++) {
        int u, v;
        cin >> u >> v;
        u--; v--;
        tree[u].push_back(v);
        tree[v].push_back(u);
    }

    using info_t = array<S, 4>;

    auto ans = [&](auto self, int v, int par) -> info_t {
        vector<info_t> dp_ch;
        for (int w : tree[v]) {
            if (w == par) continue;
            dp_ch.push_back(self(self, w, v));
        }
        info_t res;
        num p = pfall[v];
        {
            S cur {p, 0, 0};
            for (auto dp : dp_ch) {
                S val {0, 0, 0};
                for (int x = 0; x < 4; x++) {
                    val += dp[x] * S{1, x == 1, 0};
                }
                cur = cur * val;
            }
            res[3] = cur;
        }
        {
            res[0] = S{1 - p, 0, 0};
            for (auto dp : dp_ch) {
                info_t nres;
                nres[3] = res[3];
                for (int x = 0; x < 4; x++) {
                    for (int px = 0; px <= 2; px++) {
                        int a = min(2, px + (x <= 2));
                        nres[a] += res[px] * dp[x] * S{1, x == 0, 0};
                    }
                }
                res = nres;
            }
        }
        return res;
    }(0, -1);

    S tot{0, 0, 0};
    for (int x = 0; x < 4; x++) {
        tot += ans[x] * S{1, x == 1, 0};
    }
    cout << tot[2] << '\n';
}

int main() {
    ios_base::sync_with_stdio(false), cin.tie(nullptr);
    int T;
    cin >> T;
    while (T--) solve();
}