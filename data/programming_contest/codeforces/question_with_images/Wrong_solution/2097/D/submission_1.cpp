#include<bits/stdc++.h>
#define ll long long
#define ull unsigned long long
using namespace std;
#define N 1000005
char s[N],t[N];
int n;
int id[N];
struct bi{
	vector<ull>a;
	void reset(){for(int i=0;i<a.size();++i)a[i]=0;}
	void add(int p){a[p>>6]|=(1ull<<(p&63));}
	int chk(int p){return ((a[p>>6]&(1ull<<(p&63))));}
}f[N],g[N];
bool chk(){
	int l=n;
	while(l%2==0)l>>=1;
	int c=(l+63)/64;
	for(int i=0;i<l;++i)id[i]=-1;
	for(int i=0;i<n;i+=l){
		f[i/l].a.resize(c+1);
		f[i/l].reset();
		for(int j=i;j<i+l;++j)if(s[j]=='1')f[i/l].add(j-i);
		for(int j=0;j<l;++j){
			if(!f[i/l].chk(j))continue;
			if(id[j]==-1){
				id[j]=i/l;
				break;
			}
			for(int k=0;k<=c;++k)f[i/l].a[k]^=f[id[j]].a[k];
		}
	}
	for(int i=0;i<n;i+=l){
		g[i/l].a.resize(c+1);
		g[i/l].reset();
		for(int j=i;j<i+l;++j)if(t[j]=='1')g[i/l].add(j-i);
		for(int j=0;j<l;++j){
			if(!g[i/l].chk(j))continue;
			if(id[j]==-1)return 0;
			for(int k=0;k<=c;++k)g[i/l].a[k]^=f[id[j]].a[k];
		}
	}
	return 1;
}
void slv(){
	scanf("%d%s%s",&n,s,t);
	if(!chk()){
		puts("No");
		return;
	}
	for(int i=0;i<n;++i)swap(s[i],t[i]);
	if(!chk()){
		puts("No");
		return;
	}
	puts("Yes");
}
int main(){
	int t;cin>>t;
	while(t--)slv();
	return 0;
}