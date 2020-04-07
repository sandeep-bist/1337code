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
ListNode *remove_elements(ListNode *head, int val)
{
    ListNode *s = new ListNode(-1);
    s->next = head;
    ListNode *prev = s, *curr = head;
    while (curr)
    {
        if (curr->val == val)
            prev->next = curr->next;
        else
            prev = curr;
        curr = curr->next;
    }
    return s->next;
}
