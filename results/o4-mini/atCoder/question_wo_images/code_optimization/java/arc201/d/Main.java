#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    if (!(cin >> T)) return 0;
    while(T--){
        int N;
        ll M;
        cin >> N >> M;
        vector<ll> A(N), B(N);
        for(int i = 0; i < N; i++){
            cin >> A[i];
        }
        for(int i = 0; i < N; i++){
            cin >> B[i];
        }
        sort(A.begin(), A.end());
        sort(B.begin(), B.end());

        // binary search answer
        ll left = 0, right = M - 1;
        vector<int> bad; 
        auto feasible = [&](ll T)->bool{
            // bad shifts count coverage
            bad.assign(N+1, 0);
            for(int i = 0; i < N; i++){
                ll b = B[i];
                // interval1: a in (T - b, M - b)
                ll low1 = T - b;
                ll high1 = M - b;
                int l1 = int(upper_bound(A.begin(), A.end(), low1) - A.begin());
                int r1 = int(lower_bound(A.begin(), A.end(), high1) - A.begin());
                if(l1 < r1){
                    // s = j - i mod N, j in [l1, r1-1]
                    int L = l1 - i;
                    int R = (r1 - 1) - i;
                    int Lm = (L % N + N) % N;
                    int Rm = (R % N + N) % N;
                    if(Lm <= Rm){
                        bad[Lm] += 1;
                        bad[Rm+1] -= 1;
                    } else {
                        // wrap
                        bad[Lm] += 1;
                        bad[N] -= 1;
                        bad[0] += 1;
                        bad[Rm+1] -= 1;
                    }
                }
                // interval2: a in (T + M - b, +inf)
                ll low2 = T + M - b;
                // a[j] <= M-1, so interval2 if low2 < M-1
                if(low2 < M-1){
                    int l2 = int(upper_bound(A.begin(), A.end(), low2) - A.begin());
                    if(l2 < N){
                        int L = l2 - i;
                        int R = (N - 1) - i;
                        int Lm = (L % N + N) % N;
                        int Rm = (R % N + N) % N;
                        if(Lm <= Rm){
                            bad[Lm] += 1;
                            bad[Rm+1] -= 1;
                        } else {
                            bad[Lm] += 1;
                            bad[N] -= 1;
                            bad[0] += 1;
                            bad[Rm+1] -= 1;
                        }
                    }
                }
            }
            // prefix sum to find any shift not covered
            int cur = 0;
            for(int s = 0; s < N; s++){
                cur += bad[s];
                if(cur == 0) return true;
            }
            return false;
        };

        ll ans = M - 1;
        while(left <= right){
            ll mid = (left + right) >> 1;
            if(feasible(mid)){
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        cout << ans << "\n";
    }
    return 0;
}