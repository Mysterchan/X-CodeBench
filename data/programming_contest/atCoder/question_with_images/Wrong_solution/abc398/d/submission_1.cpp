#include<iostream>
#include<vector>
#include<set>
using namespace std;
int main() {
	int n, r, c;
	string s;
	cin >> n >> r >> c;
	r *= -1;
	cin >> s;
	vector<pair<int, int>>smoke;
	set<pair<int, int>> set;
	set.insert(pair<int, int>(0, 0));
	int a=r, b=c, fr=0, fc=0;
	string ans;
	for (int i = 0; i < n; i++) {
		if (s[i] == 'W') {
			b = b + 1;
			fc += 1;
		}
		if (s[i] == 'E') {
			b = b - 1;
			fr -= 1;
		}
		if (s[i] == 'N') {
			a = a - 1;
			fr -= 1;
		}
		if (s[i] == 'S') {
			a = a + 1;
			fr += 1;
		}
		set.insert(pair<int, int>(fr,fc));
		ans.push_back(set.count(pair<int, int>(a, b))+'0');
	}
	cout<<ans;
}