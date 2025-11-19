#include<bits/stdc++.h>
#define ll long long
using namespace std;
const int maxn=3e5+9;
ll a[maxn],f[maxn],lst[maxn];
int main()
{
	int n;
	cin>>n;
	ll ans=0;
	for(int i=1;i<=n;i++)
	{
		cin>>a[i];
		f[i]=f[i-1]+i-lst[a[i]];
		if(lst[a[i]+1]>lst[a[i]])f[i]-=lst[a[i]+1]-lst[a[i]];
		if(lst[a[i]-1]>lst[a[i]])f[i]-=lst[a[i]-1]-lst[a[i]];
		lst[a[i]]=i;
		ans+=f[i];
	}
	cout<<ans;
	return 0;
}

