#include <bits/stdc++.h>
using namespace std;
using ll=long long;
const int S=1000005;
int a[S],c[S];
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; if(!(cin>>n)) return 0;
    for(int i=1;i<=n;i++) cin>>a[i];
    ll s=0;
    for(int i=n;i>=1;i--){
        int occ=c[a[i]];
        if(i==n||a[i]!=a[i+1]) s+= (ll)(n-i)-occ;
        c[a[i]]++;
    }
    cout<<s+1<<"\n";
    return 0;
}
