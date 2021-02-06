class TreeNode
    attr_accessor :val, :left, :right
    def initialize(val = 0, left = nil, right = nil)
        @val = val
        @left = left
        @right = right
    end
end

def right_side_view(root)
    # Time: O(n)
    # Space: O(n)
    return [] if root.nil?
    q, res = [], []
    q.append(root)
    until q.empty? do
        size, val = q.length, 0
        size.times do
          popped = q.shift
          val = popped.val
          q.append(popped.left) unless popped.left.nil?
          q.append(popped.right) unless popped.right.nil?
        end
        res.append(val)
    end
    res
end