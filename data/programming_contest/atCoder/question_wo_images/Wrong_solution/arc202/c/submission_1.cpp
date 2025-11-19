#include <bits/stdc++.h>
using namespace std;

long long n,a[200001],r[200001],gcdd=1,mod=998244353,cur=1;



long long power(long long x,long long t){
    long long u=t,an=1;
    for(long long i=x;u>0;i=(i*i)%mod,u/=2){
        if(u%2) an=(an*i)%mod;
    }
    return an;
}

long long divide(long long x){
    return power(x,mod-2);
}

int main(){
    cin>>n;
    for(int i=1;i<=n;i++) cin>>a[i];
    for(int i=1;i<=200000;i++){
        r[i]=(r[i-1]*10+1)%mod;
    }
    for(int i=1;i<=n;i++){
        if(i>1) gcdd=__gcd(gcdd,a[i]);
        else gcdd=a[i];
        cur=(cur*r[a[i]])%mod;
        cout<<(cur*divide(power(r[gcdd],i-1)))%mod<<"\n";
    }
}
