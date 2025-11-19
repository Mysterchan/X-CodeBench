#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for(int i = 0; i < (n); ++i)
int di[] = {1, 0, -1, 0};
int dj[] = {0, 1, 0, -1};


int main()
{
    #define int long long
    int N;
    cin >> N;
    vector<int> A(N);
    rep(i, N) cin >> A[i];
    sort(A.rbegin(), A.rend());
    int ans = 0;
    int j = 0;
    for(int i = 0; i < N; i++)
    {
        while(2 * A[j] > A[i] && j < N) j++;
        ans += N - j;
    }
    cout << ans << endl;
    return 0;
}