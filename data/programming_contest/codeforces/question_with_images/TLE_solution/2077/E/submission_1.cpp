#pragma GCC target("avx2")
#pragma GCC optimize("O3")
#include <bits/stdc++.h>
using namespace std;
const int mod = 998244353;
int A[200100];
int main(){
    int TT;
    cin>>TT;
    while(TT--){
        int N;
        cin>>N;
        for(int i=0;i<N;i++) cin>>A[i];
        long long ans = 0;
        for(int i=0;i<N;i++){
            long long a = 0, b = 0;
            for(int j=i;j<N;j++){
                if(j&1){
                    a += A[j];
                    b -= A[j];
                    if(b < 0) b = 0;
                }
                else{
                    a -= A[j];
                    b += A[j];
                    if(a < 0) a = 0;
                }
                ans += (a+b)%mod;
            }
            ans %= mod;
        }
        cout<<ans<<endl;
    }
}
