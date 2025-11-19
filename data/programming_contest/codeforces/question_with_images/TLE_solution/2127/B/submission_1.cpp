#include<bits/stdc++.h>
using namespace std;
#define int long long 
#define endl '\n'





void code() {
	int n, t;
	cin >> n >> t;
	string s; cin >> s;
	s = '&' + s;
	s = s + '&';
	string tt = s;
	if (t == 1 || t == n) {
		cout << 1 << endl;
		return;
	}

	int flag=1;
	int l = t, r = t;
	int ll = t - 1, rr = t + 1;
	int cnt1 = 1, cnt2 = 1;
	while (1) {
		ll = l - 1;
			while (ll >= 1 && s[ll] == '#') {
				--ll;
			}
			s[ll] = '#';
		while (l >= 1 && s[l-1] == '.') {
			--l;
		}
		--l;
		if (l == 0 || l == -1) {
			break;
		}
		cnt1++;
	}


	while (1) {
		rr = r + 1;
		if (flag == 0 || cnt2 != 1) {
			while ((rr <= n && s[rr] == '#')) {
				++rr;
			}
			if (rr <= n )
				s[rr] = '#';
		}
		while (r <= n && s[r + 1] == '.') {
			++r;
		}
		++r;
		if (r == n + 1 || r == n + 2) {
			break;
		}
		cnt2++;
	}


	int antt = min(cnt1, cnt2);


	 flag = 1;
	 l = t, r = t;
	 ll = t - 1, rr = t + 1;
	 cnt1 = 1, cnt2 = 1;
	 s = tt;

	while(1){
		rr = r + 1;
			while (rr <= n && s[rr] == '#') {
				++rr;
			}
			if (rr != n + 1)
				s[rr] = '#';
		
		while (r <= n && s[r+1] == '.') {
			++r;
		}
		++r;
		if (r==n+1||r==n+2) {
			break;
		}
		cnt2++;
	}

	while (1) {
		   ll = l - 1;
		if (flag == 0||cnt1!=1) {
			while ((ll >= 1 && s[ll] == '#' )) {
				--ll;
			}
			if(ll>=1)
			s[ll] = '#';
		}
		while (l >= 1 && s[l - 1] == '.') {
			--l;
		}
		--l;
		if (l == 0 || l == -1) {
			break;
		}
		cnt1++;
	}







	cout << max(antt, min(cnt1,cnt2)) << endl;

	 

}

signed main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T = 1;
	cin >> T;

	while (T--) {
		code();
	}
}