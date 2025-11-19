#include <bits/stdc++.h>
using namespace std;

const int N = 5e5 + 5;

int mp[4][4] = {{1, 0, 1, 0},
                {0, 1, 0, 1},
                {1, 0, 1, 1},
                {0, 1, 1, 1}};

int n, x, y;
int a[N], b[N];

int work(int *f) {
    int len = 0;
    int i = 1;
    while (i <= n) {
        int val = f[i];
        int cnt = 1;
        while (i + cnt <= n && f[i + cnt] == val) {
            cnt++;
        }
        
        if (val == 0 && cnt >= x) {
            int full = cnt / x;
            int rem = cnt % x;
            for (int j = 0; j < full; j++) {
                f[++len] = 2;
            }
            for (int j = 0; j < rem; j++) {
                f[++len] = 0;
            }
        } else if (val == 1 && cnt >= y) {
            int full = cnt / y;
            int rem = cnt % y;
            for (int j = 0; j < full; j++) {
                f[++len] = 3;
            }
            for (int j = 0; j < rem; j++) {
                f[++len] = 1;
            }
        } else {
            for (int j = 0; j < cnt; j++) {
                f[++len] = val;
            }
        }
        i += cnt;
    }
    return len;
}

int main() {
    cin.tie(0), cout.tie(0);
    ios::sync_with_stdio(0);
    
    cin >> n >> x >> y;
    string s, t;
    cin >> s >> t;
    
    for (int i = 0; i < n; ++i) {
        a[i + 1] = s[i] - '0';
        b[i + 1] = t[i] - '0';
    }
    
    int l1 = work(a), l2 = work(b);
    
    if (l1 != l2) {
        cout << "No\n";
        return 0;
    }
    
    for (int i = 1; i <= l1; ++i) {
        if (a[i] == b[i]) continue;
        
        int pos = -1;
        for (int j = i + 1; j <= l1; ++j) {
            if (a[j] == b[i]) {
                pos = j;
                break;
            }
        }
        
        if (pos == -1) {
            cout << "No\n";
            return 0;
        }
        
        for (int j = pos; j > i; --j) {
            if (!mp[a[j]][a[j - 1]]) {
                cout << "No\n";
                return 0;
            }
            swap(a[j], a[j - 1]);
        }
    }
    
    cout << "Yes\n";
    return 0;
}