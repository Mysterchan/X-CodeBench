#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

struct sg {
    char c;
    ll cnt;
};

ll rt, ct, ra, ca;
ll n, m, l;
vector<sg> s, t;
vector<pair<ll, pair<ll, ll>>> d1, d2;

void mv(char d, ll &r, ll &c) {
    if (d == 'U') r--;
    else if (d == 'D') r++;
    else if (d == 'L') c--;
    else if (d == 'R') c++;
}

void get_diff(const vector<sg> &seq, vector<pair<ll, pair<ll, ll>>> &res) {
    res.clear();
    ll tot = 0;
    ll dr = 0, dc = 0;
    res.emplace_back(tot, make_pair(dr, dc));
    for (auto &seg : seq) {
        ll cnt = seg.cnt;
        char dir = seg.c;
        ll step_dr = 0, step_dc = 0;
        mv(dir, step_dr, step_dc);
        dr += step_dr * cnt;
        dc += step_dc * cnt;
        tot += cnt;
        res.emplace_back(tot, make_pair(dr, dc));
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> rt >> ct >> ra >> ca;
    cin >> n >> m >> l;
    s.resize(m);
    t.resize(l);
    for (ll i = 0; i < m; i++) {
        cin >> s[i].c >> s[i].cnt;
    }
    for (ll i = 0; i < l; i++) {
        cin >> t[i].c >> t[i].cnt;
    }

    get_diff(s, d1);
    get_diff(t, d2);

    ll ans = 0;
    ll si = 1, ti = 1;
    ll sp = 0, tp = 0;
    ll sd = 0, sc = 0;
    ll td = 0, tc = 0;
    ll idr = rt - ra;
    ll idc = ct - ca;

    // The main optimization is to avoid the O(step) loop when delta_dr or delta_dc != 0.
    // Instead, solve the linear Diophantine equation for k in [1, step]:
    // curr_dr + delta_dr * k == 0 and curr_dc + delta_dc * k == 0
    // => delta_dr * k == -curr_dr and delta_dc * k == -curr_dc
    // Both must hold simultaneously, so:
    // delta_dr * k + curr_dr == 0
    // delta_dc * k + curr_dc == 0
    // => delta_dr * k = -curr_dr
    // => delta_dc * k = -curr_dc
    // So k must satisfy both equations.
    // If delta_dr == 0 and delta_dc == 0, then positions don't change relative to each other,
    // so if currently at same cell, all steps count.

    while (sp < n && tp < n) {
        ll s_end = d1[si].first;
        ll t_end = d2[ti].first;
        ll step = min(s_end - sp, t_end - tp);
        if (step > n - sp) step = n - sp;
        if (step > n - tp) step = n - tp;

        char s_dir = s[si - 1].c;
        char t_dir = t[ti - 1].c;
        ll s_dr = 0, s_dc = 0;
        ll t_dr = 0, t_dc = 0;
        mv(s_dir, s_dr, s_dc);
        mv(t_dir, t_dr, t_dc);

        ll delta_dr = s_dr - t_dr;
        ll delta_dc = s_dc - t_dc;

        ll curr_dr = idr + (sd - td);
        ll curr_dc = idc + (sc - tc);

        if (delta_dr == 0 && delta_dc == 0) {
            // Relative position does not change during these steps
            if (curr_dr == 0 && curr_dc == 0) {
                ans += step;
            }
        } else {
            // Solve for k in [1, step] such that:
            // curr_dr + delta_dr * k == 0
            // curr_dc + delta_dc * k == 0
            // Both must hold simultaneously.

            // If delta_dr == 0:
            //   curr_dr must be 0, else no solution
            // If delta_dc == 0:
            //   curr_dc must be 0, else no solution

            // Otherwise, k = -curr_dr / delta_dr = -curr_dc / delta_dc
            // Check if these values are equal and integer and in [1, step]

            bool possible = true;
            ll k1 = LLONG_MIN, k2 = LLONG_MIN;

            if (delta_dr == 0) {
                if (curr_dr != 0) possible = false;
            } else {
                if ((-curr_dr) % delta_dr != 0) possible = false;
                else k1 = (-curr_dr) / delta_dr;
            }

            if (delta_dc == 0) {
                if (curr_dc != 0) possible = false;
            } else {
                if ((-curr_dc) % delta_dc != 0) possible = false;
                else k2 = (-curr_dc) / delta_dc;
            }

            if (!possible) {
                // no solution
            } else {
                if (delta_dr == 0 && delta_dc == 0) {
                    // already handled above
                } else if (delta_dr == 0) {
                    // k2 must be in [1, step]
                    if (k2 >= 1 && k2 <= step) ans++;
                } else if (delta_dc == 0) {
                    // k1 must be in [1, step]
                    if (k1 >= 1 && k1 <= step) ans++;
                } else {
                    // both delta_dr and delta_dc != 0
                    if (k1 == k2 && k1 >= 1 && k1 <= step) ans++;
                }
            }
        }

        sp += step;
        tp += step;
        sd += s_dr * step;
        sc += s_dc * step;
        td += t_dr * step;
        tc += t_dc * step;

        if (sp == s_end) si++;
        if (tp == t_end) ti++;
    }

    cout << ans << "\n";
    return 0;
}