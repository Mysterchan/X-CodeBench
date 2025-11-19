#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string S;
    cin >> S;
    if (S.size() % 2 == 1) {
        cout << "No\n";
        return 0;
    }

    vector<char> st;
    st.reserve(S.size());
    for (char c : S) {
        if (c == '(' || c == '[' || c == '<') {
            st.push_back(c);
        } else {
            if (st.empty()) {
                cout << "No\n";
                return 0;
            }
            char o = st.back();
            st.pop_back();
            if (!((o == '(' && c == ')') ||
                  (o == '[' && c == ']') ||
                  (o == '<' && c == '>'))) {
                cout << "No\n";
                return 0;
            }
        }
    }
    cout << (st.empty() ? "Yes\n" : "No\n");
    return 0;
}