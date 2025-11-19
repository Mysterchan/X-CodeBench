#include <bits/stdc++.h>
using namespace std;

int main() {
	int N,M;cin >> N >> M;
	vector<int> A(M);
	vector<int> X;
	
	for(int i =0;i < M; i++){
		cin >> A[i];
	}
	
	for(int i =1; i < N;i++){
		X.push_back(i);
	}
	X.erase(remove_if(X.begin(), X.end(),
                      [&](int x){ return find(A.begin(), A.end(), x) != A.end(); }),
            X.end());
	
	cout << N-M <<endl;
	for(size_t i = 0; i <X.size();i++ ){
	cout << X[i] <<" ";
		if(i == X.size()-1){
		cout <<X[i]<<endl;
		}
	}
}