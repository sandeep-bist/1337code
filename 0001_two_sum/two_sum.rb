def two_sum(nums, target)
    map = {}
    nums.each_with_index do |num, index|
        compliment = target - num
        return [map[num], index] if map.key?(num)
        map[compliment] = index
    end
    []
end