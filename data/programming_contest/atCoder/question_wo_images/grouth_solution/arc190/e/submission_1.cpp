#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
const ll N=2e5+3,K=5,INF=1e18;
ll n,m,a[N],sa[N];
void Max(ll &x,ll y){if(x<y)x=y;}
struct Mat
{
	array<ll,K>f[K];
	auto& operator[](int x){return f[x];}
	void Clear(){memset(f,0xcf,sizeof(f));}
	friend Mat operator *(Mat A,Mat B)
	{
		Mat C;C.Clear();
		for(int i=0;i<K;i++)for(int k=0;k<K;k++)for(int j=0;j<K;j++)
			Max(C[i][j],A[i][k]+B[k][j]);
		return C;
	}
}I;
void Init(){for(int i=0;i<K;i++)for(int j=0;j<K;j++)I[i][j]=i==j?0:-INF;}
Mat Get(ll v)
{
	Mat A;
	if(v%2==0)
	{
		A[0]={-INF,-v,-INF,-INF,-INF};
		A[1]={-INF,-v,v,0,-INF};
		A[2]={-v,-INF,-INF,-INF,-INF};
		A[3]={-v,-INF,-INF,0,-INF};
		A[4]={-v,-INF,-INF,-INF,0};
	}
	else
	{
		A[0]={-INF,-v,-INF,-INF,-INF};
		A[1]={-INF,-v,v,-INF,1};
		A[2]={-v,-INF,-INF,-INF,-INF};
		A[3]={-v,-INF,-INF,-INF,1};
		A[4]={-v,-INF,-INF,-1,-INF};
	}
	return A;
}
struct SGT
{
	int DT;Mat tr[1<<19|3];
	void Up(int p){tr[p]=tr[p<<1]*tr[p<<1|1];}
	void Build()
	{
		DT=1<<(__lg(n)+1);
		for(int i=1;i<=n;i++)tr[i+DT]=Get(a[i]);
		for(int i=DT-1;i;i--)Up(i);
	}
	Mat Ask(int l,int r)
	{
		Mat sl=I,sr=I;
		for(l+=DT-1,r+=DT+1;l+1!=r;l>>=1,r>>=1)
		{
			if(~l&1)sl=sl*tr[l+1];
			if(r&1)sr=tr[r-1]*sr;
		}
		return sl*sr;
	}
}T;
int main()
{
	ios::sync_with_stdio(0),cin.tie(0),cout.tie(0);
	cin>>n>>m;Init(); 
	for(int i=1;i<=n;i++)cin>>a[i],sa[i]=sa[i-1]+a[i];
	T.Build();
	for(int i=1,l,r;i<=m;i++)
	{
		cin>>l>>r;Mat t=T.Ask(l,r);
		ll ans=*max_element(t[1].begin(),t[1].end());
		cout<<(sa[r]-sa[l-1]-ans)/2<<"\n";
	}
}
