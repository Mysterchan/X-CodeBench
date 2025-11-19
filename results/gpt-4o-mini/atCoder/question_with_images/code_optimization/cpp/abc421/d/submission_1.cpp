#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

struct sg {
    char c;
    ll cnt;
};

ll rt, ct, ra, ca; 
ll n, m, l; 
vector<sg> s, t; 

// function to get total movements in one direction from the sequences
void get_deltas(const vector<sg>& seq, vector<pair<ll, pair<ll, ll>>>& deltas) {
    deltas.clear();
    ll total_moves = 0, vertical_move = 0, horizontal_move = 0;
    deltas.emplace_back(total_moves, make_pair(vertical_move, horizontal_move));

    for (const auto& seg : seq) {
        ll cnt = seg.cnt;
        char dir = seg.c; 
        if (dir == 'U') vertical_move -= cnt; 
        else if (dir == 'D') vertical_move += cnt; 
        else if (dir == 'L') horizontal_move -= cnt; 
        else if (dir == 'R') horizontal_move += cnt; 

        total_moves += cnt;
        deltas.emplace_back(total_moves, make_pair(vertical_move, horizontal_move));
    }
}

int main() {
    cin >> rt >> ct >> ra >> ca;
    cin >> n >> m >> l;

    for (ll i = 0; i < m; i++) {
        char c;
        ll a;
        cin >> c >> a;
        s.push_back({c, a});
    }

    for (ll i = 0; i < l; i++) {
        char c;
        ll b;
        cin >> c >> b;
        t.push_back({c, b});
    }

    vector<pair<ll, pair<ll, ll>>> d1, d2;
    get_deltas(s, d1);
    get_deltas(t, d2);

    ll ans = 0; 
    ll si = 1, ti = 1; 
    ll sp = 0, tp = 0;

    ll idr = rt - ra; 
    ll idc = ct - ca;

    while (sp < n && tp < n) {
        ll s_end = d1[si].first, t_end = d2[ti].first;
        ll step = min(s_end - sp, t_end - tp);
        step = min(step, n - sp);
        step = min(step, n - tp);

        char s_direction = s[si - 1].c;
        char t_direction = t[ti - 1].c;

        ll s_vertical = (s_direction == 'U' ? -step : (s_direction == 'D' ? step : 0));
        ll s_horizontal = (s_direction == 'L' ? -step : (s_direction == 'R' ? step : 0));

        ll t_vertical = (t_direction == 'U' ? -step : (t_direction == 'D' ? step : 0));
        ll t_horizontal = (t_direction == 'L' ? -step : (t_direction == 'R' ? step : 0));

        ll curr_dr = idr + s_vertical - t_vertical;
        ll curr_dc = idc + s_horizontal - t_horizontal;

        if (curr_dr == 0 && curr_dc == 0) {
            ans += step;
        } else {
            // check where Takahashi and Aoki meet at any step and count occurrences
            for (ll k = 1; k <= step; k++) {
                ll new_dr = idr + (s_vertical - t_vertical) * k;
                ll new_dc = idc + (s_horizontal - t_horizontal) * k;
                if (new_dr == 0 && new_dc == 0) {
                    ans++;
                }
            }
        }
        
        sp += step;
        tp += step;

        if (sp == s_end) si++;
        if (tp == t_end) ti++;
    }
    cout << ans;
    return 0;
}