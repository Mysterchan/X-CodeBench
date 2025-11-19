#include<bits/stdc++.h> 
using namespace std;
int main()
{
	int x;
	cin>>x;
	int ret=0;
	for(int i=0;i=9;i++)
		for(int j=0;j<=9;j++)
			if(i*j!=x)
				ret+=i*j;
	cout<<ret<<endl;
	return 0;
}