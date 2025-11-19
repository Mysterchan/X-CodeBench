#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=a;i<b;i++)
#define rrep(i,a,b) for(int i=a;i>=b;i--)
#define fore(i,a) for(auto &i:a)
#define all(x) (x).begin(),(x).end()
typedef long long ll; 

int main (){
    ll rt, ct, ra, ca; cin >> rt >> ct >> ra >> ca;
    ll N, M, L; cin >> N >> M >> L;
    string S, T;
    vector<ll> A(M), B(L);
    rep(i,0,M) {
        char c; cin >> c;
        S += c;
        cin >> A[i];
    }

    rep(i,0,L) {
        char c; cin >> c;
        T += c;
        cin >> B[i];
    }

    ll ans = 0;
    ll a = 0, b = 0;
    while(a < M and b < L) {
        ll n = min(A[a], B[b]);
        ll rm = (ra + rt)/2;
        ll cm = (ca + ct)/2;
        if (rt == ra and ct == ca ){
            if (S[a]==T[b]) ans += n;
        }
        else if (S[a]=='U'){
            if (T[b]=='U'){

                if (rt == ra and ct == ca ){
                    ans += n;
                }
            }
            else if (T[b]=='D'){

                if (cm == ca and cm == ct and rm-rt==ra-rm and rm-rt<=n) ans++;
            }
            else if (T[b]=='L'){
                rm = ra;
                cm = ct;
                if (rt - rm == ca - cm and rt-rm <= n) ans++;
            }
            else if (T[b]=='R'){
                rm = ra;
                cm = ct;
                if (rt - rm == cm - ca and rt-rm <= n) ans++;
            }

        }
        else if (S[a]=='D'){
            if (T[b]=='U'){
                
                if (cm == ca and cm == ct and ra-rm==rm-rt and ra-rm<=n) ans++;
            }
            else if (T[b]=='D'){
                if (rt == ra and ct == ca ){
                    ans += n;
                }
            }
            else if (T[b]=='L'){
                ll rm = ra;
                ll cm = ct;
                if (rm - rt == ca - cm and rm-rt <= n) ans++;
            }
            else if (T[b]=='R'){
                ll rm = ra;
                ll cm = ct;
                if (rm - rt == cm - ca and rm-rt <= n) ans++;
            }
        }
        else if (S[a]=='L'){
            if (T[b]=='U'){
                ll rm = ra;
                ll cm = ct;
                if (cm - ca == rt - rm and cm-ca<=n) ans++;
            }
            else if (T[b]=='D'){
                ll rm = ra;
                ll cm = ct;
                if (cm - ca == rm - rt and cm-ca<=n) ans++;
            }
            else if (T[b]=='L'){
                if (rt == ra and ct == ca ){
                    ans += n;
                }
            }
            else if (T[b]=='R'){
                if (cm == ca and cm == ct and ra-rm==rm-rt and ra-rm<=n) ans++;
            }
        }
        else if (S[a]=='R'){
            if (T[b]=='U'){
                ll rm = ra;
                ll cm = ct;
                if (ca - cm == rt - rm and ca-cm<=n) ans++;
            }
            else if (T[b]=='D'){
                ll rm = ra;
                ll cm = ct;
                if (ca - cm == rm - rt and ca-cm<=n) ans++;
            }
            else if (T[b]=='L'){
                if (cm == ca and cm == ct and ca-cm==cm-ct and ca-cm<=n) ans++;
            }
            else if (T[b]=='R'){
                if (rt == ra and ct == ca ){
                    ans += n;
                }
            }
        }


        if (S[a] == 'U') rt -= n;
        else if (S[a] == 'D') rt += n;
        else if (S[a] == 'L') ct -= n;
        else if (S[a] == 'R') ct += n;
        if (T[b] == 'U') ra -= n;
        else if (T[b] == 'D') ra += n;
        else if (T[b] == 'L') ca -= n;
        else if (T[b] == 'R') ca += n;
        A[a] -= n;
        B[b] -= n;
        if (A[a] == 0) a++;
        if (B[b] == 0) b++;
    }
    cout << ans << endl;
    return 0;
}