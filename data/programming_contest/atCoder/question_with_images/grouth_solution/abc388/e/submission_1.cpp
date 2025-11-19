#include <iostream>
#include <algorithm>
using namespace std;
int a[1000001];
int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> a[i];
	}
	sort(a, a + n);
	int half = n / 2;
	int j = half;
	int pairs = 0;
	for (int i = 0; i < half; i++) {
		while (j < n && a[i] * 2 > a[j]) {
			j++;
		}
		if (j < n) {
			pairs++;
			j++;
		}
	}
	cout << pairs << endl;
}