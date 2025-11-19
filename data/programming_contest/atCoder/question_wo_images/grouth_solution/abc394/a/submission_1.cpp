#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define ALL(a) (a).begin(), (a).end()
#define Yes cout << "Yes" << endl
#define No cout << "No" << endl
#define el '\n'
using pri_que = priority_queue<int, vector<int>, greater<int>>;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string S;
    cin >> S;
    for (auto& s : S) {
        if (s == '2')
            cout << s;
    }
    cout << el;
}
