#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define all(a) begin(a), end(a)
#define len(a) (int)((a).size())

const ll INF = 1'000'000'000'000'000'000;

string do_op(string s, int pos) {
    s.push_back('0');
    s.insert(s.begin(), '0');
    for (int i = pos - 1; i >= 0; --i) {
        if (i + 1 == pos) {
            if (s[i] == '1') s[i + 1] = '1';
        } else {
            s[i + 1] = s[i];
        }
    }

    for (int i = pos + 1; i < len(s); ++i) {
        if (i - 1 == pos) {
            if (s[i] == '1') s[i - 1] = '1';
        } else {
            s[i - 1] = s[i];
        }
    }

    s.pop_back();
    s.erase(s.begin());

    return s;
}

string normed(string a) {
    string res;
    for (auto c : a) {
        if (res.empty() && c == '0') continue;
        res.push_back(c);
    }
    while (res.back() == '0') res.pop_back();
    return res;
}

char mrg(char a, char b, char c) {
    return (a == '0' && b == '0' && c == '0') ? '0' : '1';
}

ll solve(string s,string t) {
    pair<int, int> pos = {len(s) + 1, 0}, pos2 = {len(t) + 1, 0};
    for (int i = 0; i < len(s); ++i) {
        if (s[i] == '1') {
            pos.first = min(pos.first, i);
            pos.second = max(pos.second, i);
        }
        if (t[i] == '1') {
            pos2.first = min(pos2.first, i);
            pos2.second = max(pos2.second, i);
        }
    }

    if ((pos.second - pos.first - 1 - (pos2.second - pos2.first - 1)) % 2 != 0) return INF;
    ll ops = (pos.second - pos.first - 1 - (pos2.second - pos2.first - 1)) / 2;
    ll shft = 0;
    for (int i = 0; i < len(t); ++i) {
        if (t[i] == '1') {
            int pos_s = pos.first + ops;
            shft = abs(pos_s - i);
            break;
        }
    }
    s = normed(s);
    t = normed(t);

    int j = 0;
    for (int i = 0; i < len(s); ) {
        if (s[i] == t[j]) {
            ++i;
            ++j;
        } else {
            if (s[i] == '0') {
                if (i + 2 >= len(s)) {
                    if (mrg(s[i], (i + 1 < len(s)) ? s[i + 1] : '0', '0') == t[j]) {
                        ++j;
                        break;
                    }
                }
                i += 2;
                s[i] = mrg(s[i], s[i - 1], s[i - 2]);
            } else {
                while (true) {
                    if (t[j - 1] == '1') {
                        i += 2;
                        break;
                    }
                    else if (t[j - 2] == '1') {
                        --j;
                        ++i;
                        break;
                    } else {
                        j -= 2;
                    }
                }
            }
        }
    }

    if (j != len(t)) return INF;

    return ops + shft;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;
        string a, b;
        cin >> a >> b;

        string s1 = a, s2, s3, s4;
        for (int i = 0; i < n; ++i) {
            if (a[i] == '1') {
                s2 = do_op(a, i);
                break;
            }
        }
        for (int i = n - 1; i >= 0; --i) {
            if (a[i] == '1') {
                s3 = do_op(a, i);
                break;
            }
        }
        for (int i = n - 1; i >= 0; --i) {
            if (s2[i] == '1') {
                s4 = do_op(s2, i);
                break;
            }
        }

        ll ans = min({solve(s1, b), solve(s2, b) + 1, solve(s3, b) + 1, solve(s4, b) + 2});
        if (ans >= INF) {
            ans = -1;
        } 
        cout << ans << "\n";
    }

    return 0;
} 
