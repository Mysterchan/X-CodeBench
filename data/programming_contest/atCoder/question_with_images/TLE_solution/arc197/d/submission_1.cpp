#include <iostream>
#include <vector>
#include <numeric>
#include <map>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= 998244353;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % 998244353;
        base = (base * base) % 998244353;
        exp /= 2;
    }
    return res;
}

struct mint {
    long long val;
    mint(long long v = 0) {
        if (v < 0) v = v % 998244353 + 998244353;
        val = v % 998244353;
    }
    mint& operator+=(const mint& other) {
        val += other.val;
        if (val >= 998244353) val -= 998244353;
        return *this;
    }
     mint& operator-=(const mint& other) { 
        val -= other.val;
        if (val < 0) val += 998244353;
        return *this;
    }
    mint& operator*=(const mint& other) {
        val = (val * other.val) % 998244353;
        return *this;
    }
    friend mint operator+(mint a, const mint& b) { return a += b; }
    friend mint operator-(mint a, const mint& b) { return a -= b; }
    friend mint operator*(mint a, const mint& b) { return a *= b; }
     bool operator==(const mint& other) const { return val == other.val; } 
};


int N;
vector<vector<int>> A;

map<pair<vector<int>, int>, mint> memo;


mint count_trees(vector<int> S, int R) { 
    if (S.size() == 1) {
        return mint(1);
    }

    sort(S.begin(), S.end());
    pair<vector<int>, int> state = {S, R};
    
    auto it = memo.find(state);
    if (it != memo.end()) {
        return it->second;
    }

    for (int i_val : S) {
         if (A[R-1][i_val-1] == 0) { 
             return memo[state] = mint(0);
         }
    }

    vector<int> S_minus_R_vals;
    S_minus_R_vals.reserve(S.size() - 1);
    map<int, int> val_to_idx_map; 
    for (int i_val : S) {
        if (i_val != R) {
             S_minus_R_vals.push_back(i_val);
             val_to_idx_map[i_val] = S_minus_R_vals.size() - 1;
        }
    }

    if (S_minus_R_vals.empty()) {
         return memo[state] = mint(1); 
    }


    int num_nodes_sub = S_minus_R_vals.size();
    vector<vector<int>> adj_sub(num_nodes_sub);
    for (int i = 0; i < num_nodes_sub; ++i) {
        for (int j = i + 1; j < num_nodes_sub; ++j) {
            if (A[S_minus_R_vals[i]-1][S_minus_R_vals[j]-1] == 1) {
                adj_sub[i].push_back(j);
                adj_sub[j].push_back(i);
            }
        }
    }

    vector<vector<int>> components;
    vector<bool> visited(num_nodes_sub, false);
    for (int i = 0; i < num_nodes_sub; ++i) {
        if (!visited[i]) {
            vector<int> current_component_nodes;
            vector<int> q;
            q.push_back(i);
            visited[i] = true;
            int head = 0;
            while(head < q.size()){
                int u_idx = q[head++];
                current_component_nodes.push_back(S_minus_R_vals[u_idx]);
                for(int v_idx : adj_sub[u_idx]){
                    if(!visited[v_idx]){
                        visited[v_idx] = true;
                        q.push_back(v_idx);
                    }
                }
            }
             if(!current_component_nodes.empty()) 
               components.push_back(current_component_nodes);
        }
    }

    for (size_t p = 0; p < components.size(); ++p) {
        for (size_t q = p + 1; q < components.size(); ++q) {
            for (int i_val : components[p]) {
                for (int j_val : components[q]) {
                    if (A[i_val-1][j_val-1] == 1) {
                         return memo[state] = mint(0);
                    }
                }
            }
        }
    }

    mint total_count = mint(1);

    for (const auto& comp_vals : components) {
        vector<int> Kp;
        Kp.reserve(comp_vals.size());
        for (int v_val : comp_vals) {
            bool is_potential_root = true;
            for (int i_val : comp_vals) {
                if (A[v_val-1][i_val-1] == 0) {
                    is_potential_root = false;
                    break;
                }
            }
            if (is_potential_root) {
                Kp.push_back(v_val);
            }
        }

        if (Kp.empty()) {
            return memo[state] = mint(0);
        }

        mint component_sum = mint(0);
        vector<int> current_comp = comp_vals;
        for (int Cp : Kp) {
            component_sum += count_trees(current_comp, Cp);
        }
        
        if (component_sum.val == 0) {
             total_count = mint(0); 
             break;
        }
        total_count *= component_sum;
    }
    
    return memo[state] = total_count;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    while (T--) {
        cin >> N;
        A.assign(N, vector<int>(N));
        vector<int> initial_S(N);
        iota(initial_S.begin(), initial_S.end(), 1);

        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                cin >> A[i][j];
            }
        }

        bool possible = true;
        for(int i=0; i<N; ++i){
             if (A[i][i] == 0) { 
                 possible = false; break;
             }
        }
        if(!possible) { cout << 0 << "\n"; continue; }

        for(int i=0; i<N; ++i){
            for(int j=i+1; j<N; ++j){
                 if(A[i][j] != A[j][i]) { 
                      possible = false; break;
                 }
            }
             if (!possible) break;
        }
         if(!possible) { cout << 0 << "\n"; continue; }

        for(int j=0; j<N; ++j) {
            if(A[0][j] == 0) {
                possible = false; break;
            }
        }
        if(!possible) { cout << 0 << "\n"; continue; }


        memo.clear();
        mint result = count_trees(initial_S, 1); 
        cout << result.val << "\n";
    }
    return 0;
}
