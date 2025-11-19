#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> A(n);
    for(int i = 0; i < n; i++){
        cin >> A[i];
    }
    // freq[v]: total occurrences of value v
    vector<int> freq(n+1, 0);
    for(int i = 0; i < n; i++){
        freq[A[i]]++;
    }
    // order[i]: the 0-based occurrence index of A[i] among its value
    vector<int> order(n);
    // count occurrences as we scan
    vector<int> cnt(n+1, 0);
    for(int i = 0; i < n; i++){
        int v = A[i];
        order[i] = cnt[v];
        cnt[v]++;
    }
    // next_pos[i]: next occurrence index of A[i], or n if none
    vector<int> last_pos(n+1, n);
    vector<int> next_pos(n);
    for(int i = n-1; i >= 0; i--){
        int v = A[i];
        next_pos[i] = last_pos[v];
        last_pos[v] = i;
    }
    long long ans = 1;  // count the original sequence once
    for(int i = 0; i < n; i++){
        int v = A[i];
        int a = next_pos[i];
        // skip if next occurrence is immediately after i
        if(a == i+1) continue;
        // m = freq[v] + 1 (including sentinel), j = order[i]
        // add = n - i - m + j + 1 = n - i - (freq[v]+1) + order[i] + 1
        // simplify: = n - i - freq[v] + order[i]
        long long add = (long long)n - i - freq[v] + order[i];
        ans += add;
    }
    cout << ans << "\n";
    return 0;
}