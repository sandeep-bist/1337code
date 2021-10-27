def sort_colors(nums)
    # Time: O(n)
    # Space: O(1)
    c = c0 = 0
    c2 = nums.length - 1
    while c <= c2
        if nums[c] == 0
            nums[c], nums[c0] = nums[c0], nums[c]
            c0 += 1
            c += 1
        elsif nums[c] == 1
            c += 1
        else
            nums[c], nums[c2] = nums[c2], nums[c]
            c2 -= 1
        end
    end
end