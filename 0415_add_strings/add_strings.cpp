#include <iostream>
#include <string>

using namespace std;

// Time: O(m + n)
// Space: O(n)
string add_strings(string num1, string num2)
{
    int i = num1.size() - 1, j = num2.size() - 1, sum = 0;
    string res;
    while (i >= 0 || j >= 0 || sum)
    {
        if (i >= 0)
            sum += num1[i--] - '0';
        if (j >= 0)
            sum += num2[j--] - '0';
        res.insert(0, 1, (sum % 10) + '0');
        sum /= 10;
    }
    return res;
}