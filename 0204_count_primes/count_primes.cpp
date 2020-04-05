#include <iostream>
#include <vector>

using namespace std;

/**
 * Time: O(n) 
 * Space: O(n)
 */
int count_primes(int n)
{
    if (n <= 2)
        return 0;
    int res = 1, upper = sqrt(n);
    vector<int> primes(n, 0);
    for (int i = 3; i < n; i += 2)
        if (!primes[i])
        {
            res++;
            if (i > upper) // for overflow
                continue;
            for (int j = i * i; j < n; j += i)
                primes[j] = 1;
        }
    return res;
}
