#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define ar array

const int mxN=4e5;
int n, q;

struct {
	int p[mxN], r[mxN];
	vector<ar<int, 3>> ops;
	vector<int> st;
	void init() {
		iota(p, p+n, 0);
	}
	int find(int x) {
		return x^p[x]?find(p[x]):x;
	}
	bool join(int x, int y) {
		if((x=find(x))==(y=find(y)))
			return 0;
		if(r[x]<r[y])
			swap(x, y);
		ops.push_back({x, y, r[x]==r[y]});
		p[y]=x;
		r[x]+=r[x]==r[y];
		return 1;
	}
	void record() {
		st.push_back(ops.size());
	}
	void rollback() {
		int s=st.back();
		st.pop_back();
		while(ops.size()>s) {
			auto a=ops.back();
			ops.pop_back();
			p[a[1]]=a[1];
			r[a[0]]-=a[2];
		}
	}
} da1, da2, db;

void solve(vector<ar<int, 5>> &qs, int l2=0, int r2=q-1, int ans=0) {
	da1.record();
	da2.record();
	db.record();
	for(auto a : qs) {
		if(a[1]<=l2&&r2<=a[2]) {
			int u=a[3], v=a[4];
			if(a[0]) {
				if(db.join(u, v)) {
					if(da2.join(u, v))
						++ans;
				}
			} else {
				if(da1.join(u, v)) {
					if(!da2.join(u, v))
						--ans;
				}
			}
		}
	}
	if(l2<r2) {
		int m2=(l2+r2)/2;
		vector<ar<int, 5>> ql, qr;
		for(auto a : qs) {
			if(a[1]<=m2)
				ql.push_back(a);
			if(m2<a[2])
				qr.push_back(a);
		}
		solve(ql, l2, m2, ans);
		solve(qr, m2+1, r2, ans);
	} else
		cout << ans << "\n";
	da1.rollback();
	da2.rollback();
	db.rollback();
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	cin >> n >> q;
	map<ar<int, 2>, int> s[2];
	vector<ar<int, 5>> qs;
	for(int i=0; i<q; ++i) {
		char c;
		int x, y;
		cin >> c >> x >> y, --x, --y;
		if(x>y)
			swap(x, y);
		c-='A';
		if(s[c].find({x, y})==s[c].end())
			s[c][{x, y}]=i;
		else {
			qs.push_back({c, s[c][{x, y}], i-1, x, y});
			s[c].erase({x, y});
		}
	}
	for(int c : {0, 1})
		for(auto a : s[c])
			qs.push_back({c, a.second, q-1, a.first[0], a.first[1]});
	da1.init();
	da2.init();
	db.init();
	solve(qs);
}