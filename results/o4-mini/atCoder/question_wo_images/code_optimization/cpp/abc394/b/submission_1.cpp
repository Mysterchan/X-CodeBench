#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<string> S(N);
    for (int i = 0; i < N; i++) {
        cin >> S[i];
    }

    sort(S.begin(), S.end(), [](const string &a, const string &b) {
        return a.size() < b.size();
    });

    for (const auto &str : S) {
        cout << str;
    }
    cout << '\n';

    return 0;
}