#include <iostream>
#include <string>
#include <stack>

using namespace std;

/**
 * Given a string containing just the characters '(', ')', '{', '}', '[' and
 * ']', determine if the input string is valid.
 * 
 * An input string is valid if:
 * Open brackets must be closed by the same type of brackets.
 * Open brackets must be closed in the correct order.
 * Note that an empty string is also considered valid.
 */
bool isValid(string s)
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

int main()
{
    cout << isValid("(())") << endl;   // 1
    cout << isValid("]") << endl;      // 0
    cout << isValid("()[]{}") << endl; // 1
    cout << isValid("(]") << endl;     // 0
    cout << isValid("([)]") << endl;   // 0
    cout << isValid("{[]}") << endl;   // 1
    return 0;
}