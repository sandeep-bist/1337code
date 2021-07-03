# @param {Integer[]} nums
# @return {Integer}
def majority_element(nums)
    count = 0
    res = 0
    nums.each do |n|
        if count.zero?
            res = n
            count += 1
        elsif n == res
            count += 1
        else
            count -= 1
        end
    end
    res
end