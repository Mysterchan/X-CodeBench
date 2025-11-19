#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int MOD = 998244353;

int add(int a, int b) { a += b; if (a >= MOD) a -= MOD; return a; }
int mul(ll a, ll b) { return int((a * b) % MOD); }

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    string s;
    cin >> N >> s;

    // Precompute transitions: for a = 0 or 1, for each state k in [0,15]
    // trans_mid[a][k]: transitions for positions i < N-1
    // trans_end[a][k]: transitions for position i == N-1 (with cycle constraint)
    vector<pair<int,int>> trans_mid[2][16], trans_end[2][16];

    for(int a = 0; a < 2; ++a) {
        for(int k = 0; k < 16; ++k) {
            // nb_mid[nval] accumulates bitmask for mid transitions
            // nb_end[nval] accumulates bitmask for end transitions
            int nb_mid[4] = {0,0,0,0};
            int nb_end[4] = {0,0,0,0};
            // Enumerate according to the original logic
            for(int used = 0; used < 2; ++used) {
                for(int used_first = 0; used_first < 2; ++used_first) {
                    int bitpos = used*2 + used_first;
                    if(((k >> bitpos) & 1) == 0) continue;
                    int nused_first = used_first;
                    for(int nused = 0; nused < 2; ++nused) {
                        // mid (no constraint)
                        for(int c = 0; c <= a; ++c) {
                            int nval = (1 - used) + nused + c;
                            int nbpos = nused*2 + nused_first;
                            nb_mid[nval] |= (1 << nbpos);
                        }
                        // end (with cycle closing constraint)
                        if(nused == used_first) {
                            for(int c = 0; c <= a; ++c) {
                                int nval = (1 - used) + nused + c;
                                int nbpos = nused*2 + nused_first;
                                nb_end[nval] |= (1 << nbpos);
                            }
                        }
                    }
                }
            }
            // Count occurrences for each resulting mask
            // mid transitions
            {
                // map mask -> count
                array<int,16> cnt = {0};
                for(int nval = 0; nval < 4; ++nval) {
                    int m = nb_mid[nval];
                    cnt[m] = (cnt[m] + 1);
                }
                for(int m = 0; m < 16; ++m) {
                    if(cnt[m]) {
                        trans_mid[a][k].emplace_back(m, cnt[m]);
                    }
                }
            }
            // end transitions
            {
                array<int,16> cnt = {0};
                for(int nval = 0; nval < 4; ++nval) {
                    int m = nb_end[nval];
                    cnt[m] = (cnt[m] + 1);
                }
                for(int m = 0; m < 16; ++m) {
                    if(cnt[m]) {
                        trans_end[a][k].emplace_back(m, cnt[m]);
                    }
                }
            }
        }
    }

    // DP arrays
    vector<int> dp(16, 0), ndp(16, 0);
    dp[9] = 1;  // initial state

    // Process i = 0..N-2 with mid transitions
    for(int i = 0; i + 1 < N; ++i) {
        int a = s[i] - '0';
        // reset ndp
        for(int &x : ndp) x = 0;
        // transition
        for(int k = 0; k < 16; ++k) {
            if(dp[k] == 0) continue;
            int v = dp[k];
            auto &vec = trans_mid[a][k];
            for(auto &pr : vec) {
                int nk = pr.first, cnt = pr.second;
                ndp[nk] = (ndp[nk] + (ll)v * cnt) % MOD;
            }
        }
        dp.swap(ndp);
    }
    // Process i = N-1 with end transitions
    {
        int a = s[N-1] - '0';
        for(int &x : ndp) x = 0;
        for(int k = 0; k < 16; ++k) {
            if(dp[k] == 0) continue;
            int v = dp[k];
            auto &vec = trans_end[a][k];
            for(auto &pr : vec) {
                int nk = pr.first, cnt = pr.second;
                ndp[nk] = (ndp[nk] + (ll)v * cnt) % MOD;
            }
        }
        dp.swap(ndp);
    }

    // Sum all dp[k] for k != 0
    int ans = 0;
    for(int k = 1; k < 16; ++k) {
        ans = add(ans, dp[k]);
    }
    cout << ans << "\n";
    return 0;
}