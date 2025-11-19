#include <bits/stdc++.h>
using namespace std;
#define int long long
#define fastIO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define all(v) v.begin(), v.end()
const int MOD = 998244353, MX = 1e18, MN = -1e18, N = 2e3 + 10;

vector<pair<int,int>> mov = {
	{1, 0}, {-1, 0}, {0, 1}, {0,-1},
	{1, 1}, {1, -1}, {-1, 1}, {-1, -1}
};

signed main(){
	fastIO
	int t;
	cin >> t;
	while (t--) {
		int n;
		cin >> n;
		set<int> st;
		while (n--) {
			int x;
			cin >> x;
			st.insert(x);
		}
		cout << (st.size() == 1 ? "Yes" : "No") << endl;
	}
}