#include <bits/stdc++.h>
using namespace std;


int a[500010];
int l,r;
bool vis[500010];
int main()
{
    ios::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    int n;
    cin>>n;
    long long ans=0;
    for(int i=1;i<=n;i++){
        cin>>a[i];
        
    }
    l=1,r=2;
    while(r<=n){
        if(l==r){
            r++;
        }
        if(vis[l]){
            continue;
        }
        if(a[r]>=(a[l]*2)){
            ans++;
            r++,l++;
            vis[r]=true;
        }else{
            r++;
        }
    }
    cout<<ans;
    return 0;
    
}


