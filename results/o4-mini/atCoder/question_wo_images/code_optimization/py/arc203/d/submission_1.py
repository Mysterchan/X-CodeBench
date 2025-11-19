#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;
    vector<char> A(N);
    int s = 0;
    for(int i = 0; i < N; i++){
        int x; cin >> x;
        A[i] = (char)x;
        if(x) s++;
    }
    int Q;
    cin >> Q;

    // maintain zero segments: map from l -> r
    map<int,int> seg;
    int t = 0, u = 0; // t = # zero segments, u = # segments of length 1
    // build initial segments
    for(int i = 0; i < N; ){
        if(A[i] == 0){
            int j = i;
            while(j+1 < N && A[j+1] == 0) j++;
            seg[i] = j;
            t++;
            if(j - i + 1 == 1) u++;
            i = j+1;
        } else i++;
    }

    auto removeZero = [&](int i){
        // remove zero at i (0->1): split segment containing i
        auto it = seg.upper_bound(i);
        if(it == seg.begin()) return;
        --it;
        int l = it->first, r = it->second;
        if(r < i) return;
        // remove this segment
        seg.erase(it);
        t--;
        int len = r - l + 1;
        if(len == 1) u--;
        // left part
        if(l <= i-1){
            seg[l] = i-1;
            t++;
            if((i-1) - l + 1 == 1) u++;
        }
        // right part
        if(i+1 <= r){
            seg[i+1] = r;
            t++;
            if(r - (i+1) + 1 == 1) u++;
        }
    };

    auto addZero = [&](int i){
        // add zero at i (1->0): merge with adjacent zero segments if any
        auto itR = seg.find(i+1);
        auto it = seg.upper_bound(i);
        bool left = false, right = false;
        int l1, r1, l2, r2;
        map<int,int>::iterator itL;
        if(it != seg.begin()){
            auto pit = prev(it);
            if(pit->second == i-1){
                left = true;
                itL = pit;
                l1 = pit->first;
                r1 = pit->second;
            }
        }
        if(itR != seg.end()){
            right = true;
            l2 = itR->first;
            r2 = itR->second;
        }
        if(left && right){
            // erase both
            seg.erase(itL);
            seg.erase(itR);
            t -= 2;
            if(r1 - l1 + 1 == 1) u--;
            if(r2 - l2 + 1 == 1) u--;
            // new merged
            seg[l1] = r2;
            t++;
            if(r2 - l1 + 1 == 1) u++;
        } else if(left){
            seg.erase(itL);
            t--;
            if(r1 - l1 + 1 == 1) u--;
            seg[l1] = i;
            t++;
            if(i - l1 + 1 == 1) u++;
        } else if(right){
            seg.erase(itR);
            t--;
            if(r2 - l2 + 1 == 1) u--;
            seg[i] = r2;
            t++;
            if(r2 - i + 1 == 1) u++;
        } else {
            seg[i] = i;
            t++;
            u++;
        }
    };

    while(Q--){
        int qi;
        cin >> qi;
        int i = qi - 1;
        if(A[i] == 0){
            // 0->1
            removeZero(i);
            A[i] = 1;
            s++;
        } else {
            // 1->0
            addZero(i);
            A[i] = 0;
            s--;
        }

        ll ans;
        if(s == N){
            ans = N;
        } else if(s == 0){
            ans = 2;
        } else if(u == t){
            ans = 2 + (A[0] == 0 && A[N-1] == 0 ? 1 : 0);
        } else {
            ans = 3LL * (t - u);
            if(A[0] == 0){
                if(N >= 2 && A[1] == 1) ans += 1;
                else ans -= 1;
            }
            if(A[N-1] == 1){
                ans += 1;
            } else {
                if(N >= 2 && A[N-2] == 1) ans += 2;
            }
        }
        cout << ans << "\n";
    }

    return 0;
}