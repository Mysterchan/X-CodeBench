#pragma GCC optimize(3)
#include<bits/stdc++.h>
#define rep(i,a,b) for(int i=a;i<=b;++i)
#define per(i,a,b) for(int i=a;i>=b;--i)
#define pii pair<int,int>
#define pb push_back
#define is insert
#define es erase
#define fi first
#define se second

using namespace std;
typedef long long ll;

const int N=2e5+10;
const int p=998244353;
int n,t;
int a[N],pos[N],c[N];
int cnt=0;
int ch[N][2],pri[N];
int sz[N];
int key[N];

mt19937 rng(time(0));

int newnode(int k){
    ++cnt;
    ch[cnt][0]=ch[cnt][1]=0;
    pri[cnt]=rng();
    sz[cnt]=1;
    key[cnt]=k;
    return cnt;
}

void pu(int x){
    if(!x)
        return ;
    sz[x]=sz[ch[x][0]]+sz[ch[x][1]]+1;
}

void split(int rt,int k,int &rt1,int &rt2){
    if(!rt){
        rt1=rt2=0;
        return ;
    }
    if(sz[ch[rt][0]]>=k){
        rt2=rt;
        split(ch[rt][0],k,rt1,ch[rt2][0]);
        pu(rt);
    }
    else{
        rt1=rt;
        split(ch[rt][1],k-sz[ch[rt][0]]-1,ch[rt1][1],rt2);
        pu(rt);
    }
}

int mg(int rt1,int rt2){
    if(!rt1||!rt2)
        return rt1|rt2;
    if(pri[rt1]<pri[rt2]){
        ch[rt1][1]=mg(ch[rt1][1],rt2);
        pu(rt1);
        return rt1;
    }
    ch[rt2][0]=mg(rt1,ch[rt2][0]);
    pu(rt2);
    return rt2;
}

int qu1(int rt,int k){
    if(!rt)
        return 0;
    int tmp=qu1(ch[rt][1],k);
    if(sz[ch[rt][1]]==tmp&&key[rt]==k){
        return qu1(ch[rt][0],k)+1+tmp;
    }
    return tmp;
}

int qu2(int rt,int k){
    if(!rt)
        return 0;
    int tmp=qu2(ch[rt][0],k);
    if(sz[ch[rt][0]]==tmp&&key[rt]==k){
        return qu2(ch[rt][1],k)+1+tmp;
    }
    return tmp;
}

int s[N];

void up(int x,int k){
    for(int i=x;i<=n;i+=i&(-i))
        s[i]+=k;
}

int qu(int x){
    int ss=0;
    for(int i=x;i;i-=i&(-i))
        ss+=s[i];
    return ss;
}

int main(){
    scanf("%d",&t);
    while(t--){
        cnt=0;
        scanf("%d",&n);
        int rt=0;
        rep(i,1,n)
            scanf("%d",&a[i]),s[i]=0;
        rep(i,1,n)
            scanf("%d",&c[i]);
        rep(i,1,n){
            pos[a[i]]=i;
            rt=mg(rt,newnode(c[i]));
        }
        ll ans=1;
        rep(i,1,n){
            int x,y,z;
            int ps=pos[i]-qu(pos[i]);
            split(rt,ps,x,z);
            split(x,ps-1,x,y);
            int tmp1=qu1(x,c[pos[i]]);
            int tmp2=qu2(z,c[pos[i]]);
            ans=ans*(tmp1+tmp2+1)%p;
            rt=mg(x,z);
            up(pos[i],1);
        }
        printf("%lld\n",ans);
    }
}
