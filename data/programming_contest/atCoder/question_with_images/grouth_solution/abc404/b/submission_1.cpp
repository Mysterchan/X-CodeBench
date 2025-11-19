#include<iostream>
#include<vector>
using namespace std;
int check(int n, vector<char> s, vector<char> t) {
    int count = n*n;
    for (int i = 0;i < n * n;i++)if (s[i] == t[i])count--;
    return count;
}
void turn(int n, vector<char>& s) {
    vector<char> a(n * n, 0);
    int number;
    for (int i = 0;i < n * n;i++) {
        number = (n - 1) - i / n + n * (i % n);
        a[number] = s[i];
    }
    for (int i = 0;i < n * n;i++)s[i] = a[i];
}
int main() {
    int n;
    cin >> n;
    vector<char> s(n * n);
    vector<char> t(n * n);
    for (int i = 0;i < n * n;i++)cin >> s[i];
    for (int i = 0;i < n * n;i++)cin >> t[i];
    int total[4] = {};
    total[0] = check(n, s, t);
    for (int i = 1;i < 4;i++) {
        turn(n, s);
        total[i] = check(n, s, t);
    }
    for (int i = 0;i < 4;i++)total[i] += i;
    int a = total[0];
    for (int i = 1;i < 4;i++) {
        if (total[i] < a) {
            a = total[i];
        }
    }
    cout << a;
}