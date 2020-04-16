#include <iostream>
#include <string>

using namespace std;

/**
 * Time: O(n) 
 * Space: O(1)
 */
bool check_valid_string(string s)
{
    int curr_min = 0, curr_max = 0;
    for (auto i : s)
    {
        curr_min = i == '(' ? curr_min + 1 : max(curr_min - 1, 0);
        curr_max = i == ')' ? curr_max - 1 : curr_max + 1;
        if (curr_max < 0)
            return false;
    }
    return !curr_min;
}
