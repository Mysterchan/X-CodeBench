#include<bits/stdc++.h>
using namespace std;
int read(){
	int x=0,f=1;
	char ch=getchar();
	while(ch<'0'||ch>'9'){
		if(ch=='-')
			f=-1;
		ch=getchar();
	}
	while(ch>='0'&&ch<='9'){
		x=x*10+ch-'0';
		ch=getchar();
	}
	return x*f;
}
void write(int x){
	if(x<0) putchar('-'),x=-x;
	if(x>9) write(x/10);
	putchar(x%10+'0');
	return;
}
const int N=1e6+10;
int n,m;
int root[N*32];
struct tree{
	
	int ls[N*32],rs[N*32],sum[N*32],tot;
	void change(int &u,int v,int l,int r,int p,int k){
		u=++tot;
		ls[u]=ls[v];rs[u]=rs[v];sum[u]=sum[v]+k;
		if(l==r) return;
		int mid=l+r>>1;
		if(p<=mid) change(ls[u],ls[v],l,mid,p,k);
		else change(rs[u],rs[v],mid+1,r,p,k);
	}
	int query(int rt,int u,int l,int r,int pl,int pr){
		int x=sum[rt]-sum[u];
		if(pl<=l&&r<=pr) return x;
		int res=0,mid=l+r>>1;
		if(pl<=mid) res+=query(ls[rt],ls[u],l,mid,pl,pr);
		if(pr>mid) res+=query(rs[rt],rs[u],mid+1,r,pl,pr);
		return res;
	}
}T[2];
struct node{
	int l,r,id;
}ques[N*3];
int ans[N];
int main(){
	n=read();n=2*n;
	m=read();
	for(int i=1;i<=m;i++){
		ques[i].l=read(),ques[i].r=read();
	}
	int q;q=read();
	for(int i=1;i<=q;i++){
		m++;
		ques[m].l=read(),ques[m].r=read();ques[m].id=i;
	}
	sort(ques+1,ques+m+1,[](node x,node y){return x.l<y.l;});
	for(int i=1;i<=m;i++){
		root[i]=root[i-1];
		if(!ques[i].id)
			T[0].change(root[i],root[i-1],1,n,ques[i].r,1);
		
	}
	for(int i=1;i<=m;i++){
		if(ques[i].id){
			int l=i,r=m;int res=0;
			while(l<=r){
				int mid=l+r>>1;
				if(ques[mid].l<=ques[i].r) res=mid,l=mid+1;
				else r=mid-1;
			}
			if(res){int t=T[0].query(root[res],root[i],1,n,ques[i].r,n);
				ans[ques[i].id]+=t;}
		}
	}
	sort(ques+1,ques+m+1,[](node x,node y){return x.r<y.r;});
	for(int i=1;i<=m;i++){
		
		root[i]=root[i-1];
		if(!ques[i].id)
		{
			T[1].change(root[i],root[i-1],1,n,ques[i].l,1);
		}
		
	}
	for(int i=1;i<=m;i++){
		if(ques[i].id){
			int l=1,r=i;int res=0;
			while(l<=r){
				int mid=l+r>>1;
				if(ques[mid].r>=ques[i].l) res=mid,r=mid-1;
				else l=mid+1;
			}
			if(res){int t=T[1].query(root[i],root[res],1,n,1,ques[i].l);
				ans[ques[i].id]+=t;}
		}
	}
	for(int i=1;i<=q;i++) cout<<ans[i]<<endl;
}