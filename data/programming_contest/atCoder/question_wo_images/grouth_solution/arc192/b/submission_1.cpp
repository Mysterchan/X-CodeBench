# include <bits/stdc++.h>
using namespace std;
#define f first
#define s second
#define pii pair <int, int>
#define pb push_back
const int N = 3e5 + 5;
int a[N], odd;
int main() {
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
        odd += a[i] % 2;
    }
    if (n <= 2) {
        cout << (n % 2 ? "Fennec" : "Snuke");
        exit(0);
    } else if (n <= 3 && odd == 2) {
        cout << "Fennec\n";
        exit(0);
    }
    if (odd % 2) {
        cout << "Fennec\n";
    } else {
        cout <<"Snuke\n";
    }
}
