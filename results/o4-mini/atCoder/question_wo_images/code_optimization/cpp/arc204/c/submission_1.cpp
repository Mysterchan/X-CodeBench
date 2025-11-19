#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int MAXN = 300000;
bitset<MAXN+5> dp;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    vector<int> p(n);
    for(int i = 0; i < n; i++){
        cin >> p[i];
        --p[i];
    }
    vector<bool> vis(n, false);
    vector<int> cycles;
    cycles.reserve(n);
    for(int i = 0; i < n; i++){
        if(!vis[i]){
            int u = i, cnt = 0;
            while(!vis[u]){
                vis[u] = true;
                u = p[u];
                cnt++;
            }
            cycles.push_back(cnt);
        }
    }
    // Count even half-lengths
    int even_tot = 0;
    vector<int> cnt_half(n+1, 0);
    int ones_count = 0;
    vector<int> even_half, odd_big;
    even_half.reserve(cycles.size());
    odd_big.reserve(cycles.size());
    for(int c: cycles){
        if(c % 2 == 0){
            int h = c/2;
            even_tot += h;
            cnt_half[h]++;
            even_half.push_back(h);
        } else {
            if(c == 1){
                ones_count++;
            } else {
                odd_big.push_back(c/2);
            }
        }
    }
    // compress cnt_half
    for(int i = 1; i <= n; i++){
        while(cnt_half[i] > 2){
            cnt_half[i] -= 2;
            if(2*i <= n) cnt_half[2*i]++;
        }
    }
    // build dp for special case
    dp.reset();
    dp[0] = 1;
    for(int i = 1; i <= n; i++){
        for(int t = 0; t < cnt_half[i]; t++){
            dp |= (dp << i);
        }
    }
    // prepare sorted lists and prefix sums
    sort(even_half.begin(), even_half.end(), greater<int>());
    sort(odd_big.begin(), odd_big.end(), greater<int>());
    int E = even_half.size();
    int O = odd_big.size();
    vector<ll> prefE(E+1, 0), prefO(O+1, 0);
    for(int i = 0; i < E; i++){
        prefE[i+1] = prefE[i] + even_half[i];
    }
    for(int i = 0; i < O; i++){
        prefO[i+1] = prefO[i] + odd_big[i];
    }
    int Q;
    cin >> Q;
    while(Q--){
        int a0, b1, c2;
        cin >> a0 >> b1 >> c2;
        // Special case
        if(a0 == b1 && a0 <= even_tot){
            if(dp[a0]){
                cout << (ll)4 * a0 << "\n";
            } else {
                cout << (ll)4 * a0 - 1 << "\n";
            }
            continue;
        }
        int rem = a0;
        ll cnt2 = 0, cnt1 = 0, cnt00 = 0;
        // Part 1: even cycles
        // find k: largest k s.t. prefE[k] <= rem
        int k = int(upper_bound(prefE.begin(), prefE.end(), rem) - prefE.begin()) - 1;
        if(k < 0) k = 0;
        if(k > E) k = E;
        cnt2 += prefE[k];
        rem -= (int)prefE[k];
        if(rem > 0 && k < E){
            // partial on even_half[k]
            cnt1 += 2;
            cnt2 += rem - 1;
            rem = 0;
        }
        // Part 2: odd_big cycles
        if(rem > 0 && O > 0){
            int k2 = int(upper_bound(prefO.begin(), prefO.end(), rem) - prefO.begin()) - 1;
            if(k2 < 0) k2 = 0;
            if(k2 > O) k2 = O;
            cnt1 += 2LL * k2;
            // each full contributes (i-1)
            cnt2 += prefO[k2] - k2;
            rem -= (int)prefO[k2];
            if(rem > 0 && k2 < O){
                // partial on odd_big[k2]
                cnt1 += 2;
                cnt2 += rem - 1;
                rem = 0;
            }
        }
        // Part 3 & 4: single zero assignments on odd cycles
        if(rem > 0){
            int z1 = min(rem, O); // odd_big cycles
            int z2 = min(rem - z1, ones_count);
            cnt00 += (z1 + z2);
            cnt1 -= 2LL * z1;
            cnt2 += z1;
            int rem3 = rem - z1 - z2;
            if(rem3 > 0){
                cnt00 += 2LL * rem3;
                cnt2 -= rem3;
            }
            rem = 0;
        }
        // compute answer
        ll ans = 2LL * a0 - cnt00;
        // use A1 with cnt2 (each gives 2)
        ll use2 = min<ll>(b1, cnt2);
        ans += 2LL * use2;
        b1 -= (int)use2;
        // use remainder with cnt1 (each gives 1)
        ll use1 = min<ll>(b1, cnt1);
        ans += use1;
        cout << ans << "\n";
    }
    return 0;
}