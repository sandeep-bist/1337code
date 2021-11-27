def product_except_self(nums)
    # Time: O(n)
    # Space: O(n)
    n = nums.size
    res = [1] * n
    left = right = 1
    1.upto(n - 1) { |i|
        res[i] *= left *= nums[i - 1]
        res[~i] *= right *= nums[-i]
    }
    res
end