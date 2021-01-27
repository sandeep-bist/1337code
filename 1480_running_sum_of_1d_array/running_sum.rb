# @param {Integer[]} nums
# @return {Integer[]}
def running_sum(nums)
    # Time: O(n)
    # Space: O(n)
    res = []
    tmp = 0
    nums.each do |n|
      tmp += n
      res.append(tmp)
    end
    res
end