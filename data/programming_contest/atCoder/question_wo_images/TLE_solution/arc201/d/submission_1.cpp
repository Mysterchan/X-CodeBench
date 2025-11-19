#include<bits/stdc++.h>
using namespace std;
const int N=6e6+10;
int a[N],b[N];
int vt[N];
int cnt1[N],cnt2[N];
int s1[N],s2[N];
int t;
int n,m;
bool check(int mid)
{
    int p=1;
    memset(s1,0,sizeof(s1));
    int k=t/3*2;
    for(int i=1;i<=t;i++)
    {
        while(vt[i]-vt[p]>mid) p++;
        if(p>k) break;
        s1[p]+=cnt1[i];
    }
    int Max=-1e9;
    for(int i=1;i<=k;i++)
    {
        s1[i]+=s1[i-1];
        Max=max(Max,-cnt2[i-1]+s2[i]);
        if(cnt2[i]-s1[i]+Max>0) return 0;
    }
    return 1;
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0),cout.tie(0);
    int T;
    cin>>T;
    while(T--)
    {
        cin>>n>>m;
        for(int i=1;i<=n;i++) cin>>a[i];
        for(int i=1;i<=n;i++) cin>>b[i];
        for(int i=1;i<=n;i++) vt[i]=(m-a[i])%m,vt[i+n]=b[i];
        sort(vt+1,vt+1+2*n);
        t=unique(vt+1,vt+1+2*n)-vt-1;
        for(int i=1;i<=n;i++) 
        {
            cnt1[lower_bound(vt+1,vt+1+t,b[i])-vt]++;
            cnt2[lower_bound(vt+1,vt+1+t,(m-a[i])%m)-vt]++;
        }
        for(int i=1;i<=t;i++) 
        {
            vt[i+t]=vt[i]+m,cnt1[i+t]=cnt1[i],cnt2[i+t]=cnt2[i];
            vt[i+2*t]=vt[i]+2*m,cnt1[i+2*t]=cnt1[i];
        }
        t*=3;
        for(int i=1;i<=t;i++) 
        {
            cnt2[i]+=cnt2[i-1];
            s2[i]=s2[i-1]+cnt1[i-1];
        }
        int l=0,r=m-1,ans=m;
        while(l<=r)
        {
            int mid=(l+r)>>1;
            if(check(mid)) ans=mid,r=mid-1;
            else l=mid+1;
        }
        cout<<ans<<'\n';
        for(int i=0;i<=t;i++) cnt1[i]=cnt2[i]=s1[i]=s2[i]=0;
    }
    return 0;
}