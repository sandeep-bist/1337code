#include <iostream>

using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

int size(ListNode *head)
{
    ListNode *tmp = head;
    int i = 0;

    while (tmp)
    {
        i++;
        tmp = tmp->next;
    }
    return i;
}

/**
 * Time: O(m + n)
 * Space: O(1)
 */
ListNode *get_intersection_node(ListNode *headA, ListNode *headB)
{
    int sizeA, sizeB, diff;
    ListNode *big, *small;

    sizeA = size(headA);
    sizeB = size(headB);
    if (sizeA > sizeB)
    {
        big = headA;
        small = headB;
    }
    else
    {
        big = headB;
        small = headA;
    }
    diff = abs(sizeA - sizeB);
    for (int i = 0; i < diff; i++)
        big = big->next;
    while (big || small)
    {
        if (big == small)
            return big;
        big = big->next;
        small = small->next;
    }
    return NULL;
}
