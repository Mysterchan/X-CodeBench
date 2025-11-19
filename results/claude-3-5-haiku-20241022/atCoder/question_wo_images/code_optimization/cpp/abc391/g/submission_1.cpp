#include <bits/stdc++.h>
using namespace std;

const long long MOD = 998244353;

int N, M;
string S;

struct State {
    long long key;
    
    State() : key(0) {}
    
    State(const vector<int>& v) {
        key = 0;
        for (int i = 0; i < N; i++) {
            key = key * 11 + v[i];
        }
    }
    
    bool operator==(const State& other) const {
        return key == other.key;
    }
};

struct StateHash {
    size_t operator()(const State& s) const {
        return hash<long long>()(s.key);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    cin >> N >> M >> S;
    
    string T = S;
    sort(T.begin(), T.end());
    T.erase(unique(T.begin(), T.end()), T.end());
    long long rem = 26 - T.size();
    
    unordered_map<State, long long, StateHash> DP[2];
    int curr = 0, next = 1;
    
    vector<int> init(N, 0);
    DP[curr][State(init)] = 1;
    
    for (int i = 0; i < M; i++) {
        DP[next].clear();
        
        for (auto& p : DP[curr]) {
            long long key = p.first.key;
            long long val = p.second % MOD;
            
            // Decode state
            vector<int> vec(N);
            long long temp = key;
            for (int j = N - 1; j >= 0; j--) {
                vec[j] = temp % 11;
                temp /= 11;
            }
            
            // Add rem characters that don't change state
            State s(vec);
            DP[next][s] = (DP[next][s] + val * rem) % MOD;
            
            // Add each character from T
            for (char c : T) {
                vector<int> u = vec;
                int ma = 0;
                for (int j = 0; j < N; j++) {
                    int pma = ma;
                    ma = max(ma, u[j]);
                    if (c == S[j]) {
                        u[j] = pma + 1;
                    }
                }
                State ns(u);
                DP[next][ns] = (DP[next][ns] + val) % MOD;
            }
        }
        
        swap(curr, next);
    }
    
    vector<long long> res(N + 1, 0);
    
    for (auto& p : DP[curr]) {
        long long key = p.first.key;
        long long val = p.second % MOD;
        
        vector<int> vec(N);
        long long temp = key;
        for (int j = N - 1; j >= 0; j--) {
            vec[j] = temp % 11;
            temp /= 11;
        }
        
        int lcs = 0;
        for (int j = 0; j < N; j++) {
            lcs = max(lcs, vec[j]);
        }
        res[lcs] = (res[lcs] + val) % MOD;
    }
    
    for (int i = 0; i <= N; i++) {
        cout << res[i];
        if (i < N) cout << " ";
    }
    cout << "\n";
    
    return 0;
}