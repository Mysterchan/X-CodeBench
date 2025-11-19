#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	int n, m;
	cin >> n;
	cin >> m;
	vector<int> a(m);
	vector<int> b(m);
	vector<int> c(n + 1, 0);
	for (int i = 0;i < m;i++) {
		cin >> a[i];
		cin >> b[i];
	}
	for (int i = 0;i < m;i++) {
		c[a[i]]++;
		c[b[i]]++;
	}
	for (int i = 1;i <= n;i++) {
		if (c[i] != 2) {
			cout << "No";
			return 0;
		}
	}

    vector<bool> used(m, false);

    int e = a[0];
    int start = e;
    int d = 0;

    do {
        bool found = false;
        for (int i = 0; i < m; i++) {
            if (used[i]) continue;
            if (a[i] == e) {
                e = b[i];
                used[i] = true;
                found = true;
                break;
            }
            if (b[i] == e) {
                e = a[i];
                used[i] = true;
                found = true;
                break;
            }
        }
        if (!found) {
            cout << "No";
            return 0;
        }
        d++;
    } while (e != start);

    if (d == m) cout << "Yes";
    else cout << "No";
    return 0;
}