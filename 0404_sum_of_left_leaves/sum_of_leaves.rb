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
# @return {Integer}
def sum_of_left_leaves(root)
    # Time: O(n)
    # Space: O(n)
    return dfs(root)
end

def dfs(node, is_left = false)
    return 0 if node.nil?
    if node.left.nil? && node.right.nil?
        return is_left ? node.val : 0
    end
    dfs(node.left, true) + dfs(node.right)
end