#include <bits/stdc++.h>
    
using namespace std;
typedef long long ll;

const int N = (int)1e6 + 12, MOD = 998244353, inf = (int)1e9 + 1;

int col[N];
bool can(vector<array<int, 2>> a, int n) {
    for(int i = 0; i < n - 1; i++) {
        if((i + 1) * 2 < n) continue;
        for(int j = 0; j < n; j++) {
            col[j] = 0;
        }
        bool ok = 1;
        int l = n - i - 1;
        for(int j = 0; j < l; j++) {
            col[j] = a[j][1] - a[j][0] + 1;
        }
        for(int j = l; j < n; j++) {
            int prv = j - l;
            int len = (a[j][1] - a[j][0] + 1), nd = col[prv];
            if(nd > len) {
                ok = 0;
                break;
            }
            col[j] = len - nd;
            if(j > i) {
                if(col[j]) {
                    ok = 0;
                }
            }
        }
        vector<int> st, st1;
        for(int j = 0; j <= i; j++) {
            st.push_back(a[j][0]);
        }
        for(int j = l; j < n; j++) {
            st1.push_back(a[j][0] + col[j] + 1);
        }
        for(int j = 1; j < (int)st1.size(); j++) {
            if(st1[j] - st1[j - 1] != st[j] - st[j - 1]) {
                ok = 0;
                break;
            }
        }
        if(ok) return true;
    }
    return false;
}
int n;
void test() {
    cin >> n;
    vector<array<int, 2>> a(n), b(n);
    for(int i = 0; i < n; i++) {
        cin >> a[i][0] >> a[i][1];
        b[i][0] = inf - a[i][1];
        b[i][1] = inf - a[i][0];
    }
    if(can(a, n) || can(b, n)) {
        cout << "YES\n";
        return;
    }
    bool ok = 1;
    for(int i = 0; i < n; i++) {
        if((a[i][1] - a[i][0]) % 2 != 1) {
            ok = 0;
            break;
        }
        int mid = (a[i][0] + a[i][1]) / 2 + 1;
        if(i + 1 < n && a[i + 1][1] < mid) {
            ok = 0;
            break;
        }
    }
    for(int i = 1; i < n; i++) {
        int mid = (a[i][0] + a[i][1]) / 2 + 1;
        if(mid > a[i - 1][1]) {
            ok = 0;
            break;
        }
    }
    if(ok) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    int t = 1;
    cin >> t;

    while(t--) {
        test();
    }
}