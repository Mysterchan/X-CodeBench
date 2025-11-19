#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> P(n + 1);
    vector<int> Q(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> P[i];
    }
    for (int i = 1; i <= n; i++) {
        cin >> Q[i];
    }

    // Create an array to map bib number to person index
    vector<int> bib_to_person(n + 1);
    for (int i = 1; i <= n; i++) {
        bib_to_person[Q[i]] = i;
    }

    // For each bib number i, find the person they stare at and print that person's bib number
    for (int i = 1; i <= n; i++) {
        int person = bib_to_person[i];
        int stared_person = P[person];
        cout << Q[stared_person];
        if (i < n) cout << ' ';
    }
    cout << '\n';

    return 0;
}