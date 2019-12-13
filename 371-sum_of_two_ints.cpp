#include <iostream>
#include <vector>

using namespace std;

int getSum(int a, int b)
{
    return b == 0 ? a : getSum(a ^ b, (unsigned int)(a & b) << 1);
}

int main()
{
    cout << getSum(-1, 1) << endl;  // 0
    cout << getSum(-4, 20) << endl; // 16
    return 0;
}