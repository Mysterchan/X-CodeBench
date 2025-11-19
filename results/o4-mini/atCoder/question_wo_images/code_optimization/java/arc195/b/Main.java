#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;
    vector<int> arrA, arrB;
    arrA.reserve(N);
    arrB.reserve(N);
    int U_A = 0, U_B = 0;
    long long maxA = 0, maxB = 0;
    for(int i = 0; i < N; i++){
        long long x;
        cin >> x;
        if(x == -1) {
            U_A++;
        } else {
            arrA.push_back((int)x);
            if(x > maxA) maxA = x;
        }
    }
    for(int i = 0; i < N; i++){
        long long x;
        cin >> x;
        if(x == -1) {
            U_B++;
        } else {
            arrB.push_back((int)x);
            if(x > maxB) maxB = x;
        }
    }
    int aKnown = (int)arrA.size();
    int bKnown = (int)arrB.size();
    int need = max(aKnown - U_B, bKnown - U_A);
    if(need <= 0){
        cout << "Yes\n";
        return 0;
    }
    long long M = max(maxA, maxB);
    if(aKnown == 0 || bKnown == 0){
        // No pairs possible and still need >0 => impossible
        cout << "No\n";
        return 0;
    }
    sort(arrA.begin(), arrA.end());
    sort(arrB.begin(), arrB.end());
    vector<pair<int,int>> CA, CB;
    CA.reserve(arrA.size());
    CB.reserve(arrB.size());
    // build counts for A
    for(int i = 0, j; i < (int)arrA.size(); i = j){
        j = i+1;
        while(j < (int)arrA.size() && arrA[j] == arrA[i]) j++;
        CA.emplace_back(arrA[i], j - i);
    }
    // build counts for B
    for(int i = 0, j; i < (int)arrB.size(); i = j){
        j = i+1;
        while(j < (int)arrB.size() && arrB[j] == arrB[i]) j++;
        CB.emplace_back(arrB[i], j - i);
    }
    // build sum-weight pairs
    size_t dA = CA.size(), dB = CB.size();
    vector<pair<int,int>> ps;
    ps.reserve(dA * dB);
    for(size_t i = 0; i < dA; i++){
        int va = CA[i].first, ca = CA[i].second;
        for(size_t j = 0; j < dB; j++){
            int vb = CB[j].first, cb = CB[j].second;
            long long s = (long long)va + (long long)vb;
            if(s >= M){
                int w = ca < cb ? ca : cb;
                ps.emplace_back((int)s, w);
            }
        }
    }
    if(ps.empty()){
        cout << "No\n";
        return 0;
    }
    sort(ps.begin(), ps.end(), [](const pair<int,int> &a, const pair<int,int> &b){
        return a.first < b.first;
    });
    long long curS = ps[0].first;
    int sumW = 0;
    for(auto &p : ps){
        if(p.first != curS){
            if(sumW >= need){
                cout << "Yes\n";
                return 0;
            }
            curS = p.first;
            sumW = 0;
        }
        sumW += p.second;
    }
    if(sumW >= need){
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }
    return 0;
}