#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string S;
    cin >> S;
    int n = S.size();
    vector<char> s(S.begin(), S.end());
    vector<bool> isWA(n, false);
    priority_queue<int, vector<int>, greater<int>> pq;

    for (int i = 0; i + 1 < n; i++) {
        if (s[i] == 'W' && s[i + 1] == 'A') {
            isWA[i] = true;
            pq.push(i);
        }
    }

    while (!pq.empty()) {
        int i = pq.top();
        pq.pop();
        if (!isWA[i]) continue;
        // perform replacement at i
        s[i] = 'A';
        s[i + 1] = 'C';
        isWA[i] = false;
        // update neighbors where WA could appear or disappear
        for (int j = i - 1; j <= i + 1; j++) {
            if (j >= 0 && j + 1 < n) {
                bool now = (s[j] == 'W' && s[j + 1] == 'A');
                if (now != isWA[j]) {
                    isWA[j] = now;
                    if (now) pq.push(j);
                }
            }
        }
    }

    // output result
    for (char c : s) {
        cout << c;
    }
    cout << '\n';
    return 0;
}