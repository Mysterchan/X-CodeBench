#include<bits/stdc++.h>
using namespace std;

#define sz(x) (int)(x).size()
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define pb push_back
#define x first
#define y second
#define F first
#define S second
#define FOR(i,a,b) for(int i = (a); i < (b); ++i)
#define RFOR(i,a,b) for(int i = (a) - 1; i >= (b); --i)

typedef long long ll;
typedef double db;
typedef long double LD;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<db, db> pdd;
typedef vector<int> VI;
typedef vector<ll> VL;
const int MAX_N=5010;

ll cost[MAX_N][MAX_N];
int solve()
{
	int n, m;
	if (!(cin >> n >> m))
		return 1;
	vector<vector<int>> adj(n);
	vector<ll> W(n);
	FOR(i,0,n) cin >> W[i];
	FOR(_,0,m)
	{
		int u, v;
		cin >> u >> v;
		--u, --v;
		adj[u].pb(v);
		adj[v].pb(u);
	}
	const ll INF=1e18;
	FOR(i,0,MAX_N)
		FOR(j,0,MAX_N) cost[i][j]=INF;
	priority_queue<tuple<ll,int,int>, vector<tuple<ll,int,int>>, greater<>> pq;

	FOR(i,0,n)
	{
		cost[0][i] = W[0]*i;
		pq.push({0, i, 0});
	}
	while(!pq.empty())
	{
		auto [dist, k, v] = pq.top();
		pq.pop();
		if(dist > cost[v][k] || k == 0) continue;
		for(auto to: adj[v])
		{
			const auto cto=cost[v][k] + W[to]*(k-1);
			if(cost[to][k-1] > cto)
			{
				cost[to][k-1]=cto;
				pq.push({cto, k-1, to});
			}
		}
	}
	FOR(i,0,n)
	{
		ll res=1e18;
		FOR(j,0,n)res=min(res, cost[i][j]);
		cout<<res<<"\n";
	}
	return 0;
}

int32_t main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	int TET = 1e9;
	for (int i = 1; i <= TET; ++i)
	{
		if (solve())
			break;
		#ifdef ONPC
			cerr << "_________________________\n";
		#endif
	}
	#ifdef ONPC
		cerr << "\nfinished in " << clock() * 1. / CLOCKS_PER_SEC << " sec\n";
	#endif
	return 0;
}
