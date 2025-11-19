#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, Q;
    cin >> N >> Q;
    vector<string> a(N+2);
    for(int i = 1; i <= N; i++){
        cin >> a[i];
    }
    // build 2D prefix of 2x2 all-white cells
    vector<vector<int>> pre(N+1, vector<int>(N+1, 0));
    for(int i = 1; i < N; i++){
        for(int j = 1; j < N; j++){
            int is_white_block = 0;
            if (a[i][j-1]=='.' && a[i+1][j-1]=='.' && a[i][j]=='.' && a[i+1][j]=='.')
                is_white_block = 1;
            pre[i][j] = pre[i-1][j] + pre[i][j-1] - pre[i-1][j-1] + is_white_block;
        }
    }

    while(Q--){
        int u, d, l, r;
        cin >> u >> d >> l >> r;
        // we need to count blocks starting at (i,j) with u <= i <= d-1, l <= j <= r-1
        int x1 = u, y1 = l;
        int x2 = d - 1, y2 = r - 1;
        if(x1 > x2 || y1 > y2){
            cout << 0 << '\n';
        } else {
            int res = pre[x2][y2] - pre[x1-1][y2] - pre[x2][y1-1] + pre[x1-1][y1-1];
            cout << res << '\n';
        }
    }
    return 0;
}