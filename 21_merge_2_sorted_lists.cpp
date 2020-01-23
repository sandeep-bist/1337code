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
 * Merge two sorted linked lists and return it as a new list. The new list
 * should be made by splicing together the nodes of the first two lists.
 * 
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

int main()
{
    ListNode n1{1};
    ListNode n2(2);
    ListNode n3(4);

    n1.next = &n2;
    n2.next = &n3;

    ListNode n4{1};
    ListNode n5(3);
    ListNode n6(4);

    n4.next = &n5;
    n5.next = &n6;

    ListNode *tmp = merge_two_lists(&n1, &n4);
    while (tmp)
    {
        cout << tmp->val << " "; // 1 1 2 3 4 4
        tmp = tmp->next;
    }
    return 0;
}