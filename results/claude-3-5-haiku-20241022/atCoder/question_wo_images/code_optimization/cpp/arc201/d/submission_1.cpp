#include<bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0),cout.tie(0);
    int T;
    cin>>T;
    while(T--)
    {
        int n,m;
        cin>>n>>m;
        vector<int> a(n),b(n);
        for(int i=0;i<n;i++) cin>>a[i];
        for(int i=0;i<n;i++) cin>>b[i];
        
        vector<int> vt;
        vt.reserve(2*n);
        for(int i=0;i<n;i++) {
            vt.push_back((m-a[i])%m);
            vt.push_back(b[i]);
        }
        sort(vt.begin(),vt.end());
        vt.erase(unique(vt.begin(),vt.end()),vt.end());
        
        int t=vt.size();
        vector<int> cnt1(3*t),cnt2(3*t);
        
        for(int i=0;i<n;i++) 
        {
            int pos=lower_bound(vt.begin(),vt.end(),b[i])-vt.begin();
            cnt1[pos]++;
            pos=lower_bound(vt.begin(),vt.end(),(m-a[i])%m)-vt.begin();
            cnt2[pos]++;
        }
        
        for(int i=0;i<t;i++) 
        {
            vt.push_back(vt[i]+m);
            cnt1[i+t]=cnt1[i];
            cnt2[i+t]=cnt2[i];
            vt.push_back(vt[i]+2*m);
            cnt1[i+2*t]=cnt1[i];
        }
        t*=3;
        
        vector<int> s2(t);
        for(int i=1;i<t;i++) 
        {
            cnt2[i]+=cnt2[i-1];
            s2[i]=s2[i-1]+cnt1[i-1];
        }
        
        auto check = [&](int mid) -> bool {
            int p=0;
            vector<int> s1(t);
            int k=t/3*2;
            for(int i=0;i<t;i++)
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
                if(cnt2[i]-s1[i]+Max>0) return false;
            }
            return true;
        };
        
        int l=0,r=m-1,ans=m;
        while(l<=r)
        {
            int mid=(l+r)>>1;
            if(check(mid)) ans=mid,r=mid-1;
            else l=mid+1;
        }
        cout<<ans<<'\n';
    }
    return 0;
}