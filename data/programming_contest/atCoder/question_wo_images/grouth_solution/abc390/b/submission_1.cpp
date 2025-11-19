#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i = 0; i < (n); i++)

int main() {
    int N; cin >> N;
    vector<long long>vec(N);
    rep(i,N)cin >> vec[i];
    bool flag = true;
    
    for(int i = 0; i<N-2;i++){
        if(vec[i+1]*vec[i+1]!=vec[i]*vec[i+2]){
            flag = false;
        }
    }
    if(flag)cout<<"Yes"<<endl;
	else cout<<"No"<<endl;
}