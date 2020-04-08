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
ListNode *middle_node(ListNode *head)
{
    ListNode *h = head, *t = head;
    while (h && h->next)
    {
        h = h->next->next;
        t = t->next;
    }
    return t;
}
