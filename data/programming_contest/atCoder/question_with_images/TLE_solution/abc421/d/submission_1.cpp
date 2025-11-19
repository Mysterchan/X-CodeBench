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
vector<pair<ll, pair<ll, ll>>> d1, d2;
void mv (char d, ll & r, ll & c) {
	if (d == 'U') {
		r--;
	}
	if (d == 'D') {
		r++;
	}
	if (d == 'L') {
		c--;
	}
	if (d == 'R') {
		c++;
	}
}
void get_diff (const vector<sg> &seq, vector<pair<ll, pair<ll, ll>>> &res) {
	res.clear ();
	ll tot = 0; 
	ll dr = 0; 
	ll dc = 0; 
	res.emplace_back (tot, make_pair (dr, dc));

	for (auto &seg : seq) {
		ll cnt = seg.cnt;
		char dir = seg.c; 
		ll step_dr = 0;
		ll step_dc = 0; 
		mv (dir, step_dr, step_dc);
		dr += step_dr * cnt;
		dc += step_dc * cnt;
		tot += cnt;
		res.emplace_back (tot, make_pair (dr, dc));
	}
}

int main () {
	cin >> rt >> ct >> ra >> ca;
	cin >> n >> m >> l;
	for (ll i = 0; i < m; i++) {
		char c;
		ll a;
		cin >> c >> a;
		s.push_back ({c, a});
	}
	for (ll i = 0; i < l; i++) {
		char c;
		ll b;
		cin >> c >> b;
		t.push_back ({c, b});
	}
	get_diff (s, d1);
	get_diff (t, d2);
	ll ans = 0; 
	ll si = 1, ti = 1; 
	ll sp = 0, tp = 0; 
	ll sd = 0, sc = 0;
	ll td = 0, tc = 0; 
	ll idr = rt - ra; 
	ll idc = ct - ca; 
	while (sp < n && tp < n) {
		ll s_end = d1 [si].first;
		ll t_end = d2 [ti].first;
		ll step = min (s_end - sp, t_end - tp);
		if (step > n - sp) step = n - sp; 
		if (step > n - tp) step = n - tp;
		char s_dir = s [si - 1].c;
		char t_dir = t [ti - 1].c;
		ll s_dr = 0, s_dc = 0;
		ll t_dr = 0, t_dc = 0;
		mv (s_dir, s_dr, s_dc);
		mv (t_dir, t_dr, t_dc);
		ll delta_dr = s_dr - t_dr;
		ll delta_dc = s_dc - t_dc;
		ll curr_dr = idr + (sd - td);
		ll curr_dc = idc + (sc - tc);
		if (delta_dr == 0 && delta_dc == 0) {
			if (curr_dr == 0) {
				if (curr_dc == 0) {
					ans += step;
				}
			}
		} else {
			for (ll k = 1; k <= step; k++) {
				ll new_dr = curr_dr + delta_dr * k;
				ll new_dc = curr_dc + delta_dc * k;
				if (new_dr == 0 && new_dc == 0) {
					ans++;
				}
			}
		}
		sp += step;
		tp += step;
		sd += s_dr * step;
		sc += s_dc * step;
		td += t_dr * step;
		tc += t_dc * step;
		if (sp == s_end) {
			si++;
		}
		if (tp == t_end) {
			ti++;
		}
	}
	cout << ans;
	return 0;
}