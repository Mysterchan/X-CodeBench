#include<bits/stdc++.h>
using namespace std;
constexpr int MN=2e5+15;
int n,a[MN],q,ans,cnt1;


int calc(int i){
    if (i < 1 || i > n)
    {
        return 0;
    }
    if (a[i] == 1)
    {
        return a[i - 1] == 1;
    }
    else
    {
        if (a[i - 1] == 0 && a[i + 1] == 0)
        {
            return 1;
        }
        if (a[i - 1] == 1 && a[i + 1] == 1)
        {
            return 2;
        }
    }
    return 0;
}

int main(){
    cin>>n;
    a[0]=a[n+1]=114514;
    for(int i=1;i<=n;i++){
        cin>>a[i];
        cnt1+=a[i]==1;
    }
    ans=n;
    for(int i=1;i<=n;i++){
        ans-=calc(i);
    }
    cin>>q;
    while(q--){
        int x;
        cin>>x;
        ans+=calc(x-1)+calc(x)+calc(x+1);
        cnt1-=a[x];
        a[x]^=1;
        ans-=calc(x-1)+calc(x)+calc(x+1);
        cnt1+=a[x];
        if(cnt1==n){
            cout<<n<<'\n';
        }
        else cout<<max(2,ans)<<'\n';
    }

    return 0;
}