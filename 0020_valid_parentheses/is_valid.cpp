#include <iostream>
#include <string>
#include <stack>

using namespace std;

// Time: O(n)
// Space: O(n)
bool is_valid(string s)
{
    stack<char> stack;
    for (auto c : s)
    {
        switch (c)
        {
        case '{':
            stack.push('}');
            break;
        case '[':
            stack.push(']');
            break;
        case '(':
            stack.push(')');
            break;
        default:
            if (!stack.size() || stack.top() != c)
                return false;
            stack.pop();
        }
    }
    return stack.empty();
}
