# @param {Integer[]} nums
# @return {Integer}
def max_sub_array(nums)
    return 0 if nums.empty?
    max_curr = max_so_far = nums[0]
    nums[1..].each do |n|
        max_curr = [n, max_curr + n].max
        max_so_far = [max_curr, max_so_far].max
    end
    max_so_far
end