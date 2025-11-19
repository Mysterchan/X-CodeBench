#include <algorithm>
#include <cstring>
#include <vector>
#include <cstdio>
const int MX=500005;
int n,fa[MX],fir[MX],f[MX];
struct Edge{int to,nxt;}e[MX];
void add(int a,int b,int pos){
	e[pos]=(Edge){b,fir[a]};fir[a]=pos;
}
void dfs(int x){
	int cnt=0;
	std::vector<int>heap;heap.clear();
	for(int i=fir[x];i;i=e[i].nxt){
		int h=e[i].to;dfs(h);heap.push_back(f[h]);cnt++;
	}
	std::make_heap(heap.begin(),heap.end());
	for(int i=1;i<cnt;i++){
		int x=heap[0];std::pop_heap(heap.begin(),heap.end());heap.pop_back();
		int y=heap[0];std::pop_heap(heap.begin(),heap.end());heap.pop_back();
		heap.push_back(x-y);std::push_heap(heap.begin(),heap.end());
	}
	f[x]=(cnt?heap[0]:0)+1;
}
void solve(){
	scanf("%d",&n);
	for(int i=1;i<=n;i++)fir[i]=f[i]=0;
	for(int i=2;i<=n;i++)scanf("%d",&fa[i]);
	for(int i=2;i<=n;i++)add(fa[i],i,i-1);
	dfs(1);printf("%d\n",(n-f[1])>>1);
}
int main(){
	int data;scanf("%d",&data);
	for(int i=1;i<=data;i++)solve();
	return 0;
}