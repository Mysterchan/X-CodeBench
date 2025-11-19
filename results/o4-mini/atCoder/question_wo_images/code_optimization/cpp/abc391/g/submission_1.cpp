#include <bits/stdc++.h>
using namespace std;
using ull = unsigned long long;
const int MOD = 998244353;
int addmod(int a, int b) { a += b; if (a >= MOD) a -= MOD; return a; }
int mulmod(long long a, long long b) { return int((a * b) % MOD); }

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    string S;
    cin >> N >> M >> S;

    // Unique characters in S
    vector<char> T;
    {
        bool seen[26] = {};
        for(char c: S) if(!seen[c-'a']){
            seen[c-'a'] = true;
            T.push_back(c);
        }
    }
    int K = T.size();
    int rem = 26 - K;

    // DP maps: state encoded in 4 bits per position, up to 10 positions => 40 bits
    unordered_map<ull,int> dp_cur, dp_nxt;
    dp_cur.reserve(1024);
    dp_nxt.reserve(1024);
    dp_cur[0ULL] = 1;

    for(int step = 0; step < M; step++){
        dp_nxt.clear();
        // reserve enough buckets to avoid rehash
        dp_nxt.reserve(dp_cur.size() * (K + 1));

        for(auto &kv: dp_cur){
            ull code = kv.first;
            int cnt = kv.second;
            // Transition for rem letters (not in S)
            if(rem){
                int v = mulmod(cnt, rem);
                auto it = dp_nxt.find(code);
                if(it==dp_nxt.end()){
                    dp_nxt.emplace(code, v);
                } else {
                    it->second = addmod(it->second, v);
                }
            } else {
                // if rem==0, skip
            }
            // Decode code to u[]
            int u[10];
            ull tmp = code;
            for(int j = 0; j < N; j++){
                u[j] = int(tmp & 0xF);
                tmp >>= 4;
            }
            // Transitions for each character in T
            for(char c: T){
                int pma = 0, ma = 0;
                ull newcode = 0;
                // we'll build newcode by accumulating shifted values
                // but we need to shift in reverse order (highest j last), so collect in array
                int newu[10];
                for(int j = 0; j < N; j++){
                    pma = ma;
                    ma = (u[j] > ma ? u[j] : ma);
                    if(S[j] == c){
                        newu[j] = pma + 1;
                    } else {
                        newu[j] = u[j];
                    }
                }
                // encode newu
                for(int j = N-1; j >= 0; j--){
                    newcode <<= 4;
                    newcode |= (ull)(newu[j]);
                }
                // add cnt
                auto it2 = dp_nxt.find(newcode);
                if(it2==dp_nxt.end()){
                    dp_nxt.emplace(newcode, cnt);
                } else {
                    it2->second = addmod(it2->second, cnt);
                }
            }
        }
        dp_cur.swap(dp_nxt);
    }

    // Collect results
    vector<int> res(N+1, 0);
    for(auto &kv: dp_cur){
        ull code = kv.first;
        int cnt = kv.second;
        int mx = 0;
        // decode and find max
        for(int j = 0; j < N; j++){
            int v = int(code & 0xF);
            if(v > mx) mx = v;
            code >>= 4;
        }
        res[mx] = addmod(res[mx], cnt);
    }
    // Output
    for(int k = 0; k <= N; k++){
        cout << res[k] << (k==N?'\n':' ');
    }
    return 0;
}