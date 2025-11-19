#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    int n;
    cin >> n;
    vector<int> arrp(n + 1);  
    vector<int> arrq(n + 1);
    vector<int> result(n + 1); // To store the result directly

    for (int i = 1; i <= n; i++) {
        cin >> arrp[i];
    }
    for (int i = 1; i <= n; i++) {
        cin >> arrq[i];
    }

    // Create an index for bib numbers
    vector<int> bibIndex(n + 1);  
    for (int i = 1; i <= n; i++) {
        bibIndex[arrq[i]] = i; // Where each bib number Q_i is located
    }

    // Calculate results based on the staring person
    for (int i = 1; i <= n; i++) {
        int person = arrp[i]; // Person i is staring at person P_i
        result[i] = arrq[person]; // Take the bib number from person P_i
    }

    // Print results
    for (int i = 1; i <= n; i++) {
        cout << result[i];
        if (i < n) cout << " ";  
    }

    return 0;
}