#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;
    
    long long total = 0;
    for(int i = 0; i < n; i++){
        long long a;
        cin >> a;
        total += a;
    }
    
    if(total % 2 == 1){
        cout << "Fennec" << endl;
    } else {
        cout << "Snuke" << endl;
    }
    
    return 0;
}