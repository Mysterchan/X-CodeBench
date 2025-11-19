#include<bits/stdc++.h>
using namespace std;
typedef unsigned long long ll;
const ll k=114514;
const ll maxn=5e3+10;
ll n,ans,h[maxn],jc[maxn],inv[maxn],mod=998244353;
vector<ll> e[maxn];
stack<ll> s;
unordered_map<ll,ll> mp;
ll js(ll x){
  x^=k;
  x^=x<<13;
  x^=x>>7;
  x^=x<<17;
  x^=k;
  return x;
}
ll ksm(ll x,ll k){
	ll res=1;
	while(k){
		if(k&1) res=res*x%mod;
		x=x*x%mod;
		k>>=1;
	}
	return res;
}
void dfs(ll u){
	h[u]=1;
	for(auto v:e[u]){
		dfs(v);
		h[u]+=js(h[v]);
	}
	mp.clear();
	for(auto v:e[u]){
		mp[h[v]]++;
	}
	ans=ans*jc[e[u].size()]%mod;
	for(auto i:mp){
		ans=ans*inv[i.second]%mod;
	}
}
int main(){
	#ifdef ONLINE_JUDGE
	ios::sync_with_stdio(0);
	#endif
	cin.tie(0);
	cout.tie(0);
	cin>>n;
	s.push(0);
	for(ll i=1;i<=n;i++){
		char x;
		cin>>x;
		if(x=='(') e[s.top()].emplace_back(i),s.push(i);
		else s.pop();
	}
	ans=1;
	jc[0]=1;
	for(ll i=1;i<=n;i++){
		jc[i]=jc[i-1]*i%mod;
	}
	inv[n]=ksm(jc[n],mod-2);
	for(ll i=n;i>=1;i--){
		inv[i-1]=inv[i]*i%mod;
	}
	dfs(0);
	cout<<ans<<"\n";
	return 0;
}
