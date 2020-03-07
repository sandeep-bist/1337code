#include <iostream>

using namespace std;

class ListNode
{
public:
    int val;
    ListNode *next;
    ListNode(int val);
};

ListNode::ListNode(int val)
{
    this->val = val;
    this->next = NULL;
}

/**
 * Time: O(m + n)
 * Space: O(m + n)
 */
ListNode *merge_two_lists(ListNode *l1, ListNode *l2)
{
    ListNode *head = new ListNode(0);
    ListNode *curr = head;
    while (l1 && l2)
    {
        if (l1->val > l2->val)
        {
            curr->next = l2;
            l2 = l2->next;
        }
        else
        {
            curr->next = l1;
            l1 = l1->next;
        }
        curr = curr->next;
    };
    curr->next = l1 ? l1 : l2;
    return head->next;
}