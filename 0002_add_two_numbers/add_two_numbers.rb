def add_two_numbers(l1, l2, carry = 0)
    return nil if (l1.nil? and l2.nil? and carry.zero?)
    tmp = (l1&.val || 0) + (l2&.val || 0) + carry
    return ListNode.new(tmp % 10).tap do |l3|
        l3.next = add_two_numbers(l1&.next, l2&.next, tmp / 10)
    end
end