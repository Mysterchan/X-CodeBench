#include<bits/stdc++.h>
using namespace std;
unordered_set<int> st;
vector<int> b;
int n;
int a[20];
void dfs(int i){
	if(i==n){
		int tmp=0;
		for(auto x:b) tmp^=x;
		st.insert(tmp);
		return ;
	} 
	for(int j=0;j<(int)b.size();j++){
		b[j]+=a[i];
		dfs(i+1);
		b[j]-=a[i];
	}
	b.push_back(a[i]);
	dfs(i+1);
	b.pop_back();
}
int main(){
	cin>>n;
	for(int i=0;i<n;i++) cin>>a[i];
	dfs(0);
	cout<<st.size()<<endl;
	return 0;
}
