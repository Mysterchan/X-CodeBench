#include<bits/stdc++.h>

using namespace std;

main() {
#ifdef HOME
    freopen("input.txt", "r", stdin);
#endif
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    while (t--) {
        int s, k;
        cin >> s >> k;
        if (s % k == 0) {
            cout << k << '\n';
            continue;
        }
        int ans = 0;
        unordered_set < int > used = {0};
        int head = 0, to = 1, len = k;
        while (!ans) {
            unordered_set < int > nxt;
            int flag = 0;
            for (auto x : used) {
                if (to == 1 || len == 1) {
                    if ((s - x) % len == 0) {
                        ans = len;
                        break;
                    }
                }
                if (to == 1) {
                    if (min(x, s - x) >= len * len) flag = 1;
                }
            }
            if (ans) break;
            if (flag) {
                ans = max(1, ans - 2);
                break;
            }
            for (auto x : used) {
                if (to == 1) {
                    for (int i = 1; x + i * len < s && i <= len; i++) {
                        int pos = x + i * len;
                        int up = to * (-1);
                        nxt.insert(pos);
                    }
                    int mx = (s - x) / len;
                    for (int i = mx; i >= max(len + 1, mx - len + 1); i--) {
                        int pos = x + i * len;
                        int up = to * (-1);
                        nxt.insert(pos);
                    }
                } else {
                    for (int i = 1; x - i * len >= 0 && i <= len; i++) {
                        int pos = x - i * len;
                        int up = to * (-1);
                        nxt.insert(pos);
                    }
                    int mx = x / len;
                    for (int i = mx; i >= max(len + 1, mx - len + 1); i--) {
                        int pos = x - i * len;
                        int up = to * (-1);
                        nxt.insert(pos);
                    }
                }
            }
            to *= (-1), len--;
            used = nxt;
        }
        cout << ans << '\n';
    }
    return 0;
}

