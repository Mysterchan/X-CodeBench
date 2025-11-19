

#include <bits/stdc++.h>

using namespace std;

void init() {
    cin.tie(nullptr);
    std::istream::sync_with_stdio(false);
    cout.tie(nullptr);
}
int n;
char arr[102][102],brr[102][102],crr[102][102];
void rotate() {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            crr[j][i]=arr[i][j];
        }
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            arr[n-i-1][j]=crr[i][j];
        }
    }
}
int com() {
    int ans=0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            ans+=(arr[i][j]!=brr[i][j]);
        }
    }
    return ans;
}

int main() {
    init();
   cin >> n ;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> arr[i][j];
        }
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> brr[i][j];
        }
    }
    int ans=1e9;
    for (int i = 0; i <=4; ++i) {
        ans=min(ans,com()+i);
        rotate();
    }
    cout << ans;
}