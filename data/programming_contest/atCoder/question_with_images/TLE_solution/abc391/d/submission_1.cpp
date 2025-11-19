#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
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
    
    int Q;
    cin >> Q;
    for (int q = 0; q < Q; q++) {
        int T, A;
        cin >> T >> A;
        A--;
        int X = C[A].first;
        int Y = C[A].second;
        
        if (Y - T >= 0) {
            cout << "Yes" << endl;
            continue;
        }
        
        int cnt = lower_bound(Grid[X].begin(), Grid[X].end(), Y) - Grid[X].begin();
        bool found = false;
        for (int i = 0; i < W; i++) {
            if (i == X) continue;
            int cnt_i = lower_bound(Grid[i].begin(), Grid[i].end(), T) - Grid[i].begin();
            if (cnt >= cnt_i) {
                cout << "Yes" << endl;
                found = true;
                break;
            }
        }
        if (!found) {
            cout << "No" << endl;
        }
    }
    
    return 0;
}