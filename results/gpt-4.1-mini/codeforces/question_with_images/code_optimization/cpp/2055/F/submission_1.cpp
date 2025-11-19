#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pll = pair<ll,ll>;

bool ren(const vector<pll> &S){
    int N = (int)S.size();
    for(int i = 1; i < N; i++){
        ll l = max(S[i-1].first, S[i].first);
        ll r = min(S[i-1].second, S[i].second);
        if(l > r) return false;
    }
    return true;
}

bool goudou(vector<pll> A, vector<pll> B){
    int N = (int)A.size();
    ll a = A[0].first, b = B[0].first;
    for(int i = 0; i < N; i++){
        A[i].first -= a;
        A[i].second -= a;
        B[i].first -= b;
        B[i].second -= b;
    }
    return A == B;
}

bool solve(const vector<pll> &S){
    int N = (int)S.size();

    // Try splitting each row into two halves if length even
    {
        vector<pll> A, B;
        bool ok = true;
        for(auto [a,b]: S){
            ll len = b - a + 1;
            if(len & 1){
                ok = false;
                break;
            }
            ll half = len / 2;
            A.emplace_back(a, a + half - 1);
            B.emplace_back(b - half + 1, b);
        }
        if(ok && ren(A) && ren(B) && goudou(A, B)) return true;
    }

    // Try vertical splits with offset dh
    // dh must be <= N/2
    // We only try dh where parity condition holds
    ll sum2 = 0;
    for(int i = 0; i < N; i++){
        ll len = S[i].second - S[i].first + 1;
        if(i & 1) sum2 -= len;
        else sum2 += len;
    }

    for(int dh = 1; dh * 2 <= N; dh++){
        if((dh & 1) && sum2 != 0) continue;

        vector<pll> A, B;
        bool ok = true;

        for(int i = 0; i < N; i++){
            if(i < dh){
                A.push_back(S[i]);
            } else if(i < N - dh){
                ll len = A[i - dh].second - A[i - dh].first + 1;
                ll startB = S[i].first;
                ll endB = startB + len - 1;
                if(endB > S[i].second){
                    ok = false;
                    break;
                }
                B.emplace_back(startB, endB);
                ll startA = endB + 1;
                ll endA = S[i].second;
                if(startA > endA){
                    ok = false;
                    break;
                }
                A.emplace_back(startA, endA);
            } else {
                ll len = A[i - dh].second - A[i - dh].first + 1;
                ll startB = S[i].first;
                ll endB = startB + len - 1;
                if(endB != S[i].second){
                    ok = false;
                    break;
                }
                B.emplace_back(startB, endB);
            }
        }

        if(ok && ren(A) && ren(B) && goudou(A, B)) return true;
    }

    return false;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int Q; cin >> Q;
    while(Q--){
        int N; cin >> N;
        vector<pll> S(N);
        for(int i = 0; i < N; i++){
            ll l, r; cin >> l >> r;
            S[i] = {l, r};
        }

        bool ans = false;
        for(int attempt = 0; attempt < 2; attempt++){
            if(solve(S)){
                ans = true;
                break;
            }
            // Reflect horizontally
            for(int i = 0; i < N; i++){
                ll l = S[i].first, r = S[i].second;
                S[i].first = 1000000001 - r;
                S[i].second = 1000000001 - l;
            }
        }

        cout << (ans ? "YES\n" : "NO\n");
    }
}