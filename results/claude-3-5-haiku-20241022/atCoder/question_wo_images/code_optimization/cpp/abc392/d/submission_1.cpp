#include <algorithm>
#include <cmath>
#include <climits>
#include <iostream>
#include <iomanip>
#include <map>
#include <set>
#include <vector>

using namespace std;
using ll = long long;

int main() {

	cout << setprecision(15);

	int N;
	cin >> N;

	vector<vector<int>> A(N);

	for (int i = 0; i < N; i++) {
		int K;
		cin >> K;
		A[i] = vector<int>(K);
		for (int& a : A[i])
			cin >> a;
	}

	vector<map<int, int>> frq(N);

	for (int i = 0; i < N; i++) {
		for (int a : A[i])
			frq[i][a]++;
	}

	double ans = 0;

	for (int i = 0; i < N; i++) {
		for (int j = i + 1; j < N; j++) {
			double same = 0;
			
			// Iterate through the smaller map for efficiency
			if (frq[i].size() <= frq[j].size()) {
				for (const auto& p : frq[i]) {
					auto it = frq[j].find(p.first);
					if (it != frq[j].end()) {
						same += (double)p.second * it->second;
					}
				}
			} else {
				for (const auto& p : frq[j]) {
					auto it = frq[i].find(p.first);
					if (it != frq[i].end()) {
						same += (double)p.second * it->second;
					}
				}
			}
			
			ans = max(ans, same / A[i].size() / A[j].size());
		}
	}

	cout << ans << endl;

	return 0;
}