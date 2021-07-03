def search_insert(nums, target)
    i = 0
    j = nums.length
    while i < j
        mid = (i + j) / 2
        mid_val = nums[mid]
        return mid if mid_val == target
  
        if mid_val > target
            j = mid
        else
            i = mid + 1
        end
    end
    i
end