# Definition for singly-linked list.
class ListNode
    attr_accessor :val, :next
    def initialize(val = 0, _next = nil)
        @val = val
        @next = _next
    end
end
# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def merge_two_lists(l1, l2)
    sent = ListNode.new
    curr = sent
    until l1.nil? || l2.nil?
        if l1.val <= l2.val
            curr.next = l1
            l1 = l1.next
        else
            curr.next = l2
            l2 = l2.next
        end
        curr = curr.next
    end
    curr.next = l1.nil? ? l2 : l1
    sent.next
end