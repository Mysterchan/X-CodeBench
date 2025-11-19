#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;
    vector<int> p(N+1);
    for(int i = 1; i <= N; i++){
        cin >> p[i];
    }
    vector<int> bit(N+1);
    for(int i = 1; i <= N; i++){
        bit[i] = i & -i;
    }
    auto add = [&](int i, int v){
        for(; i <= N; i += i & -i) bit[i] += v;
    };
    auto sum = [&](int i){
        int s = 0;
        for(; i > 0; i -= i & -i) s += bit[i];
        return s;
    };
    auto findKth = [&](int k){
        int idx = 0;
        int mask = 1 << (31 - __builtin_clz(N));
        int acc = 0;
        for(; mask > 0; mask >>= 1){
            int t = idx + mask;
            if(t <= N && acc + bit[t] < k){
                idx = t;
                acc += bit[t];
            }
        }
        return idx + 1;
    };

    vector<int> ans(N+1);
    for(int i = N; i >= 1; i--){
        int pi = p[i];
        int pos = findKth(pi);
        ans[pos] = i;
        add(pos, -1);
    }
    for(int i = 1; i <= N; i++){
        cout << ans[i] << (i < N ? ' ' : '\n');
    }
    return 0;
}