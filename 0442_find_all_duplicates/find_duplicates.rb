def find_duplicates(nums)
  # Time: O(n)
  # Space: O(1)
  [].tap do |res|
    nums.each do |n|
      i = n.abs
      res << i if nums[i - 1] < 0
      nums[i - 1] *= -1  
    end
  end
end