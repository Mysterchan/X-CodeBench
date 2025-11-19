#include<bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin >> n;
    
    vector<pair<int,int>> contests(n);
    for(int i = 0; i < n; i++){
        cin >> contests[i].first >> contests[i].second;
    }
    
    const int MAXR = 500000;
    vector<int> final_rating(MAXR + 1);
    
    // For each possible initial rating
    for(int x = 1; x <= MAXR; x++){
        int rating = x;
        for(int i = 0; i < n; i++){
            if(rating >= contests[i].first && rating <= contests[i].second){
                rating++;
            }
        }
        final_rating[x] = rating;
    }
    
    int q;
    cin >> q;
    while(q--){
        int x;
        cin >> x;
        cout << final_rating[x] << "\n";
    }
    
    return 0;
}