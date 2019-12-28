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
 * Helper.
 */
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
 * Given an array of integers, return indices of the two numbers 
 * such that they add up to a specific target. 
 * You may assume that each input would have exactly one solution,
 * and you may not use the same element twice.
 */
ListNode *add_two_numbers(ListNode *l1, ListNode *l2)
{
    return add_two_numbers_helper(l1, l2, 0);
}

int main()
{
    ListNode n1(2);
    ListNode n2(4);
    ListNode n3(3);

    n1.next = &n2;
    n2.next = &n3;

    ListNode n4(5);
    ListNode n5(6);
    ListNode n6(4);

    n4.next = &n5;
    n5.next = &n6;

    ListNode *res = add_two_numbers(&n1, &n4);
    while (res)
    {
        cout << res->val << " ";
        res = res->next;
    }
    /* 7 0 8 */
    return 0;
}