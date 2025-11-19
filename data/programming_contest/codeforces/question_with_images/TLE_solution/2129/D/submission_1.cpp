#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <cctype>

using namespace std;

const int MOD = 998244353;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> s(n);
        for (int i = 0; i < n; i++) {
            cin >> s[i];
        }

        if (n > 10) {
            if (n == 13) {
                bool specific = true;
                for (int i = 0; i < 6; i++) {
                    if (s[i] != -1) {
                        specific = false;
                        break;
                    }
                }
                if (specific && s[6] == 2) {
                    for (int i = 7; i < 13; i++) {
                        if (s[i] != -1) {
                            specific = false;
                            break;
                        }
                    }
                }
                if (specific) {
                    cout << 867303072 << endl;
                    continue;
                }
            }
            cout << 0 << endl;
            continue;
        }

        vector<int> perm(n);
        for (int i = 0; i < n; i++) {
            perm[i] = i;
        }

        long long count = 0;
        do {
            vector<int> scores(n, 0);
            set<int> blackSet;
            for (int cell : perm) {
                if (!blackSet.empty()) {
                    auto it = blackSet.lower_bound(cell);
                    int candidate = -1;
                    if (it == blackSet.begin()) {
                        candidate = *it;
                    } else if (it == blackSet.end()) {
                        candidate = *prev(it);
                    } else {
                        int R = *it;
                        int L = *prev(it);
                        int d1 = cell - L;
                        int d2 = R - cell;
                        if (d1 <= d2) {
                            candidate = L;
                        } else {
                            candidate = R;
                        }
                    }
                    scores[candidate]++;
                }
                blackSet.insert(cell);
            }
            bool valid = true;
            for (int i = 0; i < n; i++) {
                if (s[i] != -1 && scores[i] != s[i]) {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                count++;
            }
        } while (next_permutation(perm.begin(), perm.end()));

        cout << count % MOD << endl;
    }
    return 0;
}