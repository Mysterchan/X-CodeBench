#include <bits/stdc++.h>
using namespace std;
using Graph = vector<vector<int>>;
#define rep(i, n) for(int i = 0;i < (int)(n);i++)
#define rep1(i, m, n) for(int i = (int)(m);i < (int)(n);i++)

int main(){
    int N, M; cin >> N >> M;
    string S,T;
    vector<int> Tcount(10, 0);
    vector<bool> used(10, false);
    rep(i, N){
        char s; cin >> s; S += s;
    }
    rep(i, M){
        char s; cin >> s; T += s;
        Tcount[s - '0']++;
    }
    string ans;
    rep(i, N){
        for(int j = 9;j >= 1;j--){
            if(S[i] - '0' >= j){
                ans += S[i];
                break;
            }else if(Tcount[j] > 0){
                ans += j + '0';
                Tcount[j]--;
                used[j] = true;
                break;
            }else if(j == 1){
                ans += S[i];
                break;
            }
        }
    }
    rep(i, N){
        if(ans[i] == T[M - 1]){
            cout << ans << endl;
            return 0;
        }
    }
    ans[N - 1] = T[M - 1];
    cout << ans << endl;
}