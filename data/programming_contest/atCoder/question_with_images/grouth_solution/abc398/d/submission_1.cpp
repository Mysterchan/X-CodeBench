#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int n,r,c,R,C;
    cin>>n>>r>>c;
    R=r;C=c;
    string a;
    cin>>a;
    map<pair<int,int>,bool>m;
    m[{0,0}]=1;
    for(int i=0;i<n;i++){
    	if(a[i]=='N')r++;
    	else if(a[i]=='S')r--;
    	else if(a[i]=='W')c++;
    	else if(a[i]=='E')c--;
    	m[{r-R,c-C}]=1;
    	if(m[{r,c}]==0)cout<<0;
    	else cout<<1;    		
	}
    return 0;
}