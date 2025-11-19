#include <bits/stdc++.h>
using namespace std;
const int MOD = 998244353;

int add_mod(int a, int b) {
    a += b;
    if (a >= MOD) a -= MOD;
    return a;
}

int mul_mod(long long a, long long b) {
    return int((a * b) % MOD);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, L, R;
    cin >> N >> L >> R;
    vector<int> A(N+1), B(N+1);
    for (int i = 1; i <= N; i++) cin >> A[i];
    for (int i = 1; i <= N; i++) cin >> B[i];

    // Prefix sum of B to bound C
    vector<int> PB(N+1, 0);
    for (int i = 1; i <= N; i++) {
        PB[i] = PB[i-1] + B[i];
    }
    int Cmax = PB[N];

    // dp[q][c]: number of ways with queue size q and C=c
    // We'll use rolling arrays: dp_cur and dp_nxt
    vector< vector<int> > dp_cur(N+1, vector<int>(Cmax+1, 0));
    vector< vector<int> > dp_nxt(N+1, vector<int>(Cmax+1, 0));
    // curSize[q]: maximum index c used in dp_cur[q]; -1 means unused
    vector<int> curSize(N+1, -1), nxtSize(N+1, -1);
    vector<int> usedCur, usedNxt;

    // initial state: step=0, q=0, C=0
    dp_cur[0][0] = 1;
    curSize[0] = 0;
    usedCur.push_back(0);

    int total_steps = 2 * N;
    for (int step = 0; step < total_steps; step++) {
        usedNxt.clear();
        // process all used queue-sizes for this step
        for (int idx = 0; idx < (int)usedCur.size(); idx++) {
            int q = usedCur[idx];
            int sz = curSize[q];
            if (sz < 0) continue;
            // parity check: step and q must have same parity (i+j=step, i-j=q => both even or odd)
            if ((step ^ q) & 1) continue;
            // compute how many pushes and pops have occurred
            int pushed = (step + q) / 2;
            int popped = step - pushed;
            // pointer to dp data
            int *dpv = dp_cur[q].data();

            // Action 1: push next if possible
            if (pushed < N) {
                int ai = A[pushed + 1];
                int nq = q + 1;
                // ensure nxtSize[nq] initialized
                if (nxtSize[nq] < 0) {
                    nxtSize[nq] = -1;
                    usedNxt.push_back(nq);
                }
                int &nqs = nxtSize[nq];
                // prefix sum to handle clamp-to-zero part
                long long pref = 0;
                int upto = min(sz, ai - 1);
                for (int c = 0; c <= upto; c++) {
                    pref += dpv[c];
                    if (pref >= MOD) pref -= MOD;
                }
                // c_new = 0 from all c<=ai-1
                dp_nxt[nq][0] = add_mod(dp_nxt[nq][0], int(pref));
                if (nqs < 0) nqs = 0;
                // for c >= ai: shift by ai
                if (sz >= ai) {
                    for (int c = ai; c <= sz; c++) {
                        int ways = dpv[c];
                        if (ways) {
                            int nc = c - ai;
                            dp_nxt[nq][nc] = add_mod(dp_nxt[nq][nc], ways);
                            if (nc > nqs) nqs = nc;
                        }
                    }
                }
            }
            // Action 2: pop if possible
            if (q > 0 && popped < N) {
                int bi = B[popped + 1];
                int nq = q - 1;
                if (nxtSize[nq] < 0) {
                    nxtSize[nq] = -1;
                    usedNxt.push_back(nq);
                }
                int &nqs = nxtSize[nq];
                // shift by +bi
                for (int c = 0; c <= sz; c++) {
                    int ways = dpv[c];
                    if (ways) {
                        int nc = c + bi;
                        dp_nxt[nq][nc] = add_mod(dp_nxt[nq][nc], ways);
                        if (nc > nqs) nqs = nc;
                    }
                }
            }
        }
        // clear old dp_cur entries
        for (int q : usedCur) {
            int sz = curSize[q];
            if (sz >= 0) {
                auto &arr = dp_cur[q];
                for (int c = 0; c <= sz; c++) arr[c] = 0;
            }
            curSize[q] = -1;
        }
        // swap dp_cur <-> dp_nxt, curSize <-> nxtSize, usedCur <-> usedNxt
        dp_cur.swap(dp_nxt);
        curSize.swap(nxtSize);
        usedCur.swap(usedNxt);
    }

    // result is dp_cur[0][c] for L<=c<=R
    int res = 0;
    if (curSize[0] >= 0) {
        int hi = min(curSize[0], R);
        for (int c = L; c <= hi; c++) {
            res = add_mod(res, dp_cur[0][c]);
        }
    }
    cout << res << "\n";
    return 0;
}