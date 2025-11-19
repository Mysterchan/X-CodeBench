#include<iostream>
#include<vector>
using namespace std;
using ll = long long;
int main() {
	int n;
	cin >> n;
	vector<int>a(n);
	for (int i = 0; i <= n; i++) {
		cin >> a[i];
		ll b = a[0];
		ll c = a[1];
	
		for (i = 0; i <= n; i++) {
			if (b * a[i] != a[i - 1]*c)
				cout << "No" << endl;
			break;
		}
	}
return 0;
}