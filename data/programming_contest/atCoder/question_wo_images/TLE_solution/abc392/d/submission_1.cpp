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

	int p = (N >= 70 ? 7 : 1);

	for (int i = 0; i < N; i++) {
		for (int j = i + p; j < N; j++) {
			double same = 0;
			for (int a : A[i])
				same += frq[j][a];
			ans = max(ans, same / A[i].size() / A[j].size());
		}
	}

	cout << ans << endl;

	return 0;
}