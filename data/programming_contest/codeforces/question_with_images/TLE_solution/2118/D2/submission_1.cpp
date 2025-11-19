#include<bits/stdc++.h>
using namespace std;
#define int long long
signed main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int n,k;
		cin>>n>>k;
		vector<int> p(n+1),d(n+1);
		for(int i=1;i<=n;i++)  cin>>p[i];
		for(int i=1;i<=n;i++)  cin>>d[i];
		int q;
		cin>>q;
		for(int i=1;i<=q;i++)
		{
			int x;
			cin>>x;
			int flag=1;
		    int t=0;
		    bool ok=false;
		    set<tuple<bool,int,int>>vis;
		    int cur=0;
		    while(true)
		    {
		    	if(flag)  cur=lower_bound(p.begin()+1,p.end(),x)-p.begin();
		    	else  cur=upper_bound(p.begin()+1,p.end(),x)-p.begin()-1;
		    	if(cur<1||cur>n){ok=true;break;}
		    	t+=abs(x-p[cur]);
		    	auto state=make_tuple(flag,cur,t%k);
		    	if(vis.count(state))  {break;}
		    	vis.insert(state);
		    	int de=d[cur];
		    	if(t%k==de) flag^=1;
		    	if(flag)  x=p[cur]+1;
		    	else  x=p[cur]-1;
		    	t++;
		    }
		    cout << (ok?"YES":"NO") << '\n';
		}

	}
}
