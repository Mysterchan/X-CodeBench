#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    string s;
    cin >> n >> s;
    int len = pow(3, n); // length of input string A
    vector<int> count0(len / 3), count1(len / 3); // count of 0s and 1s in each group of 3

    // Count количество of 0s and 1s in each group
    for (int i = 0; i < len; i += 3) {
        count0[i / 3] = (s[i] == '0') + (s[i + 1] == '0') + (s[i + 2] == '0');
        count1[i / 3] = (s[i] == '1') + (s[i + 1] == '1') + (s[i + 2] == '1');
    }

    // Initial majority
    int majority = 0; // 0 if majority is 0, 1 if majority is 1
    for (int i = 0; i < count0.size(); i++) {
        if (count1[i] > count0[i]) {
            majority++;
        }
    }
    majority = (majority > count0.size() / 2) ? 1 : 0;

    // Count minimum changes to flip the result from majority
    int changes = 0;
    if (majority == 1) {
        // Need to turn majority to 0
        for (int i = 0; i < count0.size(); i++) {
            if (count1[i] > count0[i]) {
                // Count how many flip is needed to make 0 the majority
                changes += count1[i] - count0[i] + 1;
            }
        }
    } else {
        // Need to turn majority to 1
        for (int i = 0; i < count0.size(); i++) {
            if (count0[i] > count1[i]) {
                // Count how many flip is needed to make 1 the majority
                changes += count0[i] - count1[i] + 1;
            }
        }
    }

    cout << changes;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    solve();
    return 0;
}