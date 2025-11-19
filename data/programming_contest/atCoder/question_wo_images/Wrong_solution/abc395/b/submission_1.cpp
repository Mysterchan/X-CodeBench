#include<bits/stdc++.h>

using namespace std;




int main() {
	
	int N;
	int i,sousa,tate,yoko;
	int pen = 1;

	cin >> N;
	
	vector<vector<int>> field(N,vector<int>(N,0));

	if( N % 2 == 1)
	{
		sousa = (N + 1) / 2;
	}
	else
	{
		sousa = N / 2;
	}
	
	cout << "sousa " << sousa << endl;
	
	for(i = 0 ;  i < sousa ; i++)
	{
		int kaishi = i;
		int owari  = N - i;
		for(tate = kaishi; tate < owari ; tate++)
		{
			for(yoko = kaishi; yoko < owari ;yoko ++)
			{
				field[tate][yoko] = pen;
			}
		}
		pen = pen * (-1);
	}
	
	for(tate=0 ; tate < N ; tate++)
	{
		for(yoko=0; yoko < N ;yoko++)
		{
			if(field[tate][yoko] == 1)
			{
				cout << "#";
			}
			else
			{
				cout << ".";
			}
		}
		cout << endl;
	}

}
