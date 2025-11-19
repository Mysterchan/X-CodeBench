#include<bits/stdc++.h>
using namespace std;
int n,a[1000005],qq,e[1000005],uu,h[1000005],q[1000005],t,op,l,r,c;
int find(int x){
	int r=e[x/uu];
	x-=x/uu*uu;
	while(x--)r=h[r];
	return r;
}
signed main(){
	ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
	cin>>qq;n=0;uu=max(1,(int)sqrt(qq/2));h[0]=1;
	q[1]=0;c=1;
	for(int i=1;i<=qq;i++){
		cin>>l;r=i;
		int ll=l;ll=(ll+uu-1)/uu;
		l=find(l);
		h[q[l]]=++c;
		q[c]=q[l];
		q[l]=c;
		h[c]=l;
		a[c]=r;
		for(int i=ll;i<=t;i++)e[i]=q[e[i]];
		if(c%uu==0)e[++t]=1;
	}
	int x=h[h[1]];
	while(qq--){
		cout<<a[x]<<" ";
		x=h[x];
	}
	return 0;
}