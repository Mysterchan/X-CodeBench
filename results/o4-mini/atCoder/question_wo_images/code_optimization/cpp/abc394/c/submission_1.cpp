#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    if (!(cin >> s)) return 0;
    int n = s.size();
    set<int> st;
    for (int i = 0; i + 1 < n; i++) {
        if (s[i] == 'W' && s[i+1] == 'A') {
            st.insert(i);
        }
    }

    while (!st.empty()) {
        int i = *st.begin();
        st.erase(st.begin());
        // Replace WA at i with AC
        s[i] = 'A';
        s[i+1] = 'C';
        // Update possible WA occurrences around the replaced segment
        for (int j = i - 1; j <= i + 1; j++) {
            if (j >= 0 && j + 1 < n) {
                if (s[j] == 'W' && s[j+1] == 'A') {
                    st.insert(j);
                } else {
                    st.erase(j);
                }
            }
        }
    }

    cout << s << "\n";
    return 0;
}