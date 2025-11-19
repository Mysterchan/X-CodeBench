#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, n) for (int i = 0; i < (n); i++)
#define rep2(i, s, n) for (int i = (s); i < (n); i++)

void vecprint(vector<int> vec) {
    rep(i, vec.size()) {
        cout << vec[i] << endl;
    }
}
void newvecprint(vector<int> vec) {
    rep(i, vec.size()) {
        cout << vec[i] << " ";
    }
    cout << endl;
}

int minval(vector<int> vec) {
    return *min_element(begin(vec), end(vec));
}
int maxval(vector<int> vec) {
    return *max_element(begin(vec), end(vec));
}

void solve() {
    ll a, b;
    cin >> a >> b;
    cout << (a + b) * (a + b) << endl;

    return;
}

int main() {
    solve();
    return 0;
}