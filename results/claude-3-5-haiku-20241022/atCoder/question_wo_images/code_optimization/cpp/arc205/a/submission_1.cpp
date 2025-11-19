#include<bits/stdc++.h>
using namespace std;

void solve(){
    int n,q;
    scanf("%d%d",&n,&q);
    getchar();
    vector<vector<char>>s(n + 2,vector<char>(n + 2,'#'));
    for(int i = 1 ; i <= n ; i ++){
        for(int j = 1 ; j <= n ; j ++){
            scanf("%c",&s[i][j]);
        }
        getchar();
    }
    
    // Precompute 2D prefix sum of valid 2x2 squares
    vector<vector<int>> prefix(n + 1, vector<int>(n + 1, 0));
    
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            int val = 0;
            if(i < n && j < n && s[i][j] == '.' && s[i+1][j] == '.' && 
               s[i][j+1] == '.' && s[i+1][j+1] == '.'){
                val = 1;
            }
            prefix[i][j] = val + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1];
        }
    }
    
    while(q--){
        int u,d,l,r;
        scanf("%d%d%d%d",&u,&d,&l,&r);
        
        // Count 2x2 squares where top-left corner is in [u, d-1] x [l, r-1]
        // This ensures all 4 cells of the 2x2 square are within [u,d] x [l,r]
        int result = 0;
        if(d > u && r > l){
            int row_end = d - 1;
            int col_end = r - 1;
            result = prefix[row_end][col_end];
            if(u > 1) result -= prefix[u-1][col_end];
            if(l > 1) result -= prefix[row_end][l-1];
            if(u > 1 && l > 1) result += prefix[u-1][l-1];
        }
        
        printf("%d\n",result);
    }
}

int main(){
    int t = 1;
    while(t--) solve();
    return 0;
}