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
 * Given a linked list, remove the n-th node from the end of list and return
 * its head.
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

int main()
{
    ListNode n1(1);
    ListNode n2(2);
    ListNode n3(3);
    ListNode n4(4);
    ListNode n5(5);

    n1.next = &n2;
    n2.next = &n3;
    n3.next = &n4;
    n4.next = &n5;

    ListNode *res = remove_nth_from_end(&n1, 2);
    while (res)
    {
        cout << res->val << " "; // 1 2 3 5
        res = res->next;
    }
    return 0;
}