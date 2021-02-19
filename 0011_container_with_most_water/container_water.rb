def max_area(height)
    # Time: O(n)
    # Space: O(1)
    max = 0
    i, j = 0, height.length - 1
    while i < j do
        min = [height[i], height[j]].min
        max = [max, (j - i) * min].max
        if height[i] > height[j]
            j -=1
        else
            i += 1
        end
    end
    max
end