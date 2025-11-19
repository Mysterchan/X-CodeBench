#include <bits/stdc++.h>
using namespace std;

int N, M;
string S;
map<vector<int>, long long> DP[101];
long long res[11];

const long long MOD = 998244353;

int main() {
	cin >> N >> M >> S;
	string T = S;
	sort(T.begin(), T.end());
	T.erase(unique(T.begin(), T.end()), T.end());
	long long rem = 26 - T.size();
	vector<int> v;
	for (int i = 0; i < N; i++) {
		v.push_back(0);
	}
	DP[0][v] = 1;
	for (int i = 0; i < M; i++) {
		for (auto vv : DP[i]) {
			vector<int> vec = vv.first;
			long long val = vv.second % MOD;
			DP[i + 1][vec] += val * rem;
			for (char c : T) {
				vector<int> u = vec;
				int ma = 0;
				for (int i = 0; i < N; i++) {
					int pma = ma;
					ma = max(ma, u[i]);
					if (c == S[i]) {
						u[i] = pma + 1;
					}
				}
				DP[i + 1][u] += val;
			}
		}
	}

	for (auto vv : DP[M]) {
		vector<int> vec = vv.first;
		long long val = vv.second % MOD;

		int lcs = 0;
		for (int i = 0; i < N; i++) {
			lcs = max(lcs, vec[i]);
		}
		res[lcs] += val;
	}
	for (int i = 0; i <= N; i++) {
		cout << res[i] % MOD << " \n"[i == N];
	}
}