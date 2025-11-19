#include <iostream>
using namespace std;

int main() {
    int t; 
    cin >> t;
    while (t--) {
        int n; 
        cin >> n;
        // The total number of matches is always (n - 1) for n teams
        cout << (n - 1) + (n - 1) << endl;  // (n - 1) matches in winners and (n - 1) in losers
    }
    return 0;
}