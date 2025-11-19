#include<bits/stdc++.h>
typedef long long ll;
#define pii pair<int,int>
#define fi first
#define se second
#define vec vector<int>
#define eb emplace_back
using namespace std;
int read(){
	int x=0,y=1;
	char ch=getchar();
	while(ch<48||ch>57){if(ch==45)y=-1;ch=getchar();}
	while(ch>=48&&ch<=57)x=(x<<3)+(x<<1)+(ch^48),ch=getchar();
	return x*y;
}
const int maxn=2e5+5;
int a[maxn];
int st[maxn];
int main(){
    int T;
    T=read();
    while(T--){
        int n;
        n=read();
        for(int i=1;i<=n;i++)a[i]=read();
        int tp=0;
        ll ans=0;
        for(int i=1;i<=n;i++){
            vec v(0);
            while(tp&&st[tp]<=a[i])v.eb(st[tp--]);
            if(v.size()){
                if(v.size()>1)ans+=v.back()-v[0]-(v.size()-2);
                int w=v.back()+(v.size()>1);
                if(w<=a[i]){
                    ans+=a[i]-w;
                    w=a[i]+1;
                    while(tp&&st[tp]==w)w++,tp--;
                    st[++tp]=w;
                }
                else st[++tp]=w,st[++tp]=a[i];
            }
            else st[++tp]=a[i];
        }
        if(tp>1)ans+=st[1]-st[tp]-(tp-2);
        printf("%lld\n",ans);
    }
    return 0;
}