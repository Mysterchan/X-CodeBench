#include<bits/stdc++.h>
using namespace std;

void solve(){
	int n,q;
	scanf("%d%d",&n,&q);
	getchar();
	vector<vector<char>>s(n + 2,vector<char>(n + 2,'\0'));
	for(int i = 1 ; i <= n ; i ++){
		for(int j = 1 ; j <= n ; j ++){
			scanf("%c",&s[i][j]);
		}
		getchar();
	}
	while(q --){
		int u,d,l,r;
		scanf("%d%d%d%d",&u,&d,&l,&r);
		getchar();
		int cnt = 0;
		for(int i = u ; i <= d - 1 ; i ++){
			for(int j = l ; j <= r - 1 ; j ++){
				if(s[i][j] == '.' && s[i + 1][j] == '.' && s[i][j + 1] == '.' && s[i + 1][j + 1] == '.'){
					cnt ++;
				}
			}
		}
		printf("%d\n",cnt);
	}
}

int main(){
	int t = 1;
	while(t --) solve();
	return 0;
}