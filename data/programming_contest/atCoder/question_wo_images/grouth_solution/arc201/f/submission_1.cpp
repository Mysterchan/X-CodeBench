#include<cstdio>
#define ll long long
ll read(){
    ll num=0;
    char ch;ch=getchar();
    while(ch<48||ch>57)ch=getchar();
    while(ch>47&&ch<58){
        num=(num<<1)+(num<<3)+(ch^48);
        ch=getchar();
    }return num;
}
ll min(ll x,ll y){return x<y?x:y;}
int n,m;
ll s1,s2,s3,s4,s5,s6,s7,ans;
void work(){
    s1=s2=s3=s4=s5=s6=s7=0;
    n=read();
    for(int i=1;i<=n;i++){
        ll a=read(),b=read(),c=read(),d=read(),e=read();
        s1+=min(min(a,b),c);
        s2+=min(min(b,c),d);
        s3+=min(min(c,d),e);
        s4+=min(min(b,c),a+d);
        s5+=min(min(c,d),b+e);
        s6+=min(c,min(a,b)+min(d,e));
        s7+=min(min(c,b+e),min(a,b)+d);
        ans=s7/3;
        ans=min(ans,s1);
        ans=min(ans,s2);
        ans=min(ans,s3);
        ans=min(ans,s4/2);
        ans=min(ans,s5/2);
        ans=min(ans,s6/2);
        printf("%lld ",ans);
    }printf("\n");
}
int main(){
    int Case=read();
    while(Case--)work();
}