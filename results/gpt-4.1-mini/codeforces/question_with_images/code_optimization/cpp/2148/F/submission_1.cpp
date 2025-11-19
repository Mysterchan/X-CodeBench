#include <bits/stdc++.h>
using namespace std;
using ll=long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll t; cin >> t;
    while(t--){
        ll n; cin >> n;
        vector<vector<ll>> arrays(n);
        ll max_len = 0;
        for(ll i=0; i<n; i++){
            ll k; cin >> k;
            arrays[i].resize(k);
            for(ll j=0; j<k; j++) cin >> arrays[i][j];
            max_len = max(max_len, k);
        }

        // For each column, find the minimal element among arrays that have that column
        // If minimal element is unique, bottom row at that column is that element
        // Else, pick the entire array that contains the minimal element at that column

        // Precompute for each column:
        // minimal value and count of arrays having that minimal value at that column
        // and index of one such array

        vector<ll> bottom_row;
        ll j = 0;
        while(j < max_len){
            ll mini = LLONG_MAX;
            int mini_count = 0;
            int mini_idx = -1;

            for(int i=0; i<n; i++){
                if((ll)arrays[i].size() > j){
                    ll val = arrays[i][j];
                    if(val < mini){
                        mini = val;
                        mini_count = 1;
                        mini_idx = i;
                    } else if(val == mini){
                        mini_count++;
                    }
                }
            }

            if(mini == LLONG_MAX){
                // No arrays have this column, done
                break;
            }

            if(mini_count == 1){
                // Unique minimal element at this column
                bottom_row.push_back(mini);
                j++;
            } else {
                // Multiple arrays have minimal element at this column
                // Append entire array of mini_idx from column j to end
                for(ll pos = j; pos < (ll)arrays[mini_idx].size(); pos++){
                    bottom_row.push_back(arrays[mini_idx][pos]);
                }
                j = arrays[mini_idx].size();
            }
        }

        for(auto &x : bottom_row) cout << x << " ";
        cout << "\n";
    }
}