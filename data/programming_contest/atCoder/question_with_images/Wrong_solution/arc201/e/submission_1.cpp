#include<bits/stdc++.h>
#define I inline
#define lson (k<<1)
#define rson (k<<1|1)
#define mid ((l+r)>>1)
#define int long long
using namespace std;

const int mod = 998244353;
const int N = 200010;
struct node {
    int x,y;
}a[N];
struct Segnode {
    int sum,tg;
}tr[N<<1];

int n;
int pw[N];

I void acc(int k,int v) {
    tr[k].tg+=v;
    tr[k].sum=tr[k].sum*pw[v]%mod;
}
I void pushdown(int k) {
    if(tr[k].tg) {
        acc(lson,tr[k].tg);
        acc(rson,tr[k].tg);
    }
    tr[k].tg=0;
}
I void update(int k) {
    tr[k].sum=(tr[lson].sum+tr[rson].sum)%mod;
}
I void change(int l,int r,int nl,int nr,int k) {
    if(l>=nl&&r<=nr) return acc(k,1),void();
    pushdown(k);
    if(nl<=mid) change(l,mid,nl,nr,lson);
    if(nr>mid) change(mid+1,r,nl,nr,rson);
    update(k);
}
void build(int l,int r,int k) {
    tr[k].tg=tr[k].sum=0;
    if(l==r) {
        tr[k].sum=1;
        return ;
    }
    build(l,mid,lson);
    build(mid+1,r,rson);
    update(k);
}
I void add(int &x,int y) {
    x+=y;
    x=(x>=mod?x-mod:x);
}
I void red(int &x,int y) {
    x=(x-y+mod)%mod;
}
I void shift(int sx,int sy) {
    if(sx) for(int i=1;i<=n;++i) a[i].x=n-a[i].x+1;
    if(sy) for(int i=1;i<=n;++i) a[i].y=n-a[i].y+1;
}

I void calc(int &ans) {
    for(int i=1;i<n;++i) red(ans,pw[i]*(n-1)%mod);
    vector<int> v;
    for(int i=1;i<=n;++i) v.push_back(a[i].y);
    sort(v.begin(),v.end());
    int tp=0;
    for(int i=1;i<n;++i) {
        while(tp<v.size()&&v[tp]==i) tp++;
        red(ans,pw[tp]*(n-1)%mod);
    }
}
I void calc2(int &ans) {
    auto cmp = [&] (node n1,node n2) {
        return n1.x<n2.x;
    };
    sort(a+1,a+1+n,cmp);

    build(1,n-1,1);

    for(int i=1;i<n;++i) {
        if(a[i].y!=n) change(1,n-1,a[i].y,n-1,1);
        add(ans,tr[1].sum);
    }

}
I void solve() {
    cin>>n;
    for(int i=1;i<=n;++i) cin>>a[i].y,a[i].x=i;

    int ans=(n-1)*(n-1)%mod*pw[n]%mod;

    calc(ans); shift(0,1); calc(ans); shift(0,1);


    shift(0,0); calc2(ans); shift(0,0);
    shift(0,1); calc2(ans); shift(0,1);
    shift(1,1); calc2(ans); shift(1,1);
    shift(1,0); calc2(ans); shift(1,0);
    cout<<(ans+mod-(n-1)*(n-1)%mod)%mod<<endl;
}
signed main()
{
    {
        pw[0]=1;
        for(int i=1;i<=200000;++i) pw[i]=pw[i-1]*2%mod;
    }
    int T=1;
    while(T--) {
        solve();
    }
}