#include <iostream>

using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

/**
 * Time: O(n)
 * Space: O(1)
 */
ListNode *reverse_list(ListNode *head)
{
    ListNode *prev, *curr, *next;

    prev = NULL;
    curr = head;
    while (curr)
    {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}
