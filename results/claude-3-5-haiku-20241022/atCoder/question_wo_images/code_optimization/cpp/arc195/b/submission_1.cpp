#include<bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;
    
    vector<int> a(n), b(n);
    vector<int> valid_a, valid_b;
    int cnt_wild = 0;
    int mx = 0;
    
    for(int i = 0; i < n; i++){
        cin >> a[i];
        if(a[i] == -1) cnt_wild++;
        else {
            valid_a.push_back(a[i]);
            mx = max(mx, a[i]);
        }
    }
    
    for(int i = 0; i < n; i++){
        cin >> b[i];
        if(b[i] == -1) cnt_wild++;
        else {
            valid_b.push_back(b[i]);
            mx = max(mx, b[i]);
        }
    }
    
    // If we have enough wildcards to fill everything
    if(cnt_wild >= n){
        cout << "Yes\n";
        return 0;
    }
    
    // Sort for efficient matching
    sort(valid_a.begin(), valid_a.end());
    sort(valid_b.begin(), valid_b.end());
    
    // Try different sums starting from mx
    for(int s = mx; s <= mx + n; s++){
        // Count how many pairs we can match with sum s
        int matched = 0;
        vector<bool> used_a(valid_a.size(), false);
        vector<bool> used_b(valid_b.size(), false);
        
        for(int i = 0; i < valid_a.size(); i++){
            for(int j = 0; j < valid_b.size(); j++){
                if(!used_a[i] && !used_b[j] && valid_a[i] + valid_b[j] == s){
                    matched++;
                    used_a[i] = true;
                    used_b[j] = true;
                    break;
                }
            }
        }
        
        // Check if we can fill the rest with wildcards
        if(matched + cnt_wild >= n){
            cout << "Yes\n";
            return 0;
        }
    }
    
    cout << "No\n";
    return 0;
}