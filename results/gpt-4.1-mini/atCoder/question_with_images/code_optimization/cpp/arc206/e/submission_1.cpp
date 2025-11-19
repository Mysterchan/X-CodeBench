#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int T; cin >> T;
    const ll INF = 1e18;
    while (T--) {
        int N; cin >> N;
        int n = N - 2;
        vector<int> U(n), D(n), L(n), R(n);
        for (int &x : U) cin >> x;
        for (int &x : D) cin >> x;
        for (int &x : L) cin >> x;
        for (int &x : R) cin >> x;

        // The problem reduces to pairing good cells on edges to cover the board.
        // The minimal cost is found by considering pairing strategies on opposite edges.

        // Precompute prefix minima for L and R for solve function
        auto solve = [&](const vector<int>& A, const vector<int>& B) -> ll {
            // For each i, VL[i] = A[i] + min_{j>i} A[j]
            vector<ll> VL(n);
            ll mn = INF;
            for (int i = n - 1; i >= 0; --i) {
                VL[i] = (ll)A[i] + mn;
                mn = min(mn, (ll)A[i]);
            }
            ll best = INF;
            mn = INF;
            ll l = INF;
            for (int i = 0; i < n; ++i) {
                l = min(l, VL[i]);
                ll r = (ll)B[i] + mn;
                ll nxt = (i + 1 == n) ? INF : VL[i + 1];
                best = min(best, r + min(l, nxt));
                mn = min(mn, (ll)B[i]);
            }
            return best;
        };

        ll ans = INF;

        // Try both orientations (rotations)
        for (int rot = 0; rot < 2; ++rot) {
            // Minimal cost pairing L-R and U-D edges
            ans = min(ans, solve(L, R) + solve(U, D));

            // Prepare for more complex combinations
            // Find smallest 3 in L and R, smallest 2 in U and D
            vector<int> SL = L, SR = R, SU = U, SD = D;
            nth_element(SL.begin(), SL.begin() + 2, SL.end());
            nth_element(SR.begin(), SR.begin() + 2, SR.end());
            nth_element(SU.begin(), SU.begin() + 1, SU.end());
            nth_element(SD.begin(), SD.begin() + 1, SD.end());

            ll base = (ll)SU[0] + SU[1] + SD[0] + SD[1];

            // Try pairing L and R in all ways with prefix minima from left to right
            vector<ll> VL(n);
            for (int rot2 = 0; rot2 < 2; ++rot2) {
                ll mn = INF;
                for (int i = 0; i < n; ++i) {
                    VL[i] = (ll)L[i] + mn;
                    mn = min(mn, (ll)L[i]);
                }
                for (int i = 0; i < n; ++i) {
                    ll mn2 = min(VL[i], i ? VL[i - 1] : INF);
                    for (int j = i - 1; j >= 0; --j) {
                        if (j) mn2 = min(mn2, VL[j - 1]);
                        ll v = (ll)R[i] + R[j] + mn2;
                        ans = min(ans, v + base);
                    }
                }
                swap(L, R);
            }

            if (n > 2) {
                // Consider sum of smallest 3 in L and R plus base
                ans = min(ans, (ll)SL[0] + SL[1] + SL[2] + SR[0] + SR[1] + SR[2] + base);
            }

            // Rotate edges: U->R, D->L, L->U, R->D
            swap(U, R);
            swap(D, L);
        }

        cout << ans << '\n';
    }
    return 0;
}