#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main() {
	int A;
	cin >> A;

	vector<int> type(A);
	vector<int> p_ans;

	for (int i = 0; i < A;i++)cin >> type[i];

	for (int i = 0; i < A - 1;i++) {
		for (int j = i + 1; j < A;j++) {
			if (type[i] == type[j]) p_ans.push_back(j - i + 1);
		}
	}

	sort(p_ans.begin(), p_ans.end());

	if (p_ans.size() == 0)cout << -1;
	else cout << p_ans[0];

}