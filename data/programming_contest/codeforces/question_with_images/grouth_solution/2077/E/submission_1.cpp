#include <bits/stdc++.h>

using namespace std;
#define int long long
const int p=998244353;
int po(int a,int b) {if(b==0) return 1; if(b==1) return a; if(b%2==0) {int u=po(a,b/2);return (u*1LL*u)%p;} else {int u=po(a,b-1);return (a*1LL*u)%p;}}
int inv(int x) {return po(x,p-2);}
mt19937 rnd;
#define app push_back
#define all(x) (x).begin(),(x).end()
#ifdef LOCAL
#define debug(...) [](auto...a){ ((cout << a << ' '), ...) << endl;}(#__VA_ARGS__, ":", __VA_ARGS__)
#define debugv(v) do {cout<< #v <<" : {"; for(int izxc=0;izxc<v.size();++izxc) {cout << v[izxc];if(izxc+1!=v.size()) cout << ","; }cout <<"}"<< endl;} while(0)
#else
#define debug(...)
#define debugv(v)
#endif
#define lob(a,x) lower_bound(all(a),x)
#define upb(a,x) upper_bound(all(a),x)
const int maxn=2e5+5;
int n;int sz;
int fe[maxn];int arr[maxn];
void pl(int pos) {while(pos<sz) {fe[pos]++;pos|=(pos+1);}}
int get(int pos) {int ans=0;while(pos>=0) {ans+=fe[pos];pos&=(pos+1);--pos;} return ans;}
int get2(int pos) {return get(pos)-pos;}
int calc(int pos)
{
    if(!arr[pos])
    {
        int l1=pos;int l2=pos;
        for(int i=19;i>=0;--i)
        {
            if(l1-(1<<i)>=0 && get(l1-(1<<i))==get(pos))
            {
                l1-=(1<<i);
            }
            if(l2+(1<<i)<=n && get(l2+(1<<i))==get(pos))
            {
                l2+=(1<<i);
            }
        }
        if(arr[l1]==arr[pos]) {--l1;}
        return (pos-l1)*(l2+1-pos);
    }
    else
    {
        int l1=pos;int l2=pos;
        for(int i=19;i>=0;--i)
        {
            if(l1-(1<<i)>=0 && get2(l1-(1<<i))==get2(pos))
            {
                l1-=(1<<i);
            }
            if(l2+(1<<i)<=n && get2(l2+(1<<i))==get2(pos))
            {
                l2+=(1<<i);
            }
        }
        if(arr[l1]==arr[pos]) {--l1;}
        return (pos-l1)*(l2+1-pos);
    }
}
int32_t main()
{
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    int t;cin>>t;
    while(t--)
    {
        cin>>n;vector<int> a(n);for(int i=0;i<n;++i) {cin>>a[i];}
        sz=n+2;fill(fe,fe+sz,0);fill(arr,arr+sz,0);
        vector<int> b(n+1);for(int i=0;i<n;++i) {if(i%2==0) {b[i+1]=b[i]+a[i];} else {b[i+1]=b[i]-a[i];}}
        map<int,vector<int> > mem;
        for(int i=0;i<=n;++i) {mem[b[i]].app(i);}
        vector<int> c=b;sort(all(c));c.erase(unique(all(c)),c.end());
        int cur=(n+1)*(n+2)/2;int res=0;
        for(int i=0;i<c.size()-1;++i)
        {
            int we=c[i+1]-c[i];
            for(int j:mem[c[i]])
            {
                cur-=calc(j);arr[j]=1;pl(j);cur+=calc(j);
            }
            debug(we,cur);
            res+=we*((((n+1)*(n+2)/2)-cur)%p);res%=p;
        }
        cout<<(res%p+p)%p<<'\n';
    }
    return 0;
}
