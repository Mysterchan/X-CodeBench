#include<bits/stdc++.h>
using namespace std;
#define int long long
typedef pair<int,int> PII;
typedef pair<double,double> PDD;
const int N=2e3+5;

int n;
int a[N],b[N];
map<double,int>mp;
map<PDD,int>cnt;
int ans,p;

signed main(){  
    ios::sync_with_stdio(0);
    
    cin>>n;

    for(int i=1;i<=n;i++)
        cin>>a[i]>>b[i];

    for(int i=1;i<=n;i++)
        for(int j=i+1;j<=n;j++){
            double x=(a[i]*1.0+a[j])/2,y=(b[i]*1.0+b[j])/2;
            PDD mid={x,y};
            cnt[mid]++;
            p+=cnt[mid]-1;

            if(a[i]==a[j]) {mp[2e9]++;continue;}

            double k=(b[i]-b[j])*1.0/(a[i]-a[j]);
            mp[k]++;
        }
    
    for(auto i:mp) 
        ans+=i.second*(i.second-1)/2;

    cout<<ans-p;
    
    return 0;
}