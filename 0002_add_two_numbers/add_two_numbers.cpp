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

ListNode *add_two_numbers_helper(ListNode *l1, ListNode *l2, int carry)
{
    if (!l1 && !l2 && !carry)
        return NULL;
    int temp = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + carry;
    ListNode *node = new ListNode(temp % 10);
    node->next = add_two_numbers_helper(
        l1 ? l1->next : NULL,
        l2 ? l2->next : NULL,
        temp > 9 ? 1 : 0);
    return node;
}

/**
 * Time: O(m + n)
 * Space: O(m + n)
 */
ListNode *add_two_numbers(ListNode *l1, ListNode *l2)
{
    return add_two_numbers_helper(l1, l2, 0);
}
