#include <iostream>
#include <string>

using namespace std;

/**
 * Time: O(n)
 * Space: O(1) 
 */
string defang_IP_addr(string address)
{
    string res = "";
    for (int i = 0; i < address.size(); i++)
    {
        char c = address[i];
        if (c == '.')
            res.append("[.]");
        else
            res += c;
    }
    return res;
}
