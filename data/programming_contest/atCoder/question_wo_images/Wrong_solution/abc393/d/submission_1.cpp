#include<bits/stdc++.h>
#define ll long long
using namespace std;
const ll N=1e6+10;
string st;
vector<ll> V;
ll n;
int main()
{
	freopen("gather.in","r",stdin);
	freopen("gather.out","w",stdout);
    ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	cin>>n>>st; 
	ll ls=0,rs=0,ans=0x3f3f3f3f3f3f3f3f;
	for(int i=1;i<=n;i++)
		if(st[i-1]=='1')
			V.push_back(i),rs+=i;
	for(int i=0;i<V.size();i++)
	{
		ll v=V[i],l=i,r=V.size()-i-1; 
		rs-=v;
		ans=min(ans,rs-ls+l*v-r*v-(l+l*l+r+r*r)/2);
		ls+=v;
	}
	cout<<ans;
    return 0;
}