#include <iostream>

using namespace std;

class ListNode
{
public:
    int val;
    ListNode *next;
    ListNode(int x)
    {
        val = x;
        next = NULL;
    }
};

/**
 * Time: O(n)
 * Space: O(1)
 */
ListNode *remove_nth_from_end(ListNode *head, int n)
{
    ListNode *hare = head, *tort = head;
    while (n)
    {
        hare = hare->next;
        n--;
    }
    if (!hare)
        return head->next;
    while (hare->next)
    {
        hare = hare->next;
        tort = tort->next;
    }
    tort->next = tort->next->next;
    return head;
}
