#include<bits/stdc++.h>
using namespace std;

#define LL long long
#define mod 998244353

int main() {
    int n;
    cin >> n;
    string s;
    cin >> s;

    // Count the number of '1's in the input string
    int count_one = count(s.begin(), s.end(), '1');

    // The total number of distinct sequences is determined by the number of 1's
    // and the combinations of edges which can point in different directions
    LL result = (count_one + 1) * (count_one + 1) % mod; // (k+1)^2 where k = number of 1's

    // To account for sequences that include the edges between 0 and N (if edges exist)
    if (count_one > 0) {
        result = (result * 2) % mod; // Each '1' can connect to vertex N or not
    }

    cout << result << endl;
    return 0;
}
