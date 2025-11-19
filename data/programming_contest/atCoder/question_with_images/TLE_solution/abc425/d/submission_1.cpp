#include<bits/stdc++.h>
using namespace std;

int findBlackCell(int m, int n, vector<vector<char>>& grid) {
    long long operations = 1e100;
    
    for (int t = 0; t < operations; ++t) {
        vector<pair<int, int>> to_paint;
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == '.') {
                    int black_neighbors = 0;
                    int dr[] = {-1, 1, 0, 0};
                    int dc[] = {0, 0, -1, 1};
                    
                    for (int k = 0; k < 4; ++k) {
                        int ni = i + dr[k];
                        int nj = j + dc[k];
                        
                        if (ni >= 0 && ni < m && nj >= 0 && nj < n) {
                            if (grid[ni][nj] == '#') {
                                black_neighbors++;
                            }
                        }
                    }
                    
                    if (black_neighbors == 1) {
                        to_paint.push_back({i, j});
                    }
                }
            }
        }
        
        if (to_paint.empty()) {
            break;
        }
        for (const auto& p : to_paint) {
            grid[p.first][p.second] = '#';
        }
    }
    
    int count = 0;
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (grid[i][j] == '#') {
                count++;
            }
        }
    }
    return count;
}

int main(){
  int m,n;
  cin>>m>>n;
  
  vector<vector<char>>grid(m,vector<char>(n));
  queue<pair<int,int>>q;
  vector<vector<bool>>vis(m,vector<bool>(n,false));
  for(int i=0;i<m;i++){
    for(int j=0;j<n;j++){
      cin>>grid[i][j];
      if(grid[i][j]=='#'){
        q.push({i,j});
        vis[i][j]=true;
      }
    }
  }
  
  int ans = findBlackCell(m,n,grid);
  cout<<ans<<endl;
  return 0;
}