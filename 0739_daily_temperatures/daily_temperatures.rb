def daily_temperatures(temperatures)
    # Time: O(n)
    # Space: O(n)
    res = Array.new(temperatures.size, 0)
    stack = []
  
    temperatures.each_with_index do |curr_temp, curr_day|
      while stack.any? && temperatures[stack.last] < curr_temp
        prev_day = stack.pop
        res[prev_day] = curr_day - prev_day
      end
      stack << curr_day
    end
    res
  end