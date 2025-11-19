#include <bits/stdc++.h>
using namespace std;
#ifdef LOCAL
string to_string(string s) { return '"' + s + '"'; }
string to_string(const char* s) { return to_string(string(s)); }
string to_string(bool b) { return to_string(int(b)); }
string to_string(vector<bool>::reference b) { return to_string(int(b)); }
string to_string(char b) { return "'" + string(1, b) + "'"; }
template <typename A, typename B>
string to_string(pair<A, B> p) { return "(" + to_string(p.first) + ", " + to_string(p.second) + ")"; }
template <typename A, typename B, typename C>
string to_string(tuple<A, B, C> p) {
	return "(" + to_string(get<0>(p)) + ", " + to_string(get<1>(p)) + ", " + to_string(get<2>(p)) + ")";
}
template <typename A, typename T = typename A::value_type>
string to_string(A v) {
	string res = "{";
	for (const auto& x : v) res += (res == "{" ? "" : ", ") + to_string(x);
	return res + "}";
}
void debug() { cerr << endl; }
template <typename Head, typename... Tail>
void debug(Head H, Tail... T) {
	cerr << " " << to_string(H);
	debug(T...);
}
#define db(...) cerr << "[" << #__VA_ARGS__ << "]:", debug(__VA_ARGS__)
#else
#define db(...) 42
#endif
using ll = long long;
using ld = long double;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	int tc;
	cin >> tc;
	while (tc--) {
		int n;
		cin >> n;
		n -= 2;
		const ll INF = 1e18;
		auto solve = [&](const vector<int>& L, const vector<int>& R) {
			vector<ll> VL(n);
			{
				ll mn = INF;
				for (int i = n - 1; i >= 0; --i) {
					VL[i] = L[i] + mn;
					mn = min(mn, (ll)L[i]);
				}
			}
			ll mn = INF, l = INF, best = INF;
			for (int i = 0; i < n; ++i) {
				l = min(l, VL[i]);
				ll r = R[i] + mn;
				best = min(best, r + min(l, i + 1 == n ? INF : VL[i + 1]));
				mn = min(mn, (ll)R[i]);
			}
			return best;
		};
		vector<int> U(n), D(n), L(n), R(n);
		for (int& x : U) cin >> x;
		for (int& x : D) cin >> x;
		for (int& x : L) cin >> x;
		for (int& x : R) cin >> x;
		ll best = INF;
		for (int rot : {0, 1}) {
			best = min(best, solve(L, R) + solve(U, D));
			auto SL = L;
			auto SR = R;
			auto SU = U;
			auto SD = D;
			nth_element(SL.begin(), SL.begin() + 2, SL.end());
			nth_element(SR.begin(), SR.begin() + 2, SR.end());
			nth_element(SU.begin(), SU.begin() + 1, SU.end());
			nth_element(SD.begin(), SD.begin() + 1, SD.end());
			ll base = SU[0] + SU[1];
			base += SD[0] + SD[1];
			vector<ll> VL(n);
			for (int rot2 : {0, 1}) {
				{
					ll mn = INF;
					for (int i = 0; i < n; ++i) {
						VL[i] = L[i] + mn;
						mn = min(mn, (ll)L[i]);
					}
				}
				for (int i = 0; i < n; ++i) {
					ll mn = min(VL[i], i ? VL[i - 1] : INF);
					for (int j = i - 1; j >= 0; --j) {
						if (j) mn = min(mn, VL[j - 1]);
						ll v = R[i] + R[j];
						v += mn;
						best = min(best, v + base);
					}
				}
				swap(L, R);
			}
			if (n > 2) {
				best = min(best, (ll)SL[0] + SL[1] + SL[2] + SR[0] + SR[1] + SR[2] + base);
			}
			swap(U, R);
			swap(D, L);
		}
		cout << best << '\n';
	}
}
