#include <bits/stdc++.h>
using namespace std;
using ll = long long;

static const int BITS = 60;

// We'll group items by their exponent, sort descending, take prefix‐sums.
// Then do a bitwise‐DP from the top bit down, carrying "capacity units".
// We keep dp_prev[x] = max value achievable at the current bit level with x carry‐units.
// We cap carry‐units by the total number of items available so far.

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--){
        int N;
        ll W;
        cin >> N >> W;
        // Read items by exponent
        vector<vector<ll>> v(BITS);
        for(int i = 0; i < N; i++){
            int x; ll y;
            cin >> x >> y;
            v[x].push_back(y);
        }
        // Sort each bucket descending and make prefix sums
        vector<vector<ll>> pref(BITS);
        vector<int> cnt(BITS);
        for(int b = 0; b < BITS; b++){
            auto &V = v[b];
            if (V.empty()) continue;
            sort(V.begin(), V.end(), greater<ll>());
            cnt[b] = int(V.size());
            pref[b].resize(V.size()+1);
            pref[b][0] = 0;
            for(int i = 0; i < (int)V.size(); i++){
                pref[b][i+1] = pref[b][i] + V[i];
            }
        }
        // pf[b] = total items in bits [0..b]
        vector<int> pf(BITS);
        pf[0] = cnt[0];
        for(int b = 1; b < BITS; b++){
            pf[b] = pf[b-1] + cnt[b];
        }

        // dp_prev and dp_cur: we only need to store up to pf[b] units.
        // We'll use a large negative as -inf.
        const ll NEG_INF = LLONG_MIN / 4;
        vector<ll> dp_prev, dp_cur;
        dp_prev.assign(1, 0); // at bit = BITS, carry=0 -> value=0

        // Process bits from high (BITS-1) down to 0
        for(int b = BITS-1; b >= 0; b--){
            int have_items = pf[b];
            // Maximum carry units we ever need is have_items (extra units beyond that can't pick more items)
            dp_cur.assign(have_items+1, NEG_INF);

            // Precompute whether W has this bit
            int wbit = ((W >> b) & 1);

            // For each possible carry_in from dp_prev
            // carry_in ≤ previous pf[b+1], but we'll cap it to have_items
            for(int carry_in = 0; carry_in < (int)dp_prev.size(); carry_in++){
                ll base_val = dp_prev[carry_in];
                if (base_val < 0 && carry_in>0) continue; // skip unreachable

                // total units at this bit
                int units = carry_in + wbit;
                if (units > have_items) units = have_items;

                // Try taking t = 0..units items from v[b]
                // value gained = pref[b][t], leftover units = units - t,
                // which become carry_out = min( pf[b-1], 2*(units - t) )
                for(int t = 0; t <= units; t++){
                    ll val = base_val + pref[b][t];
                    int leftover = units - t;
                    int carry_out = leftover * 2;
                    // cap carry_out for next bit
                    if (b > 0 && carry_out > pf[b-1]) carry_out = pf[b-1];
                    if (b == 0) {
                        // at bit 0, no next bit: we can accumulate into dp_cur[0]
                        dp_cur[0] = max(dp_cur[0], val);
                    } else {
                        dp_cur[carry_out] = max(dp_cur[carry_out], val);
                    }
                }
            }
            // swap dp_prev / dp_cur, but trim leading unreachable
            dp_prev.swap(dp_cur);
        }

        // After finishing bit 0, the only meaningful index is carry=0
        ll answer = dp_prev[0];
        if (answer < 0) answer = 0;
        cout << answer << "\n";
    }

    return 0;
}