#include <iostream>
#include <stdlib.h>
#include <string>
using namespace std;
void lightshow(char* light, int num);
int main()
{
	int n = 0;
	cin >> n;
	char* light = (char*)malloc(sizeof(char) * (n + 1));
	for (int i = 1; i <= n; i++)
	{
		cin >> light[i];
	}
	lightshow(light, n);
	return 0;
}
void lightshow(char* light, int num)
{
	int timex = 0, timeo = 0;
	char past = ' ';
	string sx, so;
	int pastx = 0, pasto = 0;
	for (int i = 1; i <= num; i++)
	{
		if (past != 'x' && light[i] == 'x')
		{
			timex++;
			sx += "请" + to_string(i);
			pastx = i;
		}
		else if (past == 'x' && light[i] == 'o')
		{
			timex++;
			if (pastx == i - 1)
				sx += "切换开关\n";
			else
				sx += "到" + to_string(i - 1) + "切换开关\n";
		}

		if (past != 'o' && light[i] == 'o')
		{
			timeo++;
			so += "请" + to_string(i);
			pasto = i;
		}
		else if (past == 'o' && light[i] == 'x')
		{
			timeo++;
			if (pasto == i - 1)
				so += "切换开关\n";
			else
				so += "到" + to_string(i - 1) + "切换开关\n";
		}

		if (i == num)
		{
			if (light[i] == 'x')
			{
				if (pastx == i)
					sx += "切换开关\n";
				else
					sx += "到" + to_string(i) + "切换开关\n";
			}
			else if (light[i] == 'o')
			{
				if (pasto == i)
					so += "切换开关\n";
				else
					so += "到" + to_string(i) + "切换开关\n";
			}
		}
		past = light[i];
	}
	if (timex < timeo) cout << sx;
	else cout << so;
}