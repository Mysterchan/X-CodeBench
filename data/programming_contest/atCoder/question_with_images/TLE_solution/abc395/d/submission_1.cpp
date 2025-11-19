#include<iostream>
#include<set>
#include<string>
#include<vector>
#include<algorithm>
#include<cstring>
#include<stack>
#include<map>
#include<queue>

using namespace std;

const int N = 1e6 + 10;

int at[N] , n,q;

map<int,set<int> > ma;



int main(){


	cin>>n>>q;
	
	for(int i = 1; i <= n; i++){
		ma[i].insert(i);
		at[i] = i;
	}
	
	
	
	while(q--){
		int t,a,b;
		cin>>t;
		if(t == 1){
			cin>>a>>b;
			int num = at[a];
			ma[num].erase(a);
			at[a] = b;
			ma[b].insert(a);
		}
		else if(t == 2){
			cin>>a>>b;
			set<int> temp;
			temp = ma[a];
			ma[a] = ma[b];
			ma[b] = temp;
			
			set<int>::iterator it;
			for(it = ma[a].begin(); it != ma[a].end(); it++){
				at[*it] = a;
			}
			for(it = ma[b].begin(); it != ma[b].end(); it++){
				at[*it] = b;
			}
			
		}
		else if(t == 3){
			cin>>a;
			cout<<at[a]<<'\n';
		}
	}
	
	return 0;
}
