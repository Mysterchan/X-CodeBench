#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;
    vector<int> A(N+1);
    for(int i = 1; i <= N; i++){
        cin >> A[i];
    }
    vector<vector<int>> pos(N+2);
    for(int i = 1; i <= N; i++){
        pos[A[i]].push_back(i);
    }
    ll answer = 0;
    // For y from 1 to N, compute number of subarrays where y exists and y+1 does not.
    for(int y = 1; y <= N; y++){
        // Boundaries from occurrences of y+1
        vector<int> const &bpos = (y+1 <= N ? pos[y+1] : *(vector<int>*)nullptr);
        int prev = 0;
        if(y+1 <= N){
            // process segments between bpos elements
            for(int b : bpos){
                int l = prev + 1;
                int r = b - 1;
                if(l <= r){
                    // compute contribution from segment [l, r]
                    ll len = r - l + 1;
                    ll total = len * (len + 1LL) / 2LL;
                    auto const &py = pos[y];
                    // find indices in pos[y] within [l, r]
                    auto itL = lower_bound(py.begin(), py.end(), l);
                    auto itR = upper_bound(py.begin(), py.end(), r);
                    if(itL != itR){
                        int idxL = int(itL - py.begin());
                        int idxR = int(itR - py.begin()) - 1;
                        ll sumGaps = 0;
                        // gap before first y in segment
                        ll d1 = py[idxL] - l;
                        sumGaps += d1 * (d1 + 1LL) / 2LL;
                        // gaps between y's
                        for(int k = idxL; k < idxR; k++){
                            ll d = py[k+1] - py[k] - 1;
                            sumGaps += d * (d + 1LL) / 2LL;
                        }
                        // gap after last y in segment
                        ll d2 = r - py[idxR];
                        sumGaps += d2 * (d2 + 1LL) / 2LL;
                        answer += (total - sumGaps);
                    }
                }
                prev = b;
            }
            // last segment after last bpos
            int l = prev + 1;
            int r = N;
            if(l <= r){
                ll len = r - l + 1;
                ll total = len * (len + 1LL) / 2LL;
                auto const &py = pos[y];
                auto itL = lower_bound(py.begin(), py.end(), l);
                auto itR = upper_bound(py.begin(), py.end(), r);
                if(itL != itR){
                    int idxL = int(itL - py.begin());
                    int idxR = int(itR - py.begin()) - 1;
                    ll sumGaps = 0;
                    ll d1 = py[idxL] - l;
                    sumGaps += d1 * (d1 + 1LL) / 2LL;
                    for(int k = idxL; k < idxR; k++){
                        ll d = py[k+1] - py[k] - 1;
                        sumGaps += d * (d + 1LL) / 2LL;
                    }
                    ll d2 = r - py[idxR];
                    sumGaps += d2 * (d2 + 1LL) / 2LL;
                    answer += (total - sumGaps);
                }
            }
        } else {
            // y+1 > N, so no boundaries; one segment [1, N]
            int l = 1, r = N;
            ll len = r - l + 1;
            ll total = len * (len + 1LL) / 2LL;
            auto const &py = pos[y];
            if(!py.empty()){
                // All py elements are within [1, N]
                int idxL = 0;
                int idxR = int(py.size()) - 1;
                ll sumGaps = 0;
                ll d1 = py[idxL] - l;
                sumGaps += d1 * (d1 + 1LL) / 2LL;
                for(int k = idxL; k < idxR; k++){
                    ll d = py[k+1] - py[k] - 1;
                    sumGaps += d * (d + 1LL) / 2LL;
                }
                ll d2 = r - py[idxR];
                sumGaps += d2 * (d2 + 1LL) / 2LL;
                answer += (total - sumGaps);
            }
        }
    }
    cout << answer << "\n";
    return 0;
}