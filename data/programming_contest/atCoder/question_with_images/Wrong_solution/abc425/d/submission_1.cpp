#include <bits/stdc++.h>
using namespace std;
int main(){
	int h,w;
	cin >> h >> w;
	vector<string> a(h);
	for(int i= 0;i < h;i ++){
		cin >> a[i];
	}
	int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
	vector<vector<int>> cnt(h,vector<int>(w,0));
	queue<pair<int,int>> q;
	
	for(int i = 0;i < h;i ++){
		for(int j = 0;j < w;j ++){
			if(a[i][j]=='.'){
				int c = 0;
				for(auto& d: dirs){
					int ni = i + d[0],nj = j + d[1];
					if(ni>=0&&ni < h&&nj>=0&&nj <w&&a[ni][nj]=='#'){
						c++; 
					}
				}
				cnt[i][j] = c;
				if(c == 1){
					q.emplace(i,j);
				}
			}
		}
	}
	while(!q.empty()){
		auto[i,j] = q.front();
		q.pop();
		
		if(a[i][j] == '#') continue;
		a[i][j] = '#';
		for(auto& d:dirs){
			int ni = i + d[0],nj = j +d[1];
			if(ni>=0&&ni<h&&nj>=0&&nj < w&&a[ni][nj]=='.'){
				cnt[ni][nj] ++;
				if(cnt[ni][nj] ==1){
					q.emplace(ni,nj);
				}
			}
		}	
	}
	int res = 0;
	for(int i = 0;i < h;i ++){
		res += count(a[i].begin(),a[i].end(),'#');
	}
	cout << res << endl;
	return 0;
}