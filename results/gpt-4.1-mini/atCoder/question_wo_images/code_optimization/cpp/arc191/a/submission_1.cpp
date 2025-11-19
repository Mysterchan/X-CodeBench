#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    string s, t;
    cin >> s >> t;

    // Sort t in descending order to get the largest digits first
    sort(t.begin(), t.end(), greater<char>());

    int idx = 0;
    for (int i = 0; i < n && idx < m; ++i) {
        if (t[idx] > s[i]) {
            s[i] = t[idx];
            ++idx;
        }
    }

    cout << s << "\n";

    return 0;
}