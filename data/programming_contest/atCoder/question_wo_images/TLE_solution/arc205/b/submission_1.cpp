#include<bits/stdc++.h>
using namespace std;
long long n,m;
vector<int > g[200005];
int main(){
    cin>>n>>m;
    if(m!=0){
        while(1)m++;
    }
    for(int i = 1;i<=m;i++){
        int u,v;
        scanf("%d%d",&u,&v);
        g[u].push_back(v);
        g[v].push_back(u);
    }
    cout<<(n)*(n-1)/2-(m%2)<<endl;
}