#include <iostream>
#include <string>
#include <vector>

using namespace std;

int num_decodings(string s)
{
    vector<int> dp(s.size() + 1, 0);
    dp[0] = 1;
    dp[1] = s[0] == '0' ? 0 : 1;
    for (int i = 2; i <= s.size(); i++)
    {
        int one_digit = stoi(s.substr(i - 1, 1));
        int two_digit = stoi(s.substr(i - 2, 2));
        if (one_digit >= 1)
            dp[i] += dp[i - 1];
        if (two_digit >= 10 && two_digit <= 26)
            dp[i] += dp[i - 2];
    }
    return dp[s.size()];
}

int main()
{
    cout << num_decodings("226") << endl; // 3
    cout << num_decodings("101") << endl; // 1
    return 0;
}