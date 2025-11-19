#include<bits/stdc++.h>
using namespace std;
using ll=long long;
int countDifferentSequences(const vector<int>& A) {
    int n = A.size();
    if (n == 0) return 0; 
    unordered_set<string> unique_sequences;
    string original;
    for (int num : A) {
        original += to_string(num) + ",";
    }
    unique_sequences.insert(original);
    for (int L = 0; L < n; ++L) {
        for (int R = L; R < n; ++R) {
            string seq;
            for (int i = 0; i < n; ++i) {
                if (i >= L && i <= R) {
                    seq += to_string(A[L]) + ",";
                } else {
                    seq += to_string(A[i]) + ",";
                }
            }
            unique_sequences.insert(seq);
        }
    } 
    return unique_sequences.size();
}
int main(){
	int n;
	cin>>n;
	vector<int>a(n);
	for(int i=0;i<n;i++){
		cin>>a[i];
	}
	cout<<countDifferentSequences(a);
	return 0;
}