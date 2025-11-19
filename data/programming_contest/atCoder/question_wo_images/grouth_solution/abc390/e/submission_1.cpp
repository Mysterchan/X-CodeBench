#include <bits/stdc++.h>
#include <vector>
using namespace std;

int main() {
	long long edb, mk, kaloria, ertek;
	int vitamin;
	cin >> edb >> mk;
	vector<vector<long long>> dp(4,vector<long long> (mk+2));

	for(int i = 1; i <= edb; i++)
	{
		cin >> vitamin >> ertek >> kaloria;
		for(int j = mk; j >= kaloria; j--)
		{
			dp[vitamin][j] = max(dp[vitamin][j], dp[vitamin][j-kaloria] + ertek);
		}
	}

	int egy = 0, ketto = 0, harom = 0;
	while (egy + ketto + harom < mk)
	{
		if(dp[1][egy] <= dp[2][ketto] && dp[1][egy] <= dp[3][harom])
		{
			egy++;
		}
		else if(dp[2][ketto] <= dp[1][egy] && dp[2][ketto] <= dp[3][harom])
		{
			ketto++;
		}
		else if(dp[3][harom] <= dp[1][egy] && dp[3][harom] <= dp[2][ketto])
		{
			harom++;
		}
	}


	cout << min({dp[1][egy], dp[2][ketto], dp[3][harom]});

	
}
