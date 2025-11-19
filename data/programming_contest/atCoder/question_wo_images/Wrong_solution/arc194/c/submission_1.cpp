#include <bits/stdc++.h>
using namespace std;
#define int long long
#define LL long long
#define ULL unsigned long long
#define DB double
#define LD long double
#define PII pair<int,int>
#define PLL pair<long long,long long>
#define fr first
#define sc second
#define popcnt __builtin_popcount
const int N=2e5+10,M=22;
const LL P=1e9+9;
int n,a[N],b[N],c[N]; LL sa[N],sb[N];
vector<int> p[3];
bool cmp_ls(int x,int y) {return x<y;}
bool cmp_gr(int x,int y) {return x>y;}
int work() {
    cin>>n;
    for (int i=1;i<=n;i++) cin>>a[i];
    for (int i=1;i<=n;i++) cin>>b[i];
    for (int i=1;i<=n;i++) cin>>c[i];
    for (int i=1;i<=n;i++) {
        if (!a[i]&&b[i]) p[0].push_back(c[i]);
        else if (a[i]&&!b[i]) p[1].push_back(c[i]);
        else if (a[i]&&b[i]) p[2].push_back(c[i]);
    }
    sort(p[0].begin(),p[0].end(),cmp_gr);
    sort(p[1].begin(),p[1].end(),cmp_gr);
    sort(p[2].begin(),p[2].end(),cmp_gr);
    LL sum=0;
    if (p[0].size()) sa[0]=p[0][0];
    for (int i=0;i<p[0].size();i++) {
        sum+=(LL)(i+1)*p[0][i];
        if (i) sa[i]=sa[i-1]+p[0][i];
    }
    if (p[1].size()) sb[0]=p[1][0];
    for (int i=0;i<p[1].size();i++) {
        sum+=(LL)i*p[1][i];
        if (i) sb[i]=sb[i-1]+p[1][i];
    }
    int t,cnt=0;
    for (t=0;t<p[2].size();t++) {
        LL res1=(LL)p[2][t]*(p[0].size()+p[1].size()+cnt*2);
        int pa=upper_bound(p[0].begin(),p[0].end(),p[2][t],cmp_gr)-p[0].begin();
        int pb=upper_bound(p[1].begin(),p[1].end(),p[2][t],cmp_gr)-p[1].begin();
        LL res2=(LL)p[2][t]*(pa+1+pb+cnt*2)+sa[p[0].size()-1]+sb[p[1].size()-1];
        if (pa) res2-=sa[pa-1];
        if (pb) res2-=sb[pb-1];
        if (res2<res1) {
            sum+=res2; cnt++;
        } else sum+=res1;
    }
    cout<<sum<<'\n';
    return 0;
}
signed main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int T=1;
    while (T--) { work(); }
    return 0;
}