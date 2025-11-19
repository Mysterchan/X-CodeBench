#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<string> mat(n);
    for(int i = 0; i < n; i++){
        cin >> mat[i];
    }

    // out_by_char[u][c] = list of v's with edge u->v labeled c
    // in_by_char[v][c]  = list of u's with edge u->v labeled c
    static vector<int> out_by_char[100][26], in_by_char[100][26];

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            char ch = mat[i][j];
            if(ch == '-') continue;
            int c = ch - 'a';
            out_by_char[i][c].push_back(j);
            in_by_char[j][c].push_back(i);
        }
    }

    const int INF = INT_MAX;
    static int dist[100][100];
    static bool vis[100][100];
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            dist[i][j] = INF;
            vis[i][j] = false;
        }
    }

    deque<pair<int,int>> q;

    // Multi-source initialization:
    // (u,u) = distance 0
    for(int u = 0; u < n; u++){
        vis[u][u] = true;
        dist[u][u] = 0;
        q.emplace_back(u,u);
    }
    // Any direct edge u->v gives a palindrome of length 1
    for(int u = 0; u < n; u++){
        for(int c = 0; c < 26; c++){
            for(int v: out_by_char[u][c]){
                if(!vis[u][v]){
                    vis[u][v] = true;
                    dist[u][v] = 1;
                    q.emplace_back(u,v);
                }
            }
        }
    }

    // BFS
    while(!q.empty()){
        auto [u,v] = q.front();
        q.pop_front();
        int duv = dist[u][v];
        // Try to prepend c on left (x->u) and append c on right (v->y)
        for(int c = 0; c < 26; c++){
            auto &lefts  = in_by_char[u][c];
            auto &rights = out_by_char[v][c];
            if(lefts.empty() || rights.empty()) continue;
            int nd = duv + 2;
            for(int x: lefts){
                for(int y: rights){
                    if(!vis[x][y]){
                        vis[x][y] = true;
                        dist[x][y] = nd;
                        q.emplace_back(x,y);
                    }
                }
            }
        }
    }

    // Output
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(dist[i][j] == INF) 
                cout << -1 << (j+1<n?' ':'\n');
            else
                cout << dist[i][j] << (j+1<n?' ':'\n');
        }
    }
    return 0;
}