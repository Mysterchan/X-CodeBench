#include <bits/stdc++.h>
using namespace std;
#define int long long
#define pii pair<int,int>
#define INF LLONG_MAX/20

string tree;
int dfs(int i) {
	if (3*i+1>=tree.length()) return 1;
	int cnt0=0,cnt1=0;
	if (tree[3*i+1]=='0')cnt0++;
	else cnt1++;
	if (tree[3*i+2]=='0')cnt0++;
	else cnt1++;
	if (tree[3*i+3]=='0')cnt0++;
	else cnt1++;
	if (cnt0>cnt1) {
		if (cnt0==2) {
			int ans=INF;
			if (tree[3*i+1]=='1') ans=min(ans,dfs(3*i+1));
			if (tree[3*i+2]=='1') ans=min(ans,dfs(3*i+2));
			if (tree[3*i+3]=='1') ans=min(ans,dfs(3*i+3));
			return ans;
		}
		else {
			int a1=dfs(3*i+1),a2=dfs(3*i+2),a3=dfs(3*i+3);
			return min(a1+a2,min(a2+a3,a1+a3));
		}
	}
	else {
		if (cnt1==2) {
			int ans=INF;
			if (tree[3*i+1]=='0') ans=min(ans,dfs(3*i+1));
			if (tree[3*i+2]=='0') ans=min(ans,dfs(3*i+2));
			if (tree[3*i+3]=='0') ans=min(ans,dfs(3*i+3));
			return ans;
		}
		else {
			int a1=dfs(3*i+1),a2=dfs(3*i+2),a3=dfs(3*i+3);
			return min(a1+a2,min(a2+a3,a1+a3));
		}
	}
}

signed main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	tree="";
	int n;cin>>n;
	
	int len=1; for(int i=0;i<n;i++) len*=3;
	string s;cin>>s;
	vector<string> rows;
	string row_str=s;
	for (int i=0;i<n;i++) {
		rows.push_back(row_str);
		string temp="";
		int cnt0=0,cnt1=0;
		for (char c: row_str) {
			if(c=='0')cnt0++;
			else cnt1++;
			if (cnt0+cnt1==3) {
				if(cnt0>cnt1)temp+='0';
				else temp+='1';
				
				cnt0=0, cnt1=0;
			}
		}
		row_str=temp;
	}
	rows.push_back(row_str);
	reverse(rows.begin(),rows.end());
	for (string x:rows) tree+=x;
	cout<<dfs(0);
	return 0;
}