#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, X, Y;
    if (!(cin >> N >> X >> Y)) return 0;
    string S, T;
    cin >> S >> T;

    auto compress = [&](const string &s)->vector<int>{
        vector<int> v;
        v.reserve(s.size());
        int i = 0;
        while (i < (int)s.size()) {
            int j = i + 1;
            while (j < (int)s.size() && s[j] == s[i]) j++;
            int len = j - i;
            if (s[i] == '0') {
                int full = len / X;
                int rem = len % X;
                for (int k = 0; k < full; ++k) v.push_back(2);
                for (int k = 0; k < rem; ++k) v.push_back(0);
            } else {
                int full = len / Y;
                int rem = len % Y;
                for (int k = 0; k < full; ++k) v.push_back(3);
                for (int k = 0; k < rem; ++k) v.push_back(1);
            }
            i = j;
        }
        return v;
    };

    vector<int> A = compress(S);
    vector<int> B = compress(T);
    if (A.size() != B.size()) {
        cout << "No\n";
        return 0;
    }
    int M = A.size();
    // Check fixed tokens
    for (int i = 0; i < M; ++i) {
        bool a_fixed = (A[i] < 2);
        bool b_fixed = (B[i] < 2);
        if (a_fixed || b_fixed) {
            if (A[i] != B[i]) {
                cout << "No\n";
                return 0;
            }
        }
    }
    // Check segments of swappable tokens 2/3
    int i = 0;
    while (i < M) {
        if (A[i] < 2) {
            i++;
            continue;
        }
        int j = i;
        int cnt2_A = 0, cnt3_A = 0;
        int cnt2_B = 0, cnt3_B = 0;
        while (j < M && A[j] >= 2) {
            if (A[j] == 2) cnt2_A++; else cnt3_A++;
            if (B[j] == 2) cnt2_B++; else cnt3_B++;
            j++;
        }
        if (cnt2_A != cnt2_B || cnt3_A != cnt3_B) {
            cout << "No\n";
            return 0;
        }
        i = j;
    }
    cout << "Yes\n";
    return 0;
}