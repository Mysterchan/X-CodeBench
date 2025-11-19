#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i = 0; i < (n); i++)

int main() {
    int X; cin >> X;
    vector<vector<int>>vec(9,vector<int>(9));
    rep(i,9)rep(j,9) vec[i][j]= (i+1)*(j+1);
    int count = 0;
    rep(i,9)rep(j,9) if(X!=vec[i][j]){count += vec[i][j];}
    cout << count << "\n";
}