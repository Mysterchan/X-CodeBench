#include<bits/stdc++.h>

using namespace std;
using ll = long long;

bool pass = true;
int H, W, K;
int color = 0;
map<vector<int>, int> visited;

void dfs(vector<int> rc) {

    if(rc[1] == 0 || rc[0] == H-1) {
        pass = false; return;
    }

    for(int i = -1; i <= 1; i++)
        for(int j = -1; j <= 1; j++) {
            if(i == j && j == 0) continue;

            vector<int> newrc = {rc[0] + i, rc[1]+j};
            if(0 <= newrc[0] && newrc[0] < H && 0 <= newrc[1] && newrc[1] < W)
                if(visited[newrc] < 0) {
                    visited[newrc] = visited[rc];
                    dfs(newrc);
                }
        }

}

int main() {

    cin >> H >> W >> K;

    vector<vector<int>> obs(K, vector<int>(2));
    
    for(int i = 0; i < K; i++) {
        cin >> obs[i][0] >> obs[i][1];
        obs[i][0]--; obs[i][1]--;
        visited[obs[i]] = -1;

    }


    for(int i = 1; i < W; i++){
        if(!pass)   break;
        if(visited[{0, i}] < 0) {
            color++;
            visited[{0, i}] = color;
            dfs({0, i});
        }
    }
        

    for(int i = 1; i < H; i++){
        if(!pass)   break;
        if(visited[{i, W-1}] < 0) {
            color++;
            visited[{i, W-1}] = color;
            dfs({i, W-1});
        }
    }


    if(pass)    cout << "Yes";
    else cout << "No";

    




    

    
}