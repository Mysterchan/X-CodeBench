#include <bits/stdc++.h>
using namespace std;
const int N = 1e6 + 7;

int n, q, op, x, y, i, pplace[N], nestname[N];
int main(){
	cin>>n>>q;
	for(i=1;i<=n;i++)pplace[i]=nestname[i]=i;
	while(q--){
		cin>>op>>x;
		if(op-3)cin>>y;
		if(op==1) pplace[x]=y;
		if(op==2) swap(nestname[x],nestname[y]);
		if(op==3) cout<<nestname[pplace[x]]<<"\n";
	}
	return 0;
}
