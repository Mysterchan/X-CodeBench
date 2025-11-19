#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    long long sum = 0;
    bool hasEven = false, hasOdd = false;
    for(int i = 1; i <= n; i++){
        int x;
        cin >> x;
        if(x){
            sum++;
            if(i % 2 == 0) hasEven = true;
            else hasOdd = true;
        }
    }

    int r = n % 4;
    bool ok = false;
    if(r == 0){
        ok = true;
    } else if(r == 1 || r == 3){
        if(sum > 0) ok = true;
    } else { // r == 2
        if(hasEven && hasOdd) ok = true;
    }

    cout << (ok ? "Yes\n" : "No\n");
    return 0;
}