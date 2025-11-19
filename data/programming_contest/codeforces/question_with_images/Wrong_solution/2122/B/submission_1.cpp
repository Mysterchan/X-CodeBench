#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin >> t;
    while( t-- ){
        int n;
        cin >> n;
        int cnt = 0;
        int zero  = 0, zero_ch = 0;
        for( int i =0; i<n; i++){
            int a, b, c, d;
            cin >> a >> b >> c >> d;
            if( d < b){
                cnt += a + b-d;
            }
            else if( c<a){
                cnt += a -c;
            }
        }
        cout<< cnt <<endl;
    }
}