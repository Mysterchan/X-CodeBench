#include <bits/stdc++.h>
using namespace std;

int main(){
    int t; cin >> t;
    while(t--){
        int n, k; cin >> n >> k; k-=1;
        vector<int> a(n);
        for(int i = 0; i<n; i++) cin >> a[i];
        set<int> arr_new;
        for(int ele : a){
            if(ele>=a[k]) arr_new.insert(ele);
        }
        bool check = true;
        int water_level = 1;
        vector<int> arr(arr_new.begin(), arr_new.end());
        for(int i = 1; i<arr.size(); i++){
            if(arr[i-1]<(water_level+arr[i]-arr[i-1]-1)){
                cout << "NO" << "\n";
                check = false;
                break;
            }
        }
        if(check) cout << "YES" << "\n";
    }
}