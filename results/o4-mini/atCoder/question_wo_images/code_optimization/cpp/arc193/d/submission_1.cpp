#include <bits/stdc++.h>
using namespace std;
using ll = long long;

static int posA[1000005], posB[1000005];
static int tda[1000005], tdb[1000005];
static int da[1000005], db[1000005];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    if(!(cin >> T)) return 0;
    while(T--){
        int n;
        cin >> n;
        string A, B;
        cin >> A >> B;
        int cntA = 0, cntB = 0;
        for(int i = 0; i < n; ++i){
            if(A[i] == '1'){
                posA[++cntA] = i + 1;
            }
        }
        for(int i = 0; i < n; ++i){
            if(B[i] == '1'){
                posB[++cntB] = i + 1;
            }
        }
        if(cntB > cntA){
            cout << -1 << '\n';
            continue;
        }
        int dact = cntA - 1;
        int dbct = cntB - 1;
        for(int i = 1; i <= dact; ++i){
            tda[i] = posA[i+1] - posA[i];
        }
        for(int i = 1; i <= dbct; ++i){
            tdb[i] = posB[i+1] - posB[i];
        }
        ll ans = LLONG_MAX;
        bool found = false;
        // Try two types: whether we remove first piece or not
        for(int type = 0; type < 2; ++type){
            // If no gaps, skip type 1
            if(type == 1 && dact < 1) continue;
            // copy tda to da, tdb to db
            for(int i = 1; i <= dact; ++i) da[i] = tda[i];
            da[dact+1] = 0;
            for(int i = 1; i <= dbct; ++i) db[i] = tdb[i];
            ll tans = 0;
            int ct = 1;
            ll nsum = 0;
            bool ok = true;
            if(type == 1){
                // remove first gap by one merge
                da[1]--;
                tans++;
            }
            for(int i = 1; i <= dbct; ++i){
                int need = db[i];
                bool matched = false;
                if(ct > dact){
                    ok = false;
                    break;
                }
                while(true){
                    if(ct > dact){
                        ok = false;
                        break;
                    }
                    if(da[ct] > need){
                        int extra = da[ct] - need;
                        // shrink accumulated sum
                        tans += (nsum >> 1);
                        if(nsum & 1){
                            tans++;
                            extra--;
                        }
                        nsum = 0;
                        // shrink this gap
                        tans += (extra >> 1);
                        if(extra & 1){
                            tans++;
                            da[ct+1]--;
                        }
                        ct++;
                        matched = true;
                        break;
                    } else if(da[ct] == need && ((nsum & 1) == 0)){
                        tans += (nsum >> 1);
                        nsum = 0;
                        ct++;
                        matched = true;
                        break;
                    }
                    nsum += da[ct];
                    ct++;
                }
                if(!ok || !matched){
                    ok = false;
                    break;
                }
            }
            if(!ok) continue;
            found = true;
            // Remaining gaps
            ll rem = 0;
            for(int i = ct; i <= dact; ++i) rem += da[i];
            tans += (rem + 1) / 2;
            // center alignment cost
            int sc = 0;
            if(type == 1) sc--;
            ll midA = (ll)posA[1] + posA[cntA] + sc;
            midA /= 2;
            ll midB = (ll)posB[1] + posB[cntB];
            midB /= 2;
            tans += llabs(midA - midB);
            ans = min(ans, tans);
        }
        if(!found) cout << -1 << '\n';
        else cout << ans << '\n';
    }
    return 0;
}