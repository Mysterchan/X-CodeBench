#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;
    int n = s.size(), ans = 0;
    for(int i = 0; i < n; i++){
        if(s[i] != 'A') continue;
        for(int j = i + 1; j < n; j++){
            if(s[j] != 'B') continue;
            int k = 2 * j - i;
            if(k < n && s[k] == 'C') ans++;
        }
    }
    cout << ans;
    return 0;
}