# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @param {Integer} target_sum
# @return {Integer}

def path_sum(root, target_sum)
    # Time: O(n)
    # Space: O(n)
    return preorder(root, 0, target_sum, Hash.new(0))
end

def preorder(node, curr_sum, target, cache)
    return 0 if node.nil?
    curr_sum += node.val
    res = cache[curr_sum - target]
    res += 1 if curr_sum == target
    cache[curr_sum] += 1
    res += preorder(node.left, curr_sum, target, cache) + preorder(node.right, curr_sum, target, cache)
    cache[curr_sum] -= 1
    res
end