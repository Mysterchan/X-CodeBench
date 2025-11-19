#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q;
    vector<int> loc(N+1), cnt(N+1, 1);
    for(int i = 1; i <= N; i++){
        loc[i] = i;
    }
    int doubles = 0;
    while(Q--){
        int t;
        cin >> t;
        if(t == 1){
            int p, h;
            cin >> p >> h;
            int old = loc[p];
            // remove from old nest
            if(cnt[old] == 2) {
                doubles--;
            }
            cnt[old]--;
            // add to new nest h
            if(cnt[h] == 1) {
                doubles++;
            }
            cnt[h]++;
            loc[p] = h;
        } else {
            cout << doubles << "\n";
        }
    }
    return 0;
}