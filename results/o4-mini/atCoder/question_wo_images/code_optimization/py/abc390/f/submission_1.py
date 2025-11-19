#include <bits/stdc++.h>
using namespace std;
using int64 = long long;

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
        int v = A[i];
        if(v >= 1 && v <= N) pos[v].push_back(i);
    }
    int64 total_sub = (int64)N * (N + 1) / 2;

    // Compute S1: sum of distinct counts over all subarrays
    int64 S1 = 0;
    for(int v = 1; v <= N; v++){
        auto &p = pos[v];
        int m = p.size();
        if(m == 0) continue;
        int prev = 0;
        for(int idx = 0; idx < m; idx++){
            int cur = p[idx];
            int64 left_choices = cur - prev;
            int64 right_choices = N - cur + 1;
            S1 += left_choices * right_choices;
            prev = cur;
        }
    }

    // Compute S2: sum over subarrays of count of consecutive present pairs
    int64 S2 = 0;
    // Temporary lambdas to compute missing count for a single list
    auto compute_missing = [&](const vector<int> &p)->int64 {
        int64 miss = 0;
        int prev = 0;
        for(int x : p){
            int len = x - prev - 1;
            if(len > 0){
                miss += (int64)len * (len + 1) / 2;
            }
            prev = x;
        }
        int len = N - prev;
        if(len > 0){
            miss += (int64)len * (len + 1) / 2;
        }
        return miss;
    };

    for(int v = 1; v < N; v++){
        auto &p1 = pos[v];
        auto &p2 = pos[v+1];
        // missing subarrays without v
        int64 miss1 = compute_missing(p1);
        // missing subarrays without v+1
        int64 miss2 = compute_missing(p2);
        // missing subarrays without both v and v+1
        int64 miss_both = 0;
        int prev = 0;
        int i = 0, j = 0;
        int sz1 = p1.size(), sz2 = p2.size();
        while(i < sz1 || j < sz2){
            int x;
            if(j >= sz2 || (i < sz1 && p1[i] < p2[j])){
                x = p1[i++];
            } else {
                x = p2[j++];
            }
            int len = x - prev - 1;
            if(len > 0){
                miss_both += (int64)len * (len + 1) / 2;
            }
            prev = x;
        }
        {
            int len = N - prev;
            if(len > 0){
                miss_both += (int64)len * (len + 1) / 2;
            }
        }
        int64 cnt_both = total_sub - miss1 - miss2 + miss_both;
        S2 += cnt_both;
    }

    int64 answer = S1 - S2;
    cout << answer << "\n";
    return 0;
}