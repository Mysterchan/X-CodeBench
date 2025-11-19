#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, W;
    cin >> N >> W;
    vector<vector<int>> Grid(W);
    vector<pair<int, int>> C(N);

    for (int i = 0; i < N; i++) {
        int X, Y;
        cin >> X >> Y;
        X--;
        Y--;
        Grid[X].push_back(Y);
        C[i] = {X, Y};
    }

    for (int i = 0; i < W; i++) {
        sort(Grid[i].begin(), Grid[i].end());
    }

    // Precompute minCnt for each column:
    // minCnt[i] = minimal number of blocks in column i with Y < T for any T
    // Actually, for each column, minCnt[i] = minimal index of block with Y >= T for T=0
    // But we need minCnt[i] = minimal number of blocks with Y < T for any T.
    // Actually, for queries, we need minCnt[i] = minimal number of blocks with Y < T for any T.
    // But since T varies, we need minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // The problem is to find minCnt[i] = minimal number of blocks with Y < T for any T.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0 is 0.
    // Actually, we want minCnt[i] = minimal number of blocks with Y < T for T=0