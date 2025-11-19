#include<bits/stdc++.h>
using namespace std;

int main(){ 
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int tc; cin >> tc;
    while(tc--){
        int n; cin >> n;
        string a, b;
        cin >> a >> b;
        
        vector<int> va, vb;
        for (int i = 0; i < n; i++){
            if (a[i] == '1') va.push_back(i + 1);
            if (b[i] == '1') vb.push_back(i + 1);
        }
        
        vector<int> tda, tdb;
        for (int i = 1; i < va.size(); i++){
            tda.push_back(va[i] - va[i-1]);
        }
        for (int i = 1; i < vb.size(); i++){
            tdb.push_back(vb[i] - vb[i-1]);
        }
        
        int ans = 0x3f3f3f3f;
        bool fdans = false;
        
        for (int type = 0; type <= 1; type++){
            vector<int> da = tda;
            vector<int> db = tdb;
            int dact = da.size();
            int dbct = db.size();
            
            int tans = 0;
            int ct = 0;
            int nsum = 0;
            bool aldn = true;
            
            if (type == 1 && dact > 0){
                da[0]--;
                tans++;
            }
            
            for (int i = 0; i < dbct; i++){
                int e = db[i];
                bool dne = false;
                
                while (ct < dact){
                    if (da[ct] > e){
                        int nw = da[ct] - e;
                        tans += nsum / 2;
                        if (nsum % 2 == 1){
                            tans++;
                            nw--;
                        }
                        nsum = 0;
                        tans += nw / 2;
                        if (nw % 2 == 1){
                            tans++;
                            if (ct + 1 < dact) da[ct + 1]--;
                            else if (ct + 1 == dact) da.push_back(-1);
                        }
                        ct++;
                        dne = true;
                        break;
                    } else if (da[ct] == e && nsum % 2 == 0){
                        tans += nsum / 2;
                        nsum = 0;
                        ct++;
                        dne = true;
                        break;
                    }
                    nsum += da[ct];
                    ct++;
                }
                
                if (ct >= dact || !dne){
                    aldn = false;
                    break;
                }
            }
            
            if (!aldn) continue;
            
            fdans = true;
            nsum = 0;
            for (int i = ct; i < dact; i++) nsum += da[i];
            tans += (nsum + 1) / 2;
            
            int sc = 0;
            if ((nsum % 2 == 1) || (dact < da.size() && da[dact] == -1)) sc++;
            if (type == 1) sc--;
            
            tans += abs((va[va.size()-1] + va[0] + sc) / 2 - (vb[vb.size()-1] + vb[0]) / 2);
            ans = min(ans, tans);
        }
        
        if (!fdans) cout << "-1\n";
        else cout << ans << "\n";
    }
}