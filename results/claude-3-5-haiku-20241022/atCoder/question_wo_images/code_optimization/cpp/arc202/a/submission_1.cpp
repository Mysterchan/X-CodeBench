#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    int t;
    cin >> t;
    
    while(t--) {
        int n;
        cin >> n;
        vector<int> a(n);
        for(int i = 0; i < n; i++) {
            cin >> a[i];
        }
        
        ll ans = 0;
        
        while(a.size() > 1) {
            int minPos = 0;
            for(int i = 1; i < a.size(); i++) {
                if(a[i] < a[minPos]) {
                    minPos = i;
                }
            }
            
            if(minPos > 0 && a[minPos] == a[minPos-1]) {
                a[minPos-1]++;
                a.erase(a.begin() + minPos);
                continue;
            }
            
            if(minPos < a.size()-1 && a[minPos] == a[minPos+1]) {
                a[minPos]++;
                a.erase(a.begin() + minPos + 1);
                continue;
            }
            
            int target = INT_MAX;
            if(minPos > 0) target = min(target, a[minPos-1]);
            if(minPos < a.size()-1) target = min(target, a[minPos+1]);
            
            ans += target - a[minPos];
            a[minPos] = target;
        }
        
        cout << ans << '\n';
    }
    
    return 0;
}