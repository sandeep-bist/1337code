#include <iostream>
#include <vector>
#include <string>

using namespace std;

/**
 * Knuth-Morris-Pratt string-searching algorithm. 
 */
vector<int> kmp_preprocess(string needle)
{
    int i = 0, j = 1, size = needle.size();
    vector<int> kmp(size, 0);
    while (j < size)
    {
        if (needle[j] == needle[i])
        {
            kmp[j] = i + 1;
            j++, i++;
        }
        else
        {
            if (i)
                i = kmp[i - 1];
            else
                j++;
        }
    }
    return kmp;
}

/**
 * Return the index of the first occurrence of needle in haystack, or -1 if
 * needle is not part of haystack.
 */
int strstr(string needle, string haystack)
{
    if (!needle.size() && !haystack.size())
        return 0;
    vector<int> kmp = kmp_preprocess(needle);
    int n = 0, h = 0;
    while (n < needle.size() && h < haystack.size())
    {
        if (needle[n] == haystack[h])
            n++, h++;
        else if (n)
            n = kmp[n - 1];
        else
            h++;
    }
    return n == needle.size() ? h - n : -1;
}

int main()
{
    cout << strstr("ll", "hello") << endl; // 2
    return 0;
}