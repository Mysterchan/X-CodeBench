#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    if (!(cin >> T)) return 0;
    while (T--){
        int N;
        ll M;
        cin >> N >> M;
        vector<ll> A(N), B(N);
        for (int i = 0; i < N; i++) cin >> A[i];
        for (int i = 0; i < N; i++) cin >> B[i];
        sort(A.begin(), A.end());
        // Prepare L = (M - B[i]) % M, sorted
        vector<ll> L(N);
        for (int i = 0; i < N; i++){
            ll x = (M - B[i]) % M;
            L[i] = x;
        }
        sort(L.begin(), L.end());
        // Prepare points P = A and A+M, sorted
        vector<ll> P;
        P.reserve(2*N);
        for (int i = 0; i < N; i++){
            P.push_back(A[i]);
        }
        for (int i = 0; i < N; i++){
            P.push_back(A[i] + M);
        }
        sort(P.begin(), P.end());
        // binary search on x
        ll lo = 0, hi = M - 1, ans = M - 1;
        auto can = [&](ll x)->bool {
            // We need to match each interval [L[i], L[i]+x] with distinct points in P
            int idxL = 0;
            int matched = 0;
            priority_queue<ll, vector<ll>, greater<ll>> pq;
            int totalP = (int)P.size();
            for (int i = 0; i < totalP; i++){
                ll p = P[i];
                // add all intervals whose start <= p
                while (idxL < N && L[idxL] <= p){
                    pq.push(L[idxL] + x);
                    idxL++;
                }
                // any expired interval?
                while (!pq.empty() && pq.top() < p){
                    return false;
                }
                if (!pq.empty()){
                    // assign p to an interval with smallest end
                    pq.pop();
                    matched++;
                    if (matched == N) return true;
                }
            }
            return false;
        };

        while (lo <= hi){
            ll mid = lo + ((hi - lo) >> 1);
            if (can(mid)){
                ans = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        cout << ans << '\n';
    }
    return 0;
}