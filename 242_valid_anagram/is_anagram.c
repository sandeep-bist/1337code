#include <stdio.h>

/**
 * Time: O(n) 
 * Space: O(1)
 */
int is_anagram(char *s, char *t)
{
    if (strlen(s) != strlen(t))
        return 0;
    int alpha[26] = {};
    for (int i = 0; i < strlen(s); i++)
    {
        alpha[s[i] - 'a']++;
        alpha[t[i] - 'a']--;
    }
    for (int i = 0; i < 26; i++)
        if (alpha[i] > 0)
            return 0;
    return 1;
}
