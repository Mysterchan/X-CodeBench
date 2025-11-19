#include<iostream>
#include<algorithm>

int main()
{
	std::string s;
	std::cin >> s;
	for (unsigned i = 0; i + 1 < s.size(); ++i)
	{
		if (s[i] == 'W' and s[i+1] == 'A') 
		{
			s[i] = 'A';
			s[i + 1] = 'C';
		}
	}
	
	std::cout << s << "\n";
}